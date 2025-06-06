<template>
  <div class="min-h-[calc(100vh-160px)] flex items-center justify-center bg-white dark:bg-[#0d1117] px-4 py-8">
    <div
      class="w-full max-w-3xl border-2 border-dashed border-blue-400 rounded-2xl bg-gray-100 dark:bg-[#1c1f26] p-10 text-center transition hover:shadow-lg"
      @dragover.prevent
      @drop.prevent="handleDrop"
    >
      <label for="file-upload" class="block cursor-pointer text-lg font-semibold text-blue-600 dark:text-blue-400 hover:underline">
        Haz clic para subir
      </label>
      <input
        id="file-upload"
        type="file"
        class="hidden"
        accept=".mp3,.wav"
        @change="handleFileSelect"
      />
      <p class="mt-2 text-sm text-gray-700 dark:text-gray-400">o arrastra y suelta tu archivo de audio aquí</p>
      <p class="mt-1 text-xs text-gray-500 dark:text-gray-500">Formatos permitidos: MP3, WAV, etc.</p>

      <div v-if="selectedFile" class="mt-6">
        <p class="font-medium text-gray-800 dark:text-white">Archivo seleccionado:</p>
        <p class="text-blue-700 dark:text-blue-300">{{ selectedFile.name }}</p>

        <button
          @click="uploadFile"
          class="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow transition"
          :disabled="isUploading"
        >
          {{ isUploading ? 'Subiendo...' : 'Subir Archivo' }}
        </button>

        <div v-if="isUploading" class="mt-6 w-full">
          <div class="relative w-full bg-gray-300 dark:bg-gray-700 rounded-full h-6 overflow-hidden">
            <div
              class="absolute top-0 left-0 h-6 bg-blue-600 text-white text-sm font-medium text-center leading-6 transition-all duration-300 ease-in-out"
              :style="{ width: uploadProgress + '%' }"
            >
              {{ uploadProgress.toFixed(0) }}%
            </div>
          </div>
        </div>

        <p v-if="uploadSuccess" class="mt-4 text-green-600 dark:text-green-400 font-medium">¡Archivo subido correctamente!</p>
        <p v-if="uploadError" class="mt-4 text-red-600 dark:text-red-400 font-medium">Error: {{ uploadError }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import UploadService from '../services/AnalysisService'

const selectedFile = ref<File | null>(null)
const isUploading = ref(false)
const uploadProgress = ref(0)
const uploadSuccess = ref(false)
const uploadError = ref('')

function handleFileSelect(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0]
    resetStatus()
  }
}

function handleDrop(event: DragEvent) {
  if (event.dataTransfer?.files.length) {
    selectedFile.value = event.dataTransfer.files[0]
    resetStatus()
  }
}

function resetStatus() {
  uploadProgress.value = 0
  uploadSuccess.value = false
  uploadError.value = ''
}

async function uploadFile() {
  if (!selectedFile.value) return

  isUploading.value = true
  uploadSuccess.value = false
  uploadError.value = ''
  uploadProgress.value = 0

  const service = new UploadService()
  const { data, error } = await service.uploadFile(selectedFile.value, (progressEvent) => {
    if (progressEvent.total) {
      uploadProgress.value = (progressEvent.loaded / progressEvent.total) * 100
    }
  })

  isUploading.value = false

  if (error) {
    uploadError.value = error
  } else {
    uploadSuccess.value = true
    console.log('Respuesta del servidor:', data)
  }
}
</script>
