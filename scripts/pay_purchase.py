#!/usr/bin/env python3
import sys
import json
import requests
import hashlib
import os

if len(sys.argv) < 2:
    print("Usage: python scripts/pay_purchase.py <payment_id>")
    sys.exit(1)

payment_id = sys.argv[1]

secret = os.environ.get('XSOLLA_HMAC_SECRET', 'verySecret')

url = "http://localhost:5000/api/webhooks/payment"

data = {
    "notification_type": "order_paid",
    "items": [
      {
        "sku": "com.xsolla.item_1",
        "type": "virtual_good",
        "is_pre_order": False,
        "quantity": 3,
        "amount": "1000",
        "promotions": [
          {
            "amount_without_discount": "6000",
            "amount_with_discount": "5000",
            "sequence": 1
          },
          {
            "amount_without_discount": "5000",
            "amount_with_discount": "4000",
            "sequence": 2
          }
        ],
        "custom_attributes":
          {
            "purchased": 0,
            "attr": "value"
          }
      },
      {
        "sku": "com.xsolla.item_new_1",
        "type": "bundle",
        "is_pre_order": False,
        "quantity": 1,
        "amount": "1000",
        "promotions": []
      },
      {
        "sku": "com.xsolla.gold_1",
        "type": "virtual_currency",
        "is_pre_order": False,
        "quantity": 1500,
        "amount": None,
        "promotions": []
      }
    ],
    "order": {
      "id": 10000 + int(payment_id),
      "mode": "default",
      "currency_type": "virtual",
      "currency": "sku_currency",
      "amount": "2000",
      "status": "paid",
      "platform": "xsolla",
      "comment": None,
      "invoice_id": "1",
      "promotions": [
        {
          "amount_without_discount": "4000",
          "amount_with_discount": "2000",
          "sequence": 1
        }
      ],
      "promocodes": [
        {
          "code": "promocode_some_code",
          "external_id": "promocode_sku"
        }
      ],
      "coupons": [
        {
          "code": "WINTER2021",
          "external_id": "coupon_sku"
        }
      ]
    },
    "user": {
      "external_id": "id_xsolla_login_1",
      "email": "gc_user@xsolla.com",
      "country": "US"
    },
    "billing": {
      "notification_type": "payment",
      "settings": {
        "project_id": 18404,
        "merchant_id": 2340
      },
      "purchase": {
          "subscription": {
              "plan_id": "b5dac9c8",
              "subscription_id": "10",
              "product_id": "Demo Product",
              "date_create": "2014-09-22T19:25:25+04:00",
              "date_next_charge": "2014-10-22T19:25:25+04:00",
              "currency": "USD",
              "amount": 9.99
          },
          "total": {
              "currency": "USD",
              "amount": 200
          },
          "promotions": [{
              "technical_name": "Demo Promotion",
              "id": 853
          }],
          "coupon": {
              "coupon_code": "ICvj45S4FUOyy",
              "campaign_code": "1507"
          }
        },
      "transaction": {
          "id": 1,
          "external_id": payment_id,
          "payment_date": "2014-09-24T20:38:16+04:00",
          "payment_method": 1,
          "payment_method_name": "PayPal",
          "payment_method_order_id": 1234567890123456789,
          "dry_run": 1,
          "agreement": 1
      },
      "payment_details": {
          "payment": {
              "currency": "USD",
              "amount": 230
          },
          "vat": {
              "currency": "USD",
              "amount": 0,
              "percent": 20
          },
          "sales_tax": {
              "currency": "USD",
              "amount": 0,
              "percent": 0
          },
          "direct_wht": {
              "currency": "USD",
              "amount": 0,
              "percent": 0
          },
          "payout_currency_rate": "1",
          "payout": {
              "currency": "USD",
              "amount": 200
          },
          "country_wht": {
              "currency": "USD",
              "amount": 2,
              "percent": 10
          },
          "user_acquisition_fee": {
              "currency": "USD",
              "amount": 2,
              "percent": 1
          },
          "xsolla_fee": {
              "currency": "USD",
              "amount": 10
          },
          "payment_method_fee": {
              "currency": "USD",
              "amount": 20
          },
          "repatriation_commission": {
              "currency": "USD",
              "amount": 10
          }
      }
    },
    "custom_parameters": {
        "parameter1": "value1",
        "parameter2": "value2"
    }
}

request_body = json.dumps(data)
string_to_sign = request_body + secret
signature = hashlib.sha1(string_to_sign.encode('utf-8')).hexdigest()

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'authorization': f'Signature {signature}'
}

print("sending with signature: ", signature)
response = requests.post(url, headers=headers, data=request_body)

print(f"Status Code: {response.status_code}")
try:
    print(f"Response JSON: {response.json()}")
except json.JSONDecodeError:
    print(f"Response Text: {response.text}")
