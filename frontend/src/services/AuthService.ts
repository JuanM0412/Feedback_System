import axios from 'axios';
import type { AxiosResponse } from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'; // Fallback para desarrollo

interface User {
  email: string;
  username: string;
}

interface AuthResponse {
  access_token: string;
  token_type: string;
}

export const useAuth = () => {
  const router = useRouter();
  const user = ref<User | null>(null);
  const error = ref<string | null>(null);
  const loading = ref<boolean>(false);

  const api = axios.create({
    baseURL: API_URL,
    headers: {
      'Content-Type': 'application/json',
    },
    withCredentials: true
  });

  api.interceptors.request.use((config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });

  api.interceptors.response.use(
    (response) => response,
    (err) => {
      if (err.response.status === 401) {
        logout();
        router.push('/login');
      }
      return Promise.reject(err);
    }
  );

  const login = async (email: string, password: string) => {
    try {
      loading.value = true;
      error.value = null;
      
      const params = new URLSearchParams();
      params.append('username', email);
      params.append('password', password);
  
      const response: AxiosResponse<AuthResponse> = await api.post('/auth/token', params, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });
      
      localStorage.setItem('access_token', response.data.access_token);
      await fetchUser();
      
      router.push('/rubrica');
    } catch (err) {
      error.value = 'Credenciales incorrectas. Por favor, inténtalo de nuevo.';
      console.error('Login error:', err);
    } finally {
      loading.value = false;
    }
  };

  const register = async (email: string, username: string, password: string) => {
    try {
      loading.value = true;
      error.value = null;
      
      // 1. Primero hacemos el registro
      const registerResponse = await api.post('/auth/register', {
        email,
        username,
        password
      }, {
        headers: {
          'Content-Type': 'application/json' // Asegurar el content-type correcto
        }
      });
  
      // 2. Si el registro fue exitoso, hacemos login automático
      if (registerResponse.status === 200 || registerResponse.status === 201) {
        const params = new URLSearchParams();
        params.append('username', email);
        params.append('password', password);
  
        const loginResponse = await api.post('/auth/token', params, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        });
  
        localStorage.setItem('access_token', loginResponse.data.access_token);
        await fetchUser();
        router.push('/rubrica');
      }
    } catch (err: any) {
      console.error('Register error:', err);
      
      // Manejo más específico de errores
      if (err.response) {
        if (err.response.status === 400) {
          error.value = err.response.data.detail || 'Datos inválidos. Verifica tu información.';
        } else if (err.response.status === 409) {
          error.value = 'El usuario o correo electrónico ya existe';
        } else {
          error.value = `Error del servidor: ${err.response.status}`;
        }
      } else if (err.request) {
        // La solicitud fue hecha pero no se recibió respuesta
        error.value = 'No se recibió respuesta del servidor';
      } else {
        // Error al configurar la solicitud
        error.value = 'Error de conexión. Verifica tu red.';
      }
    } finally {
      loading.value = false;
    }
  };

  const fetchUser = async (): Promise<boolean> => {
    try {
      const response = await api.get('/auth/me');
      user.value = response.data;
      return true;
    } catch (err) {
      console.error('Failed to fetch user:', err);
      logout();
      return false;
    }
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    user.value = null;
    router.push('/login');
  };

  const init = async () => {
    const token = localStorage.getItem('access_token');
    if (token) {
      const success = await fetchUser();
      if (!success) {
        router.push('/login');
      }
    }
  };

  const updateProfile = async (data: { evaluation_rubric?: string; business_summary?: string }) => {
    try {
      const response = await api.patch('/auth/me', data);
      if (user.value) {
        user.value = { ...user.value, ...response.data };
      }
      return response.data;
    } catch (err) {
      console.error('Update profile error:', err);
      throw err;
    }
  };

  const refreshUser = async () => {
    await fetchUser();
  };

  init();

  return {
    user,
    error,
    loading,
    api,
    login,
    register,
    logout,
    fetchUser,
    updateProfile
  };
};