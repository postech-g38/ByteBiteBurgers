from src.adapters.api.bytebiteburgers.settings import ByteBiteBurguers

from src.settings import get_settings

def bytebiteburguers_facade() -> ByteBiteBurguers:
    return ByteBiteBurguers(
        host=get_settings().api_byte_bite_burguer.byte_bite_burguers_host
    )
