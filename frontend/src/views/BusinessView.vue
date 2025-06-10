<template>
  <main class="flex-grow w-full py-8 px-4 md:px-6 lg:px-8 mt-16">
    <div class="w-full">
      <div class="flex justify-between items-center mb-8 px-4 md:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Descripción del Negocio</h1>
        <div class="flex gap-2">
          <button 
            v-if="hasBusinessInfo && !isEditing"
            @click="enableEditing"
            class="bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded-md transition-colors duration-200"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
            Editar
          </button>
          <button 
            @click="saveBusiness"
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            :disabled="loading || (hasBusinessInfo && !isEditing)"
          >
            <span v-if="!loading">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              Guardar
            </span>
            <span v-else class="flex items-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Guardando...
            </span>
          </button>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-6 mx-4 md:mx-6 lg:mx-8">
        <h2 class="text-xl font-semibold mb-2 dark:text-white">Importancia de la Descripción del Negocio</h2>
        <p class="text-gray-700 dark:text-gray-300 mb-4">
          Proporciona información clave sobre tu empresa para mejorar el análisis de llamadas:
        </p>
        <ul class="list-disc pl-5 text-gray-700 dark:text-gray-300 mb-4 space-y-1">
          <li>Productos/Servicios principales que ofreces</li>
          <li>Características de tu público objetivo</li>
          <li>Procesos comerciales relevantes</li>
          <li>Términos técnicos o específicos del sector</li>
        </ul>
      </div>

      <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-6 mx-4 md:mx-6 lg:mx-8" role="alert">
        <span class="block sm:inline">{{ errorMessage }}</span>
      </div>

      <div v-if="successMessage" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative mb-6 mx-4 md:mx-6 lg:mx-8" role="alert">
        <span class="block sm:inline">{{ successMessage }}</span>
      </div>

      <div class="flex flex-col lg:flex-row gap-6 mb-8 px-4 md:px-6 lg:px-8">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 w-full flex-1">
          <h2 class="text-xl font-semibold mb-4 dark:text-white">Tu Descripción del Negocio</h2>
          <textarea
            v-model="businessContent"
            class="w-full h-96 p-4 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white resize-none"
            placeholder="Ejemplo: Nombre de empresa, sector, productos principales, público objetivo, procesos comerciales..."
            :disabled="loading || (hasBusinessInfo && !isEditing)"
          ></textarea>
        </div>

        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 flex-1">
          <h2 class="text-xl font-semibold mb-4 dark:text-white">Ejemplo</h2>
          <pre class="bg-gray-100 dark:bg-gray-700 p-4 rounded-md text-sm text-gray-800 dark:text-gray-300 overflow-x-auto">
TechSolutions Inc. - Desarrollo de Software

Sector: Tecnología B2B

Productos principales:
- Software de gestión empresarial
- Soluciones de automatización
- Plataforma de análisis de datos

Clientes ideales:
- Empresas medianas (50-500 empleados)
- Sectores: manufactura, logística
- Departamentos: Operaciones, TI

Procesos clave:
1. Demostración del producto
2. Prueba gratuita de 30 días
3. Implementación guiada
4. Soporte continuo
          </pre>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import UserService from '../services/UserService';
import { userStore } from '../store/userStore';

const router = useRouter();

const businessContent = ref('');
const loading = ref(false);
const errorMessage = ref('');
const successMessage = ref('');
const isEditing = ref(false);

const hasBusinessInfo = computed(() => {
  return businessContent.value.trim().length > 0;
});

const enableEditing = () => {
  isEditing.value = true;
};

const fetchBusinessInfo = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const response = await UserService.getBusinessInfo();
    businessContent.value = response.business_summary || '';
    isEditing.value = !hasBusinessInfo.value;
    
  } catch (error: unknown) {
    console.error('Business info error:', error);
    
    if (error instanceof Error) {
      if (error.message.includes('401') || error.message.includes('token') || error.message.includes('unauthorized')) {
        errorMessage.value = 'Sesión expirada. Redirigiendo al login...';
        userStore.logout();
        setTimeout(() => router.push('/login'), 2000);
      } else {
        errorMessage.value = error.message || 'Error al cargar la información del negocio';
      }
    } else {
      errorMessage.value = 'Error al cargar la información del negocio';
    }
  } finally {
    loading.value = false;
  }
};

const saveBusiness = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    successMessage.value = '';
    
    if (!businessContent.value.trim()) {
      errorMessage.value = 'La descripción del negocio no puede estar vacía';
      return;
    }

    await UserService.saveBusinessInfo({
      business_summary: businessContent.value
    });
    
    successMessage.value = 'Información guardada correctamente';
    isEditing.value = false;
    
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
    
  } catch (error: unknown) {
    console.error('Save business error:', error);
    
    if (error instanceof Error) {
      if (error.message.includes('401') || error.message.includes('token') || error.message.includes('unauthorized')) {
        errorMessage.value = 'Sesión expirada. Redirigiendo al login...';
        userStore.logout();
        setTimeout(() => router.push('/login'), 2000);
      } else {
        errorMessage.value = error.message || 'Error al guardar la información';
      }
    } else {
      errorMessage.value = 'Error al guardar la información';
    }
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  if (!userStore.isAuthenticated) {
    router.push('/login');
  } else {
    fetchBusinessInfo();
  }
});
</script>