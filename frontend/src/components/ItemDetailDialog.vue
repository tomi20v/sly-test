<template>
  <v-dialog v-model="showDialog" max-width="800px" :persistent="persistent">
    <v-card class="item-detail-card">
      <close-button @click="closeDialog"></close-button>
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
             <v-card-text v-if="purchaseState === PurchaseState.paid">
              <v-alert type="success" dense class="mb-4">
                Payment successful, enjoy your item
              </v-alert>
            </v-card-text>
            <v-card-actions class="pa-4">
              <v-btn
                v-if="purchaseState !== PurchaseState.payingretry && purchaseState !== PurchaseState.paid"
                class="buy-now-btn"
                block
                :disabled="isBuyNowDisabled"
                @click="buyNow"
              >
                <span v-if="purchaseState === PurchaseState.creatingPurchase">Processing...</span>
                <span v-else>Buy Now</span>
              </v-btn>
              <v-btn
                v-if="purchaseState === PurchaseState.paid"
                class="buy-now-btn"
                block
                @click="goToPurchases"
              >
                My Purchases
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
import CloseButton from './CloseButton.vue';
import { usePurchaseStore } from '../store/purchaseStore';

const enum PurchaseState {
  beforePurchase = 'beforePurchase',
  creatingPurchase = 'creatingPurchase',
  payingretry = 'payingretry',
  error = 'error',
  paid = 'paid',
}

const props = defineProps<{
  modelValue: boolean,
  item: ItemInterface | null
}>();

const emit = defineEmits(['update:modelValue', 'show-purchases']);

const purchaseState = ref<PurchaseState>(PurchaseState.beforePurchase);
const isBuyNowDisabled = ref(false);
const errorMessage = ref<string | null>(null);
const successMessage = ref<string | null>(null);
const persistent = ref(false);
const purchaseId = ref<string | null>(null);
let pollingInterval: any = null;

const purchaseStore = usePurchaseStore();

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

watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    purchaseState.value = PurchaseState.beforePurchase;
    errorMessage.value = null;
    successMessage.value = null;
    persistent.value = false;
    isBuyNowDisabled.value = false;
    if (pollingInterval) {
      clearInterval(pollingInterval);
    }
  }
});

async function buyNow() {
  if (!props.item) return;

  persistent.value = true;
  isBuyNowDisabled.value = true;
  purchaseState.value = PurchaseState.creatingPurchase;
  errorMessage.value = null;

  try {
    const responseData = await purchaseStore.createPurchase(props.item.id);
    purchaseId.value = responseData.id;
    purchaseState.value = PurchaseState.payingretry;
    startPolling();
    
  } catch (error: any) {
    errorMessage.value = 'Purchase failed, please try again in a bit';
    purchaseState.value = PurchaseState.error;
    persistent.value = false;
    isBuyNowDisabled.value = false;
  }
}

function startPolling() {
  pollingInterval = setInterval(async () => {
    if (!purchaseId.value) return;

    try {
      const data = await purchaseStore.fetchPurchase(purchaseId.value);
      if (data.payment_status === 'paid') {
        clearInterval(pollingInterval);
        purchaseState.value = PurchaseState.paid;
        persistent.value = false;
      } else if (data.payment_status === 'failed') {
        clearInterval(pollingInterval);
        errorMessage.value = 'Payment failed, please try again.';
        purchaseState.value = PurchaseState.error;
        persistent.value = false;
        setTimeout(() => {
          isBuyNowDisabled.value = false;
        }, 2000);
      }
    } catch (error) {
      clearInterval(pollingInterval);
      errorMessage.value = 'Error checking payment status.';
      purchaseState.value = PurchaseState.error;
      persistent.value = false;
      setTimeout(() => {
        isBuyNowDisabled.value = false;
      }, 2000);
    }
  }, 2000);
}

function closeDialog() {
  if (!persistent.value) {
    showDialog.value = false;
  }
}
function goToPurchases() {
  emit('show-purchases');
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
