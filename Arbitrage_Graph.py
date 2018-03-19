import matplotlib.pyplot as plt
import Arbitrage_API as main
import numpy as np
import pandas as pd
import datetime

def Plot_Graph(coin, currency):
    fig = plt.figure()
    ax = fig.subplots()

    while (True):
        data = pd.DataFrame(main.Cryptonator_Api(coin,currency))
        ax.scatter(data['price'], data['volume'])
        title = '{} in {} on {} '.\
            format(coin, currency, datetime.datetime.utcnow().strftime('%d-%m-%Y %I:%M:%S'))

        fig.suptitle(title)
        print(title)
        #
        print("High Market is {} with price {}".format(data[data.price == np.max(data['price'])].market.item(), np.max(data['price'])))
        print(" Low Market is {} with price {}".format(data[data.price == np.min(data['price'])].market.item(), np.min(data['price'])))
        print(" Difference is {}".format(float(np.max(data['price']))-float(np.min(data['price']))))

        plt.ylabel('Currency Volume')
        plt.xlabel('Currency Price')
        plt.locator_params(nbins=8)
        for i, gText in enumerate(data['market']):
                ax.annotate(gText, (data['price'][i], data['volume'][i]))


        plt.pause(300)

