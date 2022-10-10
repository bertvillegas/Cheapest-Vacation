#Write a function called vacation that takes:

#A list of floats called prices, which represents how much a hotel room costs each night
#An int called days, which represents how long of a vacation you want to take in days
#It should return:

#The index of the day your vacation should start on that will ensure you take the cheapest vacation. If there are multiple different days you could start your vacation on to get the cheapest price, return the earlier day.

def vacation(prices, days):
  prices_length = len(prices)
  left = 0
  right = days 
  min_sum = sum(prices[:right])
  min_day = left
  current_sum = min_sum
  while right <= prices_length:
    current_sum = sum(prices[left:right])
    if current_sum < min_sum:
      min_sum = current_sum
      min_day = left
    left += 1
    right += 1
  return min_day 
  pass  

#test
prices =[100, 250, 40, 30, 15, 90]
days = 2
print(vacation(prices,days))


