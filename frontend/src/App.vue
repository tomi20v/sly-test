<template>
  <v-app>
    <v-app-bar color="red" density="compact">
      <v-app-bar-nav-icon icon="mdi-sword-cross"></v-app-bar-nav-icon>
      <v-app-bar-title class="text-left">Digital Game Item Store</v-app-bar-title>
      <v-spacer/>
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-app-bar-nav-icon v-bind="props" />
        </template>
        <v-list>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon icon="mdi-account"></v-icon>
            </template>
            <v-list-item-title>test2@example.com</v-list-item-title>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item @click="showPurchaseList = true">
            <template v-slot:prepend>
              <v-icon icon="mdi-credit-card"></v-icon>
            </template>
            <v-list-item-title>My Purchases</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <ItemList />
    </v-main>
    <PurchaseListDialog v-model="showPurchaseList" />
  </v-app>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import ItemList from './components/ItemList.vue';
  import PurchaseListDialog from './components/PurchaseListDialog.vue';

  const showPurchaseList = ref(false);
</script>
