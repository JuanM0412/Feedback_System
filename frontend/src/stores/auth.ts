import { defineStore } from 'pinia';
import { useAuth } from '@/services/AuthService';
import { ref, computed } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const { 
    user, 
    error, 
    loading, 
    login, 
    register, 
    logout, 
    fetchUser,
    updateProfile,
    refreshUser 
  } = useAuth();
  
  const isAuthenticated = computed(() => !!user.value);
  
  return {
    user,
    error,
    loading,
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser,
    updateProfile,
    refreshUser
  };
});