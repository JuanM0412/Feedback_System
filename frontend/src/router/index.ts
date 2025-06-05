import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomeView.vue'
import UploadFileView from '../views/UploadFileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/upload_file',
      name: 'upload_file',
      component: UploadFileView
    }
  ]
})

export default router