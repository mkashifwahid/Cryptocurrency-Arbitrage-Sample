# Cryptocurrency-Arbitrage-Sample
Cryptocurrency Arbitrage Finding Mismatched Prices in Different Exchanges

## Getting Start
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites
Python with libraries
  ```
  matplotlib
  numpy
  pandas
  datetime
  requests
  ```


### Code file details
```
Index.py           Interact with user
Arbitrage_API.py   Call api for data from https://api.cryptonator.com/api/full
Arbitrage_Graph.py Working on graph represtation
```

### Sequence of calling files
```
Index.py will interact with user and call Arbitrage_Graph.py function with giving parameter of coin and currency
Arbitrage_Graph call Arbitrage Api Function for Data
```
