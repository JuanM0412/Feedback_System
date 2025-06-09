<template>
  <main class="flex-grow w-full py-8 px-4 md:px-6 lg:px-8 mt-16">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Rúbrica de Evaluación</h1>
        <div class="flex gap-2">
          <button 
            v-if="hasRubrica && !isEditing"
            @click="enableEditing"
            class="bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
          >
            Editar Rúbrica
          </button>
          <button 
            @click="saveRubrica"
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            :disabled="loading || (hasRubrica && !isEditing)"
          >
            <span v-if="!loading">Guardar Cambios</span>
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

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-6">
        <h2 class="text-xl font-semibold mb-2 dark:text-white">¿Qué es una Rúbrica de Evaluación?</h2>
        <p class="text-gray-700 dark:text-gray-300 mb-4">
          Una rúbrica de evaluación es una guía estructurada que define los criterios para analizar las llamadas telefónicas. 
          La rúbrica es fundamental para:
        </p>
        <ul class="list-disc pl-5 text-gray-700 dark:text-gray-300 mb-4 space-y-1">
          <li>Proporcionar contexto específico al modelo de lenguaje</li>
          <li>Mejorar la precisión y relevancia del análisis</li>
          <li>Establecer estándares consistentes para evaluar las interacciones</li>
          <li>Enfocar el análisis en los aspectos más importantes para tu negocio</li>
        </ul>
        <p class="text-gray-700 dark:text-gray-300">
          Cuanto más detallada y clara sea tu rúbrica, mejores resultados obtendrás del análisis automático.
        </p>
      </div>

      <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-6" role="alert">
        <span class="block sm:inline">{{ errorMessage }}</span>
      </div>

      <div v-if="successMessage" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative mb-6" role="alert">
        <span class="block sm:inline">{{ successMessage }}</span>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-8">
        <textarea
          v-model="rubricaContent"
          class="w-full h-96 p-4 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white resize-none"
          placeholder="Escribe aquí tu rúbrica de evaluación..."
          :disabled="loading || (hasRubrica && !isEditing)"
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
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import UserService from '../services/UserService';
import { userStore } from '../store/userStore';

const router = useRouter();

const rubricaContent = ref('');
const loading = ref(false);
const errorMessage = ref('');
const successMessage = ref('');
const isEditing = ref(false);

const hasRubrica = computed(() => {
  return rubricaContent.value.trim().length > 0;
});

const enableEditing = () => {
  isEditing.value = true;
};

const fetchRubrica = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const response = await UserService.getRubrica();
    rubricaContent.value = response.evaluation_rubric || '';
    isEditing.value = !hasRubrica.value;
    
  } catch (error: unknown) {
    console.error('Rubrica fetch error:', error);
    
    if (error instanceof Error) {
      if (error.message.includes('401') || error.message.includes('token') || error.message.includes('unauthorized')) {
        errorMessage.value = 'Sesión expirada. Redirigiendo al login...';
        userStore.logout();
        setTimeout(() => router.push('/login'), 2000);
      } else {
        errorMessage.value = error.message || 'Error al cargar la rúbrica';
      }
    } else {
      errorMessage.value = 'Error al cargar la rúbrica';
    }
  } finally {
    loading.value = false;
  }
};

const saveRubrica = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    successMessage.value = '';
    
    if (!rubricaContent.value.trim()) {
      errorMessage.value = 'La rúbrica de evaluación no puede estar vacía';
      return;
    }

    await UserService.saveRubrica({
      evaluation_rubric: rubricaContent.value
    });
    
    successMessage.value = 'Rúbrica de evaluación guardada exitosamente';
    isEditing.value = false;
    
    // Limpiar el mensaje de éxito después de 3 segundos
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
    
  } catch (error: unknown) {
    console.error('Save rubrica error:', error);
    
    if (error instanceof Error) {
      if (error.message.includes('401') || error.message.includes('token') || error.message.includes('unauthorized')) {
        errorMessage.value = 'Sesión expirada. Redirigiendo al login...';
        userStore.logout();
        setTimeout(() => router.push('/login'), 2000);
      } else {
        errorMessage.value = error.message || 'Error al guardar la rúbrica';
      }
    } else {
      errorMessage.value = 'Error al guardar la rúbrica';
    }
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  // Verificar si el usuario está autenticado
  if (!userStore.isAuthenticated) {
    router.push('/login');
  } else {
    fetchRubrica();
  }
});
</script>