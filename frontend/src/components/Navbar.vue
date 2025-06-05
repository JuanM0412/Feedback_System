<template>
  <nav class="bg-white dark:bg-gray-900 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="text-xl font-bold text-blue-600 dark:text-blue-400">
            SalesAnalyzer
          </router-link>
        </div>
        
        <div class="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
          <template v-if="isAuthenticated">
            <router-link 
              to="/rubrica" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
              active-class="bg-blue-100 dark:bg-blue-800"
            >
              Rúbrica
            </router-link>
            <router-link 
              to="/business" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
              active-class="bg-blue-100 dark:bg-blue-800"
            >
              Negocio
            </router-link>
            <button 
              @click="handleLogout"
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
            >
              Cerrar Sesión
            </button>
          </template>
          <template v-else>
            <router-link 
              to="/login" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
            >
              Iniciar Sesión
            </router-link>
            <router-link 
              to="/register" 
              class="px-3 py-2 rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
            >
              Registrarse
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useAuth } from '../services/AuthService';
import axios from 'axios';

const { user, logout, refreshUser } = useAuth();

const isAuthenticated = computed(() => !!user.value);

const handleLogout = async () => {
  await logout();
  window.location.reload();
};
</script>