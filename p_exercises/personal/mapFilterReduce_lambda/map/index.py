
from functools import reduce 

dollars = ["32$", "15$", "12$", "17$", "20$"] 
print('\n>>>> Dollars: {}\n'.format(dollars)) 

prices = list(map(lambda dollar: int(dollar[0:-1]), dollars))
expensive = list(filter(lambda price: price >= 20, prices))
total = reduce(lambda acum, price,: acum + price, expensive, 0) 

print('>>>> Prices: {}'.format(prices)) 
print('>>>> Expensive: {}'.format(expensive))
print('>>>> Total: {}\n'.format(total))

