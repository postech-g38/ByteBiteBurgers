import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 20,  // 10 Virtual Users
  interactions: 50, // 20 interactions per Virtual users 10 * 20
  duration: '60s', // test duration time 40 seconds
};

// 10 * 20 = 200 request to get/pedido in 40 seconds
export default function () {
  http.get("http://aea830e58c65a4b6ca8f25b3eb251257-1762251680.us-east-1.elb.amazonaws.com:8000/v1/usuario/");
  sleep(1);
}