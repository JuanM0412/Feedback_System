<template>
  <main class="flex-grow w-full flex items-center justify-center bg-gradient-to-r from-blue-600 to-blue-800 min-h-screen md:px-6 lg:px-8 mt-16">
    <div class="w-full">
      <div class="flex justify-between items-center mb-8 px-4 md:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Usuarios Registrados</h1>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mx-4 md:mx-6 lg:mx-8 overflow-x-auto">
        <table class="min-w-full table-auto border-collapse">
          <thead>
            <tr class="bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-left text-sm uppercase font-semibold">
              <th class="px-4 py-3 border-b dark:border-gray-600">Usuario</th>
              <th class="px-4 py-3 border-b dark:border-gray-600">Correo</th>
              <th class="px-4 py-3 border-b dark:border-gray-600">Rol</th>
              <th class="px-4 py-3 border-b dark:border-gray-600">Estado</th>
              <th class="px-4 py-3 border-b dark:border-gray-600">Acciones</th>

            </tr>
          </thead>
          <tbody>
            <tr
              v-for="user in users"
              :key="user.id"
              class="border-b hover:bg-gray-50 dark:hover:bg-gray-700 dark:border-gray-700"
            >
              <td class="px-4 py-3 text-gray-900 dark:text-white">{{ user.username }}</td>
              <td class="px-4 py-3 text-gray-700 dark:text-gray-300">{{ user.email }}</td>
              <td class="px-4 py-3 text-gray-700 dark:text-gray-300">
                {{ user.type ? 'Administrador' : 'Usuario' }}
              </td>
              <td class="px-4 py-3 text-gray-700 dark:text-gray-300">
                {{ user.state ? 'Activo' : 'Inactivo' }}
              </td>
              <td class="px-4 py-3 text-gray-700 dark:text-gray-300">
                <button
                  class="px-3 py-1 text-sm rounded-md font-medium transition-colors duration-200"
                  :class="user.state
                    ? 'bg-red-500 text-white hover:bg-red-600'
                    : 'bg-green-500 text-white hover:bg-green-600'"
                  @click="toggleUserState(user)"
                >
                  {{ user.state ? 'Desactivar' : 'Activar' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <p
          v-if="users.length === 0"
          class="text-gray-600 dark:text-gray-300 mt-4 text-center"
        >
          No hay usuarios registrados.
        </p>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { UserResponse } from '../interfaces/User';
import UserService from '../services/UserService';

const users = ref<UserResponse[]>([]);

const fetchUsers = async () => {
  try {
    const response = await UserService.getUsers();
    users.value = response;
  } catch (err) {
    console.error('Error cargando usuarios:', err);
  }
};

const toggleUserState = async (user: UserResponse) => {
  try {
    if (user.state) {
      await UserService.deactivateUserById(user.id.toString());
    } else {
      await UserService.activateUserById(user.id.toString());
    }
    await fetchUsers();
  } catch (error) {
    console.error('Error cambiando estado del usuario:', error);
  }
};

onMounted(fetchUsers);
</script>
