import { defineStore } from 'pinia'
import type { ItemInterface } from '../../model/ItemInterface';
import axios from 'axios';

export const useItemStore = defineStore('items', {
  state: () => ({
    count: 0,
    items: [] as ItemInterface[],
    itemsLoading: false,
  }),
  actions: {
    increment() {
      this.count++
    },
    async fetchItems() {
      this.itemsLoading = true;
      try {
        const response = await axios.get(`/api/items`);
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      } finally {
        this.itemsLoading = false;
      }
    },
  },
})
