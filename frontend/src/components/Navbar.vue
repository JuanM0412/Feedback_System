<template>
  <nav class="bg-white dark:bg-gray-900 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="text-xl font-bold text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors duration-200">
            SalesAnalyzer
          </router-link>
        </div>
        
        <div class="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
          <template v-if="isAuthenticated">
            <router-link 
              to="/rubrica" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400 transition-colors duration-200"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Rúbrica
            </router-link>
            <router-link 
              to="/business" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400 transition-colors duration-200"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Negocio
            </router-link>
            <button 
              @click="handleLogout"
              :disabled="loading"
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!loading">Cerrar Sesión</span>
              <span v-else class="flex items-center">
                <svg class="animate-spin -ml-1 mr-2 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Saliendo...
              </span>
            </button>
          </template>
          <template v-else>
            <router-link 
              to="/login" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400 transition-colors duration-200"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Iniciar Sesión
            </router-link>
            <router-link 
              to="/register" 
              class="px-3 py-2 rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200"
              active-class="bg-blue-700"
            >
              Registrarse
            </router-link>
          </template>
        </div>

        <!-- Mobile menu button -->
        <div class="sm:hidden flex items-center">
          <button 
            @click="toggleMobileMenu"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
          >
            <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
              <path v-if="!showMobileMenu" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile menu -->
      <div v-show="showMobileMenu" class="sm:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1">
          <template v-if="isAuthenticated">
            <router-link 
              to="/rubrica" 
              @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Rúbrica
            </router-link>
            <router-link 
              to="/business" 
              @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Negocio
            </router-link>
            <button 
              @click="handleLogout"
              :disabled="loading"
              class="block w-full text-left px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 disabled:opacity-50"
            >
              <span v-if="!loading">Cerrar Sesión</span>
              <span v-else>Saliendo...</span>
            </button>
          </template>
          <template v-else>
            <router-link 
              to="/login" 
              @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800"
              active-class="bg-blue-100 dark:bg-blue-800 text-blue-600 dark:text-blue-400"
            >
              Iniciar Sesión
            </router-link>
            <router-link 
              to="/register" 
              @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-white bg-blue-600 hover:bg-blue-700"
              active-class="bg-blue-700"
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
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { userStore } from '../store/userStore';

const router = useRouter();

const loading = ref(false);
const showMobileMenu = ref(false);

const isAuthenticated = computed(() => userStore.isAuthenticated);

const handleLogout = async () => {
  try {
    loading.value = true;
    userStore.logout();
    showMobileMenu.value = false;
    await router.push('/login');
  } catch (error) {
    console.error('Logout error:', error);
  } finally {
    loading.value = false;
  }
};

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value;
};

const closeMobileMenu = () => {
  showMobileMenu.value = false;
};
</script>