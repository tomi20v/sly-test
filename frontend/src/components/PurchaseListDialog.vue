<template>
  <v-dialog v-model="showDialog" max-width="500px">
    <v-card class="pb-4">
      <close-button @click="closeDialog"></close-button>
      <v-card-title class="text-center text-h5" style="padding-top: 24px; padding-bottom: 16px;">
        <v-icon icon="mdi-credit-card"></v-icon>
        <span class="ml-2">My Purchases</span>
      </v-card-title>
      <v-card-text class="text-center">
        You have not purchased anything.... Yet?
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import CloseButton from './CloseButton.vue';

const props = defineProps<{
  modelValue: boolean;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
}>();

const showDialog = computed({
  get() {
    return props.modelValue;
  },
  set(value) {
    emit('update:modelValue', value);
  }
});

function closeDialog() {
  showDialog.value = false;
}
</script>
