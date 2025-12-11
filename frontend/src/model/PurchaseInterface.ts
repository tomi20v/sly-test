export interface PurchaseInterface {
  id: string;
  item_id: number;
  created_at: string;
  payment_status: 'pending' | 'failed' | 'paid';
}
