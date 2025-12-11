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
          v-if="purchaseStore.purchasesLoading || itemStore.itemsLoading"
          indeterminate
          color="primary"
          class="mb-4"
        ></v-progress-linear>

        <v-alert v-else-if="purchaseStore.purchasesError" type="error" dense class="mb-4">
          {{ purchaseStore.purchasesError }}
        </v-alert>

        <div v-else-if="purchaseStore.purchases.length === 0" class="text-center">
          You have not purchased anything.... Yet?
        </div>

        <v-list v-else lines="one" dense>
          <v-list-item
            v-for="purchase in purchaseStore.purchases"
            :key="purchase.id"
            :title="getItemName(purchase.item_id)"
            :subtitle="`Time: ${new Date(purchase.created_at).toLocaleString()} ${purchase.payment_status.toUpperCase()}`"
          >
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, watch } from 'vue';
import CloseButton from './CloseButton.vue';
import { useItemStore } from '../store/itemStore';
import { usePurchaseStore } from '../store/purchaseStore';

const props = defineProps<{
  modelValue: boolean;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
}>();

const itemStore = useItemStore();
const purchaseStore = usePurchaseStore();

const showDialog = computed({
  get() {
    return props.modelValue;
  },
  set(value) {
    emit('update:modelValue', value);
  }
});

watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    purchaseStore.fetchPurchases();
    itemStore.fetchItems();
  }
});

function getItemName(itemId: number) {
  const item = itemStore.items.find(i => i.id === itemId);
  return item ? item.name : 'Unknown Item';
}

function closeDialog() {
  showDialog.value = false;
}
</script>
