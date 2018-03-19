import Arbitrage_Graph as g

coin = input("Enter coin here : ")
comparison_Currency = input("Enter target currency here  : ")
print ("Please Wait ... Graph in process, your base coin is ",coin," & your target currency is ",comparison_Currency)

g.Plot_Graph(coin, comparison_Currency)


