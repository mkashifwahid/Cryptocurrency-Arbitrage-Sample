import requests
import pandas as pd
import datetime


def Cryptonator_Api(coin, comparison_currency):
    url = 'https://api.cryptonator.com/api/full/{}-{}' \
        .format(coin, comparison_currency)
    page = requests.get(url)
    data = page.json()['ticker']['markets']
    df = pd.DataFrame(data)

    return df
