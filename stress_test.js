import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10,  // 10 Virtual Users
  interactions: 20, // 20 interactions per Virtual users 10 * 20
  duration: '40s', // test duration time 40 seconds
};

// 10 * 20 = 200 request to get/pedido in 40 seconds
export default function () {
  http.get('http://ad284c1ac441545f18154385f507000c-2108317586.us-east-1.elb.amazonaws.com:8000/v1/pedido/');
  sleep(1);
}