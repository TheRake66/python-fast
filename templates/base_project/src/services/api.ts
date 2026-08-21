import axios from 'axios';
import configuration from '../configuration.json';

const conf = configuration.api;
const prot = conf.ssl ? 'https' : 'http';

const api = axios.create({
  baseURL: `${prot}://${conf.server}:${conf.port}/api/${conf.version}/`,
  headers: { 'Content-Type': 'application/json' },
  timeout: 10000
});

export default api;