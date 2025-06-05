<template>
  <main class="flex-grow w-full py-8 px-4 md:px-6 lg:px-8">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Rúbrica de Evaluación</h1>
        <button 
          @click="saveRubrica"
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
          v-model="rubricaContent"
          class="w-full h-96 p-4 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="Escribe aquí tu rúbrica de evaluación..."
        ></textarea>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
        <h2 class="text-xl font-semibold mb-4 dark:text-white">Ejemplo de Estructura</h2>
        <pre class="bg-gray-100 dark:bg-gray-700 p-4 rounded-md text-sm text-gray-800 dark:text-gray-300 overflow-x-auto">
# Rúbrica de Evaluación de Llamadas

## 1. Presentación (20%)
- Saludo profesional
- Identificación clara
- Objetivo de la llamada

## 2. Detección de Necesidades (30%)
- Preguntas abiertas
- Escucha activa
- Confirmación de entendimiento

## 3. Argumentación (30%)
- Beneficios claros
- Objeciones manejadas
- Adaptación al cliente

## 4. Cierre (20%)
- Resumen de beneficios
- Llamada a la acción
- Despedida adecuada
        </pre>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuth } from '../services/AuthService';

const { user, refreshUser, error: authError, api } = useAuth(); // Añade api aquí
const rubricaContent = ref('');
const loading = ref(false);
const error = ref('');

const fetchRubrica = async () => {
  try {
    const response = await api.get('/auth/me'); // Usa api en lugar de axios
    if (response.data && response.data.evaluation_rubric) {
      rubricaContent.value = response.data.evaluation_rubric;
    } else {
      rubricaContent.value = '';
    }
  } catch (err) {
    console.error('Error fetching rubrica:', err);
    error.value = 'No se pudo cargar la rúbrica. Por favor, recarga la página.';
  }
};

const saveRubrica = async () => {
  try {
    loading.value = true;
    error.value = '';
    
    const response = await api.patch('/auth/me', { 
      evaluation_rubric: rubricaContent.value 
    }, {
      validateStatus: (status) => status < 500
    });

    if (response.status === 200) {
      await refreshUser();
    } else {
      error.value = response.data?.detail || 'Error al guardar los cambios';
    }
  } catch (err) {
    console.error('Error saving rubrica:', err);
    error.value = 'Error de conexión. Verifica tu red e intenta nuevamente.';
  } finally {
    loading.value = false;
  }
};

onMounted(async () => {
  await fetchRubrica();
});
</script>