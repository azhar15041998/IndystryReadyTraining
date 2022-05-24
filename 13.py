'''A milk vendor buys milk at the rate of 3.25/lt then adds a litre of water for every
4 litres of milk and sells the water milk at the rate of 4.15/lt. Calculate the gain
for milk vendor.'''

#vendor buys milk at 3.25/lt rate and add 1 litre for every 4 litre
a = 3.25 * (4+1)
#Now the total milk  is 5 litre sell at 4.15/lt i,e.
b = 4.15 * (4+1)
profit = b - a  #for 5 litres, for every litre  profit/5
print("The gain rate  for the milk vendor is",profit)