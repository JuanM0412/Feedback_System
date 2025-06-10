<template>
  <main class="flex-grow w-full">
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-600 to-blue-800 text-white w-full min-h-[70vh] flex items-center justify-center">
      <div class="w-full px-4 md:px-6 lg:px-8 text-center pb-6 pt-20">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">
          Automatización de Análisis de Llamadas de Ventas
        </h1>
        <p class="text-xl md:text-2xl mb-6 max-w-3xl mx-auto">
          Solución integral para transcribir, analizar y mejorar el desempeño de tus agentes de ventas
        </p>
        <template v-if="isAuthenticated">
          <template v-if="!isAdmin">
            <router-link
              to="/upload_file"
              class="bg-gradient-to-r from-blue-600 to-blue-800 text-white hover:from-blue-700 hover:to-blue-900 font-medium rounded-lg px-6 py-3 text-lg border-2 border-white transition-colors"
            >
              Analizar Llamada
            </router-link>
          </template>
        </template>
        <template v-else>
          <div class="flex justify-center gap-4 mt-6">
            <router-link to='/login' class="bg-gradient-to-r from-blue-600 to-blue-800 text-white hover:from-blue-700 hover:to-blue-900 font-medium rounded-lg px-6 py-3 text-lg border-2 border-white transition-colors">
              Iniciar Sesión
            </router-link>
          </div>
        </template>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-16 bg-gray-50 dark:bg-gray-800 w-full">
      <div class="w-full px-4 md:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center mb-12 dark:text-white">Funcionalidades Clave</h2>
          
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white text-center">Análisis Automático</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Detección automática de nuevos audios, transcripción con AssemblyAI y análisis semántico con GPT-4o.
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white  text-center">Simulaciones Personalizadas</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Generación de escenarios basados en errores detectados y conversión a audios realistas con ElevenLabs.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white text-center">Reportes Automáticos</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Creación automática de reportes en Google Sheets o Airtable con trazabilidad completa por agente y fecha.
            </p>
          </div>

          <!-- Feature 4 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white text-center">Seguridad Garantizada</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Protección de API Keys mediante proxy o cifrado, con control de costos y alertas de consumo.
            </p>
          </div>

          <!-- Feature 5 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white text-center">Entrega Rápida</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Tiempo de entrega de análisis + simulación menor a 15 minutos desde la carga del audio.
            </p>
          </div>

          <!-- Feature 6 -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
            <div class="text-blue-600 dark:text-blue-400 mb-4 flex justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2-2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-3 dark:text-white text-center">Mejora Continua</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Incremento de métricas de ventas en al menos un 20% en 60 días mediante práctica dirigida.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-10 w-full">
      <div class="w-full px-4 md:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center mb-12 dark:text-white">Cómo Funciona</h2>
          
        <div class="w-full mx-auto max-w-4xl">
          <!-- Paso 1 -->
          <div class="flex flex-col md:flex-row gap-6 mb-8 items-start">
            <div class="flex-shrink-0 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full h-16 w-16 flex items-center justify-center text-2xl font-bold">
              1
            </div>
            <div class="flex-grow">
              <h3 class="text-xl font-semibold mb-3 dark:text-white">Detección de Audios</h3>
              <p class="text-gray-600 dark:text-gray-300">
                El sistema detecta automáticamente nuevos audios cargados en Google Drive, listos para ser procesados.
              </p>
            </div>
          </div>

          <!-- Paso 2 -->
          <div class="flex flex-col md:flex-row gap-6 mb-8 items-start">
            <div class="flex-shrink-0 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full h-16 w-16 flex items-center justify-center text-2xl font-bold">
              2
            </div>
            <div class="flex-grow">
              <h3 class="text-xl font-semibold mb-3 dark:text-white">Transcripción y Análisis</h3>
              <p class="text-gray-600 dark:text-gray-300">
                AssemblyAI transcribe el audio y GPT-4o realiza un análisis semántico profesional, evaluando estructura de ventas y detectando áreas de mejora.
              </p>
            </div>
          </div>

          <!-- Paso 3 -->
          <div class="flex flex-col md:flex-row gap-6 mb-8 items-start">
            <div class="flex-shrink-0 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full h-16 w-16 flex items-center justify-center text-2xl font-bold">
              3
            </div>
            <div class="flex-grow">
              <h3 class="text-xl font-semibold mb-3 dark:text-white">Generación de Simulaciones</h3>
              <p class="text-gray-600 dark:text-gray-300">
                Basado en los errores detectados, el sistema crea escenarios personalizados de práctica y los convierte en audios realistas usando ElevenLabs.
              </p>
            </div>
          </div>

          <!-- Paso 4 -->
          <div class="flex flex-col md:flex-row gap-6 items-start">
            <div class="flex-shrink-0 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full h-16 w-16 flex items-center justify-center text-2xl font-bold">
              4
            </div>
            <div class="flex-grow">
              <h3 class="text-xl font-semibold mb-3 dark:text-white">Entrega y Seguimiento</h3>
              <p class="text-gray-600 dark:text-gray-300">
                Las simulaciones se envían automáticamente a los agentes y los resultados se registran para generar reportes de desempeño.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-blue-700 text-white pt-14 pb-10 w-full">
      <div class="w-full px-4 md:px-6 lg:px-6 text-center">
        <h2 class="text-3xl font-bold mb-6">¿Listo para transformar tu equipo de ventas?</h2>
        <p class="text-xl mb-8 w-full mx-auto">
          Comienza a mejorar el desempeño de tus agentes con nuestra solución automatizada.
        </p>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { userStore } from '../store/userStore';

const isAuthenticated = computed(() => userStore.isAuthenticated);
const isAdmin = computed(() => userStore.type === true);
</script>