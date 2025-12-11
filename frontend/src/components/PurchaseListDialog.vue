<template>
  <v-dialog v-model="showDialog" max-width="500px">
    <v-card class="pb-4">
      <close-button @click="closeDialog"></close-button>
      <v-card-title class="text-center text-h5" style="padding-top: 24px; padding-bottom: 16px;">
        <v-icon icon="mdi-credit-card"></v-icon>
        <span class="ml-2">My Purchases</span>
      </v-card-title>
      <v-card-text>
        <v-progress-linear
          v-if="state === 'loading'"
          indeterminate
          color="primary"
          class="mb-4"
        ></v-progress-linear>

        <v-alert v-else-if="state === 'error'" type="error" dense class="mb-4">
          {{ errorMessage }}
        </v-alert>

        <div v-else-if="state === 'empty'" class="text-center">
          You have not purchased anything.... Yet?
        </div>

        <v-list v-else-if="state === 'loaded'" lines="one" dense>
          <v-list-item
            v-for="purchase in purchases"
            :key="purchase.id"
            :title="`Purchase ID: ${purchase.id}`"
            :subtitle="`Time: ${new Date(purchase.created_at).toLocaleString()} ${purchase.payment_status.toUpperCase()}`"
          >
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import CloseButton from './CloseButton.vue';

interface Purchase {
  id: string;
  created_at: string;
  payment_status: 'pending' | 'failed' | 'paid';
}

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

const purchases = ref<Purchase[]>([]);
const state = ref('loading'); // loading | error | empty | loaded
const errorMessage = ref('');

async function fetchPurchases() {
  state.value = 'loading';
  try {
    // Assuming user_id=1 for now.
    const response = await fetch('/api/users/2/purchases');
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || 'Failed to fetch purchases');
    }
    
    if (data.length === 0) {
      state.value = 'empty';
    } else {
      purchases.value = data;
      state.value = 'loaded';
    }
  } catch (error: any) {
    errorMessage.value = error.message;
    state.value = 'error';
  }
}

watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    fetchPurchases();
  }
});

function closeDialog() {
  showDialog.value = false;
}
</script>
