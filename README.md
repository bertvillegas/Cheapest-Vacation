# Cheapest Vacation
Write a function called vacation that takes:

A list of floats called prices, which represents how much a hotel room costs each night, An int called days, which represents how long of a vacation you want to take in days

It should return:

The index of the day your vacation should start on that will ensure you take the cheapest vacation. If there are multiple different days you could start your vacation on to get the cheapest price, return the earlier day.

Assumptions: 1 <= days <= len(prices)

The prices will be integers, but there will be no negative prices (some prices could be zero though)
Example:

vacation([100, 80, 75, 50, 200], 3)

If you take a 3-day vacation starting on day 0, it will cost $100 + $80 + $75 = $255

If you take a 3-day vacation starting on day 1, it will cost $80 + $75 + $50 = $205

If you take a 3-day vacation starting on day 2, it will cost $75 + $50 + $200 = $325

The cheapest 3-day vacation starts on day 1, so you should return 1.

