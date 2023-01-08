#Carly's Clipper is a barber shop. 
#below shows the names of the cuts offered at Carly’s Clippers.
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
# the price of each hairstyle in the hairstyles list.
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# the number of purchases for each hairstyle type in the last week.
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#task: calculate the  the average price is 
total_price = 0
for price in prices:
  print(price)
  total_price += price 
print(total_price)

number = len(prices)
print(number)
average_price = total_price/ number

# task: 
# lower down the price by 5 dollars for each hairstyles. 
print("Average Haircut Price: " + str(average_price))
new_prices = [i - 5 for i in prices]
print(new_prices)

#task: 
# calculate the revenue Carly's Clippers earned last week. 
total_revenue = 0
for i in range(number):
  print(i)
for i in range(len(hairstyles)):
  total_revenue += prices[i]* last_week[i]
print("Average Haircut Price: " + str(total_revenue))
average_daily_revenue = total_revenue/ 7
print(average_daily_revenue)

#task : 
# print a list that has every haistyles'name that are under 30 dollars. 
price_under_30 = [
  #expression- pick hairstyles' ith elements 
  hairstyles[i]
  #statement- for i in the length 
  for i in range(len(hairstyles)-1)
  #conditional- if - new_prices[i] < 30
  if new_prices[i] < 30
]
print(price_under_30)


