<template>
  <nav class="bg-white dark:bg-gray-900 fixed w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <!-- Logo -->
      <router-link to="/" class="flex items-center space-x-3 rtl:space-x-reverse">
        <img src="https://flowbite.com/docs/images/logo.svg" class="h-8" alt="Logo" />
        <span class="self-center text-2xl font-semibold whitespace-nowrap text-gray-900 dark:text-white">SalesAnalyzer</span>
      </router-link>

      <!-- Botones autenticación (versión escritorio) -->
      <div class="hidden md:flex md:order-2 gap-3 rtl:gap-reverse">
        <template v-if="isAuthenticated">
          <button
            @click="handleLogout"
            :disabled="loading"
            class="text-gray-700 dark:text-gray-300 hover:text-blue-700 dark:hover:text-blue-500 font-medium rounded-lg text-sm px-4 py-2 text-center transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
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
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Iniciar Sesión
          </router-link>
          <router-link
            to="/register"
            class="text-blue-700 bg-white hover:bg-gray-100 border border-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-gray-900 dark:text-blue-500 dark:border-blue-500 dark:hover:bg-gray-800 dark:hover:text-white dark:focus:ring-blue-800"
          >
            Registrarse
          </router-link>
        </template>
        <!-- Botón menú mobile -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden inline-flex items-center justify-center p-2 text-gray-500 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:focus:ring-gray-600"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!showMobileMenu" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Menú principal -->
      <div :class="['items-center justify-between w-full md:flex md:w-auto md:order-1', showMobileMenu ? 'block' : 'hidden']">
        <ul
          class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
        >
          <template v-if="isAuthenticated">
            <li>
              <router-link
                to="/rubrica"
                class="block py-2 px-3 rounded text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                active-class="text-blue-700 md:text-blue-700 dark:text-blue-500"
                @click="closeMobileMenu"
              >Rúbrica</router-link>
            </li>
            <li>
              <router-link
                to="/business"
                class="block py-2 px-3 rounded text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                active-class="text-blue-700 md:text-blue-700 dark:text-blue-500"
                @click="closeMobileMenu"
              >Negocio</router-link>
            </li>
          </template>
          <template v-else>
            <li>
              <router-link
                to="/"
                class="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500"
                aria-current="page"
                @click="closeMobileMenu"
              >Página Principal</router-link>
            </li>
            <li>
              <router-link
                to="/about"
                class="block py-2 px-3 rounded text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                @click="closeMobileMenu"
              >Acerca de Nosotros</router-link>
            </li>
            <li>
              <router-link
                to="/services"
                class="block py-2 px-3 rounded text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                @click="closeMobileMenu"
              >Servicios</router-link>
            </li>
            <li>
              <router-link
                to="/contact"
                class="block py-2 px-3 rounded text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                @click="closeMobileMenu"
              >Contacto</router-link>
            </li>
          </template>
        </ul>
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