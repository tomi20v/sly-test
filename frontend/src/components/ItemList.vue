      <template>
        <v-container>
          <v-row>
            <v-col>
              <h2 class="text-h4 text-center my-4">Our Wares</h2>
            </v-col>
          </v-row>
          <v-progress-linear v-if="store.itemsLoading" indeterminate></v-progress-linear>
          <v-row v-else>
           <v-col v-for="item in store.items" :key="item.id" cols="12" sm="6" md="4" lg="3">
             <v-card class="rounded-lg item-card" @click="openDialog(item)">
                <div class="image-container">
                  <v-img
                    :src="`https://picsum.photos/400/600?random=${item.id}`"
                    height="200px"
                    cover
                  ></v-img>
                  <div class="price-tag">
                    <span class="price">€{{ getPriceEuros(item.price) }}<sup class="cents">{{ getPriceCents(item.price) }}</sup></span>
                  </div>
                  <div class="details-overlay">
                    <v-btn class="details-button">More Details</v-btn>
                  </div>
                </div>
                <v-card-title>
                  <span class="text-truncate">{{ item.name }}</span>
                </v-card-title>
             </v-card>
           </v-col>
         </v-row>
         <item-detail-dialog v-model="dialog" :item="selectedItem" @show-purchases="$emit('show-purchases')"></item-detail-dialog>
       </v-container>
     </template>
     
     <script setup lang="ts">
     import { onMounted, ref } from 'vue';
     import { useItemStore } from '../store/itemStore';
     import ItemDetailDialog from './ItemDetailDialog.vue';
     import type { ItemInterface } from '../model/ItemInterface';

     const store = useItemStore();

     const dialog = ref(false);
     const selectedItem = ref<ItemInterface | null>(null);

      const openDialog = (item: ItemInterface) => {
        selectedItem.value = item;
        dialog.value = true;
      };

    defineEmits(['show-purchases']);


    const getPriceEuros = (price: number) => {
        if (typeof price !== 'number') return '0';
        return price.toFixed(2).split('.')[0];
    };

    const getPriceCents = (price: number) => {
        if (typeof price !== 'number') return '00';
        return price.toFixed(2).split('.')[1];
    };

     onMounted(() => {
       store.fetchItems();
     });
     </script>

    <style scoped>
    .cents {
      font-size: 0.6em;
    }

    .image-container {
      position: relative;
    }

    .price-tag {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      background-color: rgba(0, 0, 0, 0.7);
      color: white;
      padding: 0.375rem 0.75rem;
      border-radius: 0.75rem;
      font-size: 1.5rem;
      line-height: 1;
    }

    .details-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .item-card {
      transition: transform 0.2s ease-in-out;
      cursor: pointer;
    }

    .item-card:hover {
      transform: scale(1.05);
      z-index: 10;
    }

    .item-card:hover .details-overlay {
      opacity: 1;
    }
    </style>
