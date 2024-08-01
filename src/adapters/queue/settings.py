from typing import Dict, Any, Optional, List
import logging
import json
import asyncio

import boto3

from src.adapters.database.settings import get_session
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.services.pagamento_service import PagamentoService
from src.adapters.api.bytebiteburgers.settings import ByteBiteBurguers
from src.settings import get_settings

_logger = logging.getLogger(__name__)


class AwsSQS:
    def __init__(self, name: Optional[str] = None, url: Optional[str] = None) -> None:
        self._client = boto3.client('sqs')
        self._reference = name or url

    def publish_message(self, message: Dict[str, Any], key: Optional[str] = None) -> Dict[str, Any]:
        response = self._client.send_message(
            QueueUrl=self._reference, 
            MessageBody=json.dumps(message)
        )
        return response
    
    async def consume_message(
        self, 
        max_message: int = 5, 
        visibility_timeout_seconds: int = 20, 
        wait_seconds: int = 2
    ) -> List[Dict[str, str | bytes]]:
        response = self._client.receive_message(
            QueueUrl=self._reference,
            MaxNumberOfMessages=max_message,
            VisibilityTimeout=visibility_timeout_seconds,
            WaitTimeSeconds=wait_seconds,
        )
        return response
    
    def delete_message(self, handle: str) -> Dict[str, str]:
        response = self._client.delete_message(
            QueueUrl=self._reference,
            ReceiptHandle=handle
        )
        return response
    
    async def exec(self) -> None:
        _logger.error(f"INFO:     Broker Listening to  AWS SQS {self._reference}")
        while True:
            try:
                await asyncio.sleep(2)
                _logger.info('Brokcer checking AWS SQS [every 2s]')
                result = await self.consume_message()
                
                if 'Messages' in result:
                    message_digest = True
                    
                    for message in result['Messages']:
                        body = json.loads(message['Body'])
                        logging.info(f"Message: {body}")
                        handle = message['ReceiptHandle']
                        
                        with get_session() as session:
                            service = PagamentoService(
                                PagamentoRepository(session),
                                ByteBiteBurguers(get_settings().api_byte_bite_burguer.byte_bite_burguers_host)
                            )
                            result = service.create(
                                PagamentoPayloadSchema.model_validate(body)
                            )
                            logging.info(f"Digest: {result}")

                else:
                    message_digest = False
                    logging.info('No messages to process')

            except Exception as e:
                logging.error(e)
                
            else:
                if message_digest:
                    self.delete_message(handle)
