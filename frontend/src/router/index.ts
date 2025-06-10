import { createRouter, createWebHistory } from 'vue-router'
import UploadFileView from '../views/UploadFileView.vue'
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import RubricaView from '../views/RubricaView.vue';
import BusinessView from '../views/BusinessView.vue';
import { userStore } from '../store/userStore'
import UsersView from '../views/UsersView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/upload_file',
      name: 'upload_file',
      component: UploadFileView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: { requiresAuth: false }
    },
    {
      path: '/admin/create_user',
      name: 'create_user',
      component: RegisterView,
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/users',
      name: 'users',
      component: UsersView,
      meta: { requiresAuth: true }
    },
    {
      path: '/rubrica',
      name: 'rubrica',
      component: RubricaView,
      meta: { requiresAuth: true }
    },
    {
      path: '/business',
      name: 'business',
      component: BusinessView,
      meta: { requiresAuth: true }
    }
  ]
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = userStore.isAuthenticated;

  if(to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  }else if((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    next('/');
  }else {
    next();
  }
})

export default router;