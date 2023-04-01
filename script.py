# Shreya B Deshpande
# This project is done through Codecademy
# The project prints cost for ground shipping and the cost for drone shipping accordin to the weight. 
# Cost of ground shipping also includes flat charge and sometimes ground shipping premium.

weight = 1.5

if (2 >= weight):
  cost = (weight * 1.50) + 20.00
elif (2 < weight <= 6):
  cost = (weight * 3.00) + 20.00
elif (6 < weight <= 10):
  cost = (weight * 4.00) + 20.00
elif (weight < 10):
  cost = (weight * 4.75) + 20.00

print(cost)

premium_ground_shipping_cost = 125.00
print(premium_ground_shipping_cost)

if (2 >= weight):
  cost = (weight * 4.50)
elif (2 < weight <= 6):
  cost = (weight * 9.00)
elif (6 < weight <= 10):
  cost = (weight * 12.00)
elif (weight < 10):
  cost = (weight * 14.25)

print(cost)