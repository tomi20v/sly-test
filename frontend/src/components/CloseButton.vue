<template>
  <v-btn icon="mdi-close" class="close-button" @click="$emit('click')"></v-btn>
</template>

<script setup lang="ts">
defineEmits(['click']);
</script>

<style scoped>
.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 20;
}
</style>