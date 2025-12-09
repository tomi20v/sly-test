import { defineStore } from 'pinia'
import type { ItemInterface } from '../../model/ItemInterface';
import axios from 'axios';

export const useAppStore = defineStore('app', {
  state: () => ({
    count: 0,
    items: [] as ItemInterface[],
  }),
  actions: {
    increment() {
      this.count++
    },
    async fetchItems() {
      try {
        const response = await axios.get(`/api/items`);
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    },
  },
})
