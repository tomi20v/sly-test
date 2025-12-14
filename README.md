# Digital Game Item Store solution - Tamas Temesvari

## Current state

Implemented the 
- item list
- purchases list (available in the top right menu, or after a successful purchase)
- a simple working payment flow
  - when "BUY NOW" button is pressed, it is disabled, and a purchase is created in the backend
  - polling starts to retrieve the purchase's data, the button is replaced by a progress bar
  - if failed (has to be set in the DB manually), an error is displayed, and button is enabled again in a couple if seconds, and the flow restarts with a new purchase when pressed
  - if succeeded, a success message is displayed, and button is replaced by a "MY PURCHASES" button
- the test "payment success" script
- a simple webhook logging system, as it comes very handy in live environments


## Details, BOM

### Backend (python)
- flask
- flask-restful

### Frontend (typescipt)
- vite
- Vue (3)
- Vuetify
- Axios
- Pinia

## Limitations

- There is no authentication, as it was not a requirement and due to time constraints. Due to this, there are no checks if the user is polling his own order, or when asking for his own orders.
- The UI works nicely on desktop, but on small screens the "item detail" dialog might look weird.
- Environment was mounted in FireBase studio, no dockerization (time). With a gmail account a free Firebase Studio can be run in browser and the project imported (https://github.com/tomi20v/sly-test.git)
- There is no build pipeline eg. for github
- There are no unit tests as this is my first python project and would have required extra effort. Nevertheless, I used DI and high separation so unit testing should be straightforward.
- I have not created a backlog, so I have not worked with branches either.
- responses which are not json are not handled well


## How to run

The environment is defined for FireBase studio (project idx), can import into it directly from the git repository (https://github.com/tomi20v/sly-test.git).

Without that, the following is needed:

- have a mysql server running at localhost, default port, user root without password (or the mysql access be set up through env vars, see config.py)
- run these commands to install (extracted from dev.nix):

```
cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
mysql -u root < init.sql
npm ci --no-audit --prefer-offline --no-progress --timing
```
- run these commands to run servers (extracted from dev.nix):


```
cd backend && ./devserver.sh";
```
```
cd frontend && npm run dev
```

- open app from localhost:5173 (default)

