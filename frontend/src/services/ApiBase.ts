import axios, { AxiosError } from 'axios';
import { userStore } from '../store/userStore';

declare module 'axios' {
  interface AxiosInstance {
    isAxiosError(payload: any): payload is AxiosError;
  }
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },
});

api.isAxiosError = (payload: any): payload is AxiosError => {
  return (payload as AxiosError).isAxiosError !== undefined;
};

api.interceptors.request.use(
  (config) => {
    const token = userStore.access_token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      !originalRequest.url.includes('/auth/refresh') &&
      !originalRequest.url.includes('/auth/login')
    ) {
      originalRequest._retry = true;

      try {
        const refreshed = await userStore.refreshToken();
        if (refreshed) {
          originalRequest.headers.Authorization = `Bearer ${userStore.access_token}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        console.error('Refresh token failed:', refreshError);
        userStore.logout();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export const isAxiosError = api.isAxiosError;

export default api;
