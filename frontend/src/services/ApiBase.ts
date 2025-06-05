import axios from 'axios';

declare module 'axios' {
  interface AxiosInstance {
    isAxiosError(payload: any): payload is AxiosError;
  }
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;