<template>
  <Navbar />
  <router-view class="flex-grow" />
  <Footer />
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>