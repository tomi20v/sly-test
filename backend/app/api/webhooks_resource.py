from flask import request
from flask_restful import Resource

class WebhooksResource(Resource):
    def __init__(self, purchases_repository):
        self.purchases_repository = purchases_repository

    def post(self):
        data = request.get_json()
        if not data or 'notification_type' not in data:
            return {'error': 'Invalid payload'}, 400

        if data['notification_type'] != 'order_paid':
            return {'error': 'Unsupported notification type'}, 400

        if 'billing' not in data or 'transaction' not in data['billing'] or 'external_id' not in data['billing']['transaction'] or 'id' not in data['billing']['transaction']:
            return {'error': 'Missing transaction data'}, 400

        external_id = data['billing']['transaction']['external_id']
        xsolla_transaction_id = data['billing']['transaction']['id']

        try:
            purchase_id = int(external_id)
        except (ValueError, TypeError):
            return {'error': 'Invalid external_id'}, 400

        purchase = self.purchases_repository.get(purchase_id)
        if not purchase:
            return {'error': 'Purchase not found'}, 400

        self.purchases_repository.pay_purchase(purchase_id, xsolla_transaction_id)

        return {'status': 'success'}, 200
