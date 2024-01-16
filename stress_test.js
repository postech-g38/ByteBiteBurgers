import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 20,  // 20 Virtual Users
  interactions: 40, // 20 interactions per Virtual users 20 * 40
  duration: '60s', // test duration time 40 seconds
};

// 10 * 20 = 200 request to get/pedido in 40 seconds
export default function () {
  http.get(`${EKSHOST}:8000/v1/usuario/`);
  sleep(1);
}