# AFE1_Crypto

Cryptocurrency arbitrage bot.

### What is needed to run the code

- python version: 3.10.1
- install all pip's form the requirements.txt

## Database

For simplicity reasons we use sqlite as our main database. SQLite is already integrated in to python and doesn't need aditional services.
In the folder sqliteTutorial you can find a short example for the main usecases (CREATE, WRITE, UPDATE, DELETE, SELECT)

## Binance API

(We are using the pip python-binance to access the binance spot api.
To better understand the API we used Postman. Binance provides a .json file for Postman. It can be found in the repository too.) --> OLD

Best approch until now is using a websocket from the Binance API. We get a price feed with ~30 updates/sec.
