<template>
  <v-dialog v-model="showDialog" max-width="800px" :persistent="persistent">
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
              <span class="price">€{{ priceEuros }}<sup class="cents">{{ priceCents }}</sup></span>
            </v-card-subtitle>
            <v-card-text class="description-container">
              <p v-if="item" class="body-1 mt-4">
                {{ item.description }}
              </p>
            </v-card-text>
            <v-card-text v-if="purchaseState === PurchaseState.error" >
              <v-alert type="error" dense class="mb-4">
                  {{ errorMessage }}
              </v-alert>
            </v-card-text>
            <v-card-actions class="pa-4">
              <v-btn
                v-if="purchaseState !== PurchaseState.payingretry"
                class="buy-now-btn"
                block
                :disabled="purchaseState !== PurchaseState.beforePurchase"
                @click="buyNow"
              >
                <span v-if="purchaseState === PurchaseState.creatingPurchase">Processing...</span>
                <span v-else>Buy Now</span>
              </v-btn>
              <v-progress-linear
                v-if="purchaseState === PurchaseState.payingretry"
                indeterminate
                color="primary"
                class="mb-4"
              ></v-progress-linear>
            </v-card-actions>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import type { ItemInterface } from '../model/ItemInterface';

const enum PurchaseState {
  beforePurchase = 'beforePurchase',
  creatingPurchase = 'creatingPurchase',
  payingretry = 'payingretry',
  error = 'error',
}

const props = defineProps<{
  modelValue: boolean,
  item: ItemInterface | null
}>();

const emit = defineEmits(['update:modelValue']);

const purchaseState = ref<PurchaseState>(PurchaseState.beforePurchase);
const errorMessage = ref<string | null>(null);
const persistent = ref(false);

const priceEuros = computed(() => {
    if (props.item && typeof props.item.price === 'number') {
        return props.item.price.toFixed(2).split('.')[0];
    }
    return '0';
});

const priceCents = computed(() => {
    if (props.item && typeof props.item.price === 'number') {
        return props.item.price.toFixed(2).split('.')[1];
    }
    return '00';
});

const showDialog = computed({
  get() {
    return props.modelValue;
  },
  set(value) {
    emit('update:modelValue', value);
  }
});

// we need this so that the outclick is handled properly.
watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    // initialize state when opening dialog
    purchaseState.value = PurchaseState.beforePurchase;
    errorMessage.value = null;
    persistent.value = false;
  }
});

async function buyNow() {
  if (!props.item) return;

  persistent.value = true;
  purchaseState.value = PurchaseState.creatingPurchase;
  errorMessage.value = null;

  try {
    const response = await fetch('/api/purchases', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        item_id: props.item.id,
        email: "test2@example.com", // Hardcoded user ID, replace with actual user ID
      }),
    });
    const responseData = await response.json();
    console.log("response body", responseData);
    if (!response.ok) {
      throw new Error();
    }

    purchaseState.value = PurchaseState.payingretry;
    
  } catch (error: any) {
    errorMessage.value = 'Purchase failed, please try again in a bit';
    purchaseState.value = PurchaseState.error;
    persistent.value = false;

    // Re-enable the button after a delay
   setTimeout(() => {
       purchaseState.value = PurchaseState.beforePurchase;
   }, 5000);
  }
}

// the button closes the dialog only when not persistent
function closeDialog() {
  if (!persistent.value) {
    showDialog.value = false;
  }
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