import api, { isAxiosError } from '../services/ApiBase';
import type { UserCreate } from '../interfaces/User';
import type { AuthResponse } from '../interfaces/Auth';
import type { ApiErrorResponse } from '../interfaces/ApiErrorResponse';

class UserService {
  async register(userData: UserCreate): Promise<AuthResponse> {
    try {
      const response = await api.post<AuthResponse>('/auth/admin/create_user', userData);
      
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
      const formData = new URLSearchParams();
      formData.append('username', credentials.email);
      formData.append('password', credentials.password);

      const response = await api.post<AuthResponse>(
        '/auth/token',
        formData,
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }
      );

      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.detail || errorData?.message || 'Error logging in');
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

  async getUsers(): Promise<any> {
    try {
      const response = await api.get('/auth/admin/users');
      return response.data;
    } catch (error: unknown) {
      if (isAxiosError(error)) {
        const errorData = error.response?.data as ApiErrorResponse;
        throw new Error(errorData?.message || 'Error al obtener los usuarios');
      }
      throw new Error('Unknown error while fetching users');
    }
  }
}

export default new UserService();
