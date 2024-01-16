import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 20,  // 20 Virtual Users
  interactions: 40, // 20 interactions per Virtual users 20 * 40
  duration: '60s', // test duration time 40 seconds
};

// 10 * 20 = 200 request to get/pedido in 40 seconds
export default function () {
  http.get("http://a094291329d9b48bba7b166b013a1af7-427386988.us-east-1.elb.amazonaws.com:8000/v1/usuario/");
  sleep(1);
}