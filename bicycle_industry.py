import random

class Bicycle(object):
	def __init__(self, model_name, weight, production_cost):
		self.model_name = model_name
		self.weight = weight
		self.production_cost = production_cost

	def __str__(self):
		return self.model_name

	def __repr__(self):
		return self.model_name

bike1 = Bicycle('Cruiser', 10, 400.00)
bike2 = Bicycle('Anti-Cruister', 40, 655.00)
bike3 = Bicycle('Uphill Tank', 8, 150.00)
bike4 = Bicycle('Fixed Fixie', 13, 800.00)
bike5 = Bicycle('Lazy Cat', 10, 545.00)
bike6 = Bicycle('Torpedo', 11, 1275.00)

class BikeShop(object):
	profit_margin = .20 
	def __init__(self, name):
		#self.bikes = dict
		self.bikes = []
		self.customers = []
		self.name = name
		self.profit = 0

	# def bike_names(self, bike):
	# 	self.bike_name.append(bike.model_name)
	# 	print self.bike_name

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def bike_cost(self, bike):
		bike_cost = (bike.production_cost * (1 + self.profit_margin))
		return bike_cost
		
	def add_customer(self, customer):
		self.customers.append(customer)

	def print_customers(self):
		for customer in self.customers:
			return customer

	def add_bike(self, bike):
			self.bikes.append(bike)

	def get_inventory(self):
		inventory = {}
		for bike in self.bikes:
			inventory[bike.model_name] = 10
		return inventory

	def overall_profit(self, bike_cost):
		profit += (bike_cost() - bike.production_cost)
		return profit

	def available_bikes(self, max_costs):
		affordable_bikes = []
		for bike in self.bikes:
			if self.bike_cost(bike) <= max_costs:
				affordable_bikes.append(bike)
		return affordable_bikes


	# def purchase(self, customer):
	# 	for customer in self.customers:
	# 		bought_bike = random.choice(AngiesShop.available_bikes(customer.available_funds))
	# 	print bought_bike

	def purchased_bike(self, bike, customer):
		if bike in self.bikes:
			self.bikes.remove(bike)
			customer.bike_payment(bike_cost)
			self.profit += bike_cost


angies_shop = BikeShop('angies_shop')
angies_shop.add_bike(bike1)
angies_shop.add_bike(bike2)
angies_shop.add_bike(bike3)
angies_shop.add_bike(bike4)
angies_shop.add_bike(bike5)
angies_shop.add_bike(bike6)

class Customer(object):
	def __init__(self, name, available_funds):
		self.name = name
		self.available_funds = available_funds

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name
		
	def bike_payment(self, bike_cost):
		self.available_funds -= bike_cost

customer1 = Customer('Bob', 200.00,)
customer2 = Customer('Mary', 500.00)
customer3 = Customer('Jack', 1000.00)

#create customer when they enter the shop

angies_shop.add_customer(customer1)
angies_shop.add_customer(customer2)
angies_shop.add_customer(customer3)


# print customer1.name, AngiesShop.available_bikes(customer1.available_funds)
# # prints Bob[Uphill Tank]

# print customer2.name, AngiesShop.available_bikes(customer2.available_funds)
# #prints Mary[Cruiser, Uphill Tank]

# print customer3.name, AngiesShop.available_bikes(customer3.available_funds)
# #prints Jack[Cruiser, Anti-Cruiser, Uphill Tank, Fixed Fixie, Lazy Cat]

print angies_shop.get_inventory()
"""
prints Cruiser : 10
Anti-Cruister : 10
Uphill Tank : 10
Fixed Fixie : 10
Lazy Cat : 10
Torpedo : 10
"""

purchase1 = random.choice(angies_shop.available_bikes(customer1.available_funds))
purchase2 = random.choice(angies_shop.available_bikes(customer2.available_funds))
purchase3 = random.choice(angies_shop.available_bikes(customer3.available_funds))

print 'The following bikes were purchased: '
print str(customer1.name) + ' : ' + str(purchase1)
print str(customer2.name) + ' : ' + str(purchase2)
print str(customer3.name) + ' : ' + str(purchase3)

angies_shop.purchased_bike(purchase1, customer1)
# purchase3
# AngiesShop.purchase(customer1)
# AngiesShop.purchase(customer2)

