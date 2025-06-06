import api from './ApiBase'

export default class UploadService {
  async uploadFile(file: File, onUploadProgress?: (progressEvent: import('axios').AxiosProgressEvent) => void): Promise<{
    data?: any
    error?: string
  }> {
    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await api.post<any>('/analysis/upload_audio', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        onUploadProgress
      })

      return { data: response.data }
    } catch (error: any) {
      return {
        error: api.isAxiosError?.(error)
          ? (error.response?.data && typeof error.response.data === 'object' && 'detail' in error.response.data
              ? (error.response.data as { detail?: string }).detail || 'Error al subir el archivo'
              : 'Error al subir el archivo')
          : 'Error desconocido al subir el archivo'
      }
    }
  }
}
