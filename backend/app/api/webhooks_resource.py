from flask import request
from flask_restful import Resource

class ValidationError(Exception):
    pass

class WebhooksResource(Resource):
    def __init__(self, purchases_repository, webhook_logs_repository):
        self.purchases_repository = purchases_repository
        self.webhook_logs_repository = webhook_logs_repository

    def post(self):
        try:
            data = request.get_json()
            self.webhook_logs_repository.create(data)
            
            if not data or 'notification_type' not in data:
                raise ValidationError('Invalid payload')

            if data['notification_type'] != 'order_paid':
                raise ValidationError('Unsupported notification type')

            if 'billing' not in data or 'transaction' not in data['billing'] or 'external_id' not in data['billing']['transaction'] or 'id' not in data['billing']['transaction']:
                raise ValidationError('Missing transaction data')

            external_id = data['billing']['transaction']['external_id']
            xsolla_transaction_id = data['billing']['transaction']['id']

            try:
                purchase_id = int(external_id)
            except (ValueError, TypeError):
                raise ValidationError('Invalid external_id')

            purchase = self.purchases_repository.get(purchase_id)
            if not purchase:
                raise ValidationError('Purchase not found')

            self.purchases_repository.pay_purchase(purchase_id, xsolla_transaction_id)

            return {'status': 'success'}, 200
        except ValidationError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'Internal Server Error'}, 500
