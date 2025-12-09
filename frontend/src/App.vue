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
            <v-list-item-title>Placeholder</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <HelloWorld msg="+ Vite"/>
      <v-btn @click="store.fetchItems()">Fetch Items</v-btn>
      <v-list>
        <v-list-item v-for="item in store.items" :key="item.id">
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
  import HelloWorld from './components/HelloWorld.vue'
  import { useAppStore } from './store/app';
  const store = useAppStore();
</script>
