<template>
  <Navbar />
  <router-view class="flex-grow main-content" />
  <Footer />
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>