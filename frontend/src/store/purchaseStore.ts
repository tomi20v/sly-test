import { defineStore } from 'pinia';
import { type PurchaseInterface } from '../model/PurchaseInterface';

export const usePurchaseStore = defineStore('purchases', {
  state: () => ({
    purchases: [] as PurchaseInterface[],
    purchasesLoading: false,
    purchasesError: '',
  }),
  actions: {
    async createPurchase(itemId: number) {
      const response = await fetch('/api/purchases', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          item_id: itemId,
        }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Failed to create purchase');
      }
      return data;
    },
    async fetchPurchases() {
      this.purchasesLoading = true;
      this.purchasesError = '';
      try {
        // Assuming user_id=2 for now.
        const response = await fetch('/api/users/2/purchases');
        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.error || 'Failed to fetch purchases');
        }

        this.purchases = data;
      } catch (error: any) {
        this.purchasesError = error.message;
      } finally {
        this.purchasesLoading = false;
      }
    },
    async fetchPurchase(purchaseId: string) {
      const response = await fetch(`/api/purchases/${purchaseId}`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to fetch purchase');
      }
      return data;
    }
  },
});
