import api, { isAxiosError } from '../services/ApiBase';
import type { UserCreate } from '../interfaces/User';
import type { AuthResponse } from '../interfaces/Auth';
import type { ApiErrorResponse } from '../interfaces/ApiErrorResponse';

class UserService {
  async register(userData: UserCreate): Promise<AuthResponse> {
    try {
      const response = await api.post<AuthResponse>('/auth/register', userData);
      
      if (!response.data?.data?.access_token) {
        throw new Error(response.data?.message || 'Registration failed');
      }
      
      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.detail || errorData?.message || 'Error registering user');
      }
      throw new Error('Unknown error during registration');
    }
  }

  async login(credentials: { email: string; password: string }): Promise<AuthResponse> {
    try {
      const response = await api.post<AuthResponse>('/auth/token', credentials);

      if (!response.data || !response.data.id) {
        throw new Error(response.data.message || 'Login failed');
      }

      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error logging in');
      }
      throw new Error('Unknown error while logging in');
    }
  }

  async refreshToken(refreshToken: string): Promise<AuthResponse> {
    try {
      const response = await api.post<AuthResponse>('/auth/refresh', {
        refresh_token: refreshToken
      });
      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error refreshing token');
      }
      throw new Error('Unknown error while refreshing token');
    }
  }

  async saveRubrica(data: { evaluation_rubric: string }): Promise<any> {
    try {
      const response = await api.put('/auth/me', data);
      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error al guardar la rúbrica');
      }
      throw new Error('Unknown error while saving rubric');
    }
  }

  async saveBusinessInfo(data: { business_summary: string }): Promise<any> {
    try {
      const response = await api.put('/auth/me', data);
      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error al guardar la descripción del negocio');
      }
      throw new Error('Unknown error while saving business description');
    }
  }

  async getRubrica(): Promise<{ evaluation_rubric: string }> {
    try {
      const response = await api.get('/auth/me');
      return { evaluation_rubric: response.data?.evaluation_rubric || '' };
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error al obtener la rúbrica');
      }
      throw new Error('Unknown error while fetching rubric');
    }
  }

  async getBusinessInfo(): Promise<{ business_summary: string }> {
    try {
      const response = await api.get('/auth/me');
      return { business_summary: response.data?.business_summary || '' };
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error al obtener la descripción del negocio');
      }
      throw new Error('Unknown error while fetching business summary');
    }
  }
}

export default new UserService();
