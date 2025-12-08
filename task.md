# Digital Game Item Store - Take-Home Coding Challenge

## Overview

You are tasked with building a minimal digital store for a fictional game. Players can browse and purchase digital items (e.g., skins or power-ups). Once a purchase is made, a third-party payment provider (like Xsolla) sends a webhook confirming the purchase. Your backend must securely verify the webhook, update the database, and display the purchase on the frontend.

Prioritize code clarity, security, structure, and core functionality.

---

## Objectives

### Core Requirements

#### Backend (Python preferred, Go/C# acceptable)

- Create a REST API with the following endpoints:
  - `GET /api/items`: List all available game items.
  - `GET /api/purchases`: List all purchases for a test user.
  - `POST /api/webhooks/payment`: Accept payment confirmation webhook from the payment provider (simulate Xsolla).
- Validate and verify webhook authenticity using **HMAC with shared secret**.
- Store and cache data using **SQL Database** and **Redis**.
- Apply proper **input validation**, **error handling**, and **status codes**.

#### Frontend (Vue.js or Angular)

- Build a simple UI to:
  - Display all available game items.
  - Show a list of purchases for a test user.
  - Indicate if a purchase is successful after a simulated webhook.

#### Database Design

- Use a **relational schema** for items and purchases (incomplete example):
  - `items(id, name, description, price)`
  - `purchases(id, user_id, item_id, timestamp)`
- Add any auxiliary fields or tables you find necessary.

#### Webhook Security

- Implement the basic [Xsolla's Successful Order Payment](https://developers.xsolla.com/webhooks/operation/successful-order-payment)
- Implement HMAC signature verification.
- Use a shared secret (e.g., `XSOLLA_WEBHOOK_SECRET`).
- Validate incoming webhook headers and body integrity.
- Validate that the purchase is unique based on the order ID

#### Simulated Webhook

- Provide a script to send a simulated webhook request (check the documentation to understand the payload, feel free to ignore not needed fields in order to simplify the request).
- The script should:
  - Mimic the structure of [Xsolla's Successful Order Payment](https://developers.xsolla.com/webhooks/operation/successful-order-payment).
  - Generate the HMAC signature and send the correct headers.

---

## Folder Structure (Suggested)

```
digital-store/
├── backend/
│   ├── app/
│   ├── requirements.txt
├── frontend/
│   ├── src/
│   ├── package.json
├── scripts/
│   └── simulate_webhook.py
```

---

## Deliverables

- Fully functional backend and frontend apps.
- A webhook simulation script with example payload and signature generation.

---

## Bonus Points

- Unit and integration tests
- Clean, modular code structure
- Pagination or filtering on API endpoints
- Frontend polish and user-friendly UI

---

## References 

- https://developers.xsolla.com/webhooks/overview/#section/Webhook-listener/Generation-of-signature
- https://developers.xsolla.com/webhooks/operation/successful-order-payment/



The project as presented has been tested. Part of the evaluation involves being able to efficiently resolve potential errors or omissions, and keep a record of your decision making process.

Good luck! We’re excited to see your solution.
