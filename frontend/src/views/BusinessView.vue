<template>
  <main class="flex-grow w-full py-8 px-4 md:px-6 lg:px-8">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Descripción del Negocio</h1>
        <button 
          @click="saveBusiness"
          class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md"
          :disabled="loading"
        >
          <span v-if="!loading">Guardar Cambios</span>
          <span v-else class="flex items-center">
            <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Guardando...
          </span>
        </button>
      </div>

      <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
        {{ error }}
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-8">
        <textarea
          v-model="businessContent"
          class="w-full h-96 p-4 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="Describe tu negocio, productos/servicios principales, y público objetivo..."
        ></textarea>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
        <h2 class="text-xl font-semibold mb-4 dark:text-white">Ejemplo de Estructura</h2>
        <pre class="bg-gray-100 dark:bg-gray-700 p-4 rounded-md text-sm text-gray-800 dark:text-gray-300 overflow-x-auto">
# Descripción del Negocio

**Nombre de la Empresa:** TechSolutions Inc.

**Industria:** Desarrollo de Software B2B

**Productos/Servicios Principales:**
- Desarrollo de aplicaciones empresariales personalizadas
- Soluciones de automatización de procesos
- Consultoría en transformación digital

**Público Objetivo:**
- Medianas empresas (50-500 empleados)
- Sectores: manufactura, logística, retail
- Departamentos de TI y operaciones

**Valor Diferenciador:**
- Enfoque en integración con sistemas legacy
- Tiempos de implementación rápidos
- Soporte técnico 24/7 incluido
        </pre>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuth } from '../services/AuthService';
import { useRouter } from 'vue-router';

const router = useRouter();
const { api, user, logout } = useAuth();
const businessInfo = ref('');
const loading = ref(false);
const error = ref('');

const fetchBusinessInfo = async () => {
  try {
    loading.value = true;
    error.value = '';
    
    // Verificación adicional del token
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error('No token found');
    
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp * 1000 < Date.now()) {
      throw new Error('Token expired');
    }

    const response = await api.get('/business/info');
    businessInfo.value = response.data?.business_summary || '';
    
  } catch (err) {
    console.error('Business info error:', err);
    
    if (err.response?.status === 401 || err.message.includes('token')) {
      error.value = 'Session expired. Redirecting to login...';
      logout();
      router.push('/login');
    } else {
      error.value = err.response?.data?.detail || 
                  'Failed to load business information';
    }
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  // Verifica si el usuario está autenticado primero
  if (!user.value) {
    router.push('/login');
  } else {
    fetchBusinessInfo();
  }
});
</script>