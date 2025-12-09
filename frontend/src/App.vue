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
      <ItemList />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
  import ItemList from './components/ItemList.vue';
</script>
