<template>
  <main class="flex-grow w-full flex items-center justify-center bg-gradient-to-r from-blue-600 to-blue-800 min-h-screen">
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow-xl p-8 w-full max-w-md mx-4">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white mb-2">Crear Nuevo Usuario</h1>
      </div>

      <form @submit.prevent="register" class="space-y-6">
        <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span class="block sm:inline">{{ errorMessage }}</span>
        </div>

        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Correo Electrónico
          </label>
          <input
            id="email"
            v-model="userData.email"
            type="email"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="tu@email.com"
          />
        </div>

        <!-- Username -->
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Nombre de Usuario
          </label>
          <input
            id="username"
            v-model="userData.username"
            type="text"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="nombredeusuario"
          />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Contraseña
          </label>
          <input
            id="password"
            v-model="userData.password"
            type="password"
            required
            minlength="6"
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
            placeholder="••••••••"
          />
        </div>

        <!-- User Type -->
        <div>
          <label for="type" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Tipo de Usuario
          </label>
          <select
            id="type"
            v-model="userData.type"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          >
            <option :value="false">Usuario</option>
            <option :value="true">Administrador</option>
          </select>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            :disabled="loading"
            class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!loading">Crear Usuario</span>
            <span v-else class="flex items-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Creando...
            </span>
          </button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import UserService from '../services/UserService';
import { userStore } from '../store/userStore';

const router = useRouter();

const userData = ref({
  email: '',
  username: '',
  password: '',
  type: false
});

const loading = ref(false);
const errorMessage = ref('');

const register = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';

    const { email, username, password, type } = userData.value;

    if (!email || !username || !password || type === null || type === undefined) {
      errorMessage.value = 'Todos los campos son requeridos';
      return;
    }

    if (password.length < 6) {
      errorMessage.value = 'La contraseña debe tener al menos 6 caracteres';
      return;
    }

    const response = await UserService.register({
      email,
      username,
      password,
      type
    });

    await router.push('users');
  } catch (error: unknown) {
    errorMessage.value = error instanceof Error ? error.message : 'Ocurrió un error al registrarse';
    console.error('Register error:', error);
  } finally {
    loading.value = false;
  }
};
</script>