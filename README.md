# Digital Game Item Store solution - Tamas Temesvari

## Current state

Implemented the item list, purchases list, and a simple working payment flow.

There is an endpoint and a test script for simulation xsolla webhook, but HMAC verification is not yet included

## Limitations

No HMAC verification

No user authentication or verification

Environment only for FireBase studio

## How to run

The environment is defined for FireBase studio (project idx), can import into it directly from a git repository.

Without that, the following is needed:

- have a mysql server running at localhost, default port, user root without password
- run these commands (excerpt from dev.nix):

```
install = "cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
init-db = "mysql -u root < init.sql";
npm-install = "npm ci --no-audit --prefer-offline --no-progress --timing";
```

```
command = ["npm" "run" "dev" "--" "--port" "$PORT" "--host" "0.0.0.0"];
```

- open app from localhost:9000 (default)
