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
             <v-card class="rounded-lg">
                <div class="image-container">
                  <v-img
                    :src="`https://picsum.photos/200/300?random=${item.id}`"
                    height="200px"
                    cover
                  ></v-img>
                  <div class="price-tag">
                    <span class="price">€{{ getPriceEuros(item.price) }}<sup class="cents">{{ getPriceCents(item.price) }}</sup></span>
                  </div>
                </div>
                <v-card-title>
                  <span class="text-truncate">{{ item.name }}</span>
                </v-card-title>
             </v-card>
           </v-col>
         </v-row>
       </v-container>
     </template>
     
     <script setup lang="ts">
     import { onMounted } from 'vue';
     import { useItemStore } from '../store/itemStore';
     const store = useItemStore();

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
    </style>
