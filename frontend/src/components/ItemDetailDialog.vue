<template>
  <v-dialog v-model="showDialog" max-width="800px">
    <v-card class="item-detail-card">
      <v-btn icon="mdi-close" class="close-button" @click="closeDialog"></v-btn>
      <v-container fluid class="pa-0">
        <v-row no-gutters style="height: 600px">
          <v-col cols="12" md="6">
            <v-img
              v-if="item"
              :src="`https://picsum.photos/400/600?random=${item.id}`"
              height="100%"
              cover
              class="rounded-l-lg"
            ></v-img>
          </v-col>
          <v-col cols="12" md="6" class="d-flex flex-column">
            <v-card-title v-if="item" class="text-h5 pt-4 text-wrap">{{ item.name }}</v-card-title>
            <v-card-subtitle v-if="item">
              <span class="price">€{{ getPriceEuros(item.price) }}<sup class="cents">{{ getPriceCents(item.price) }}</sup></span>
            </v-card-subtitle>
            <v-card-text class="description-container">
              <p v-if="item" class="body-1 mt-4">
                {{ item.description }}
              </p>
            </v-card-text>
            <v-card-actions class="pa-4">
              <v-btn
                class="buy-now-btn"
                block
                @click="buyNow"
              >Buy Now</v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { ItemInterface } from '../model/ItemInterface';

const props = defineProps<{
  modelValue: boolean,
  item: ItemInterface | null
}>();

const emit = defineEmits(['update:modelValue']);

const showDialog = computed({
  get() {
    return props.modelValue;
  },
  set(value) {
    emit('update:modelValue', value);
  }
});

const getPriceEuros = (price: number) => {
    if (typeof price !== 'number') return '0';
    return price.toFixed(2).split('.')[0];
};

const getPriceCents = (price: number) => {
    if (typeof price !== 'number') return '00';
    return price.toFixed(2).split('.')[1];
};

function closeDialog() {
  showDialog.value = false;
}

function buyNow() {
  // Placeholder for buy now functionality
  console.log('Buy now clicked for:', props.item);
  closeDialog();
}
</script>

<style scoped>
.item-detail-card {
  border-radius: 16px !important;
  overflow: hidden;
}

.description-container {
  flex-grow: 1;
  overflow-y: auto;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 20;
}

.rounded-l-lg {
  border-top-left-radius: 16px;
  border-bottom-left-radius: 16px;
}

.buy-now-btn {
  background-color: #1867c0 !important;
  color: white !important;
  height: 56px !important;
  font-size: 1.25rem !important;
}

.price {
  font-size: 1.5rem;
  line-height: 1;
}

.cents {
  font-size: 0.6em;
}
</style>
