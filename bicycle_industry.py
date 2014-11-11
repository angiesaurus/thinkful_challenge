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

class BikeShops(object):
	profit_margin = .20 
	def __init__(self, name):
		self.bikes = []
		self.customers = []
		self.name = name
		self.profit = 0

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def bike_cost(self, bike):
		return bike.production_cost * (1 + self.profit_margin)

	def add_customer(self, customer):
		self.customers.append(customer)

	def print_customers(self):
		for customer in self.customers:
			print customer

	def add_bike(self, bike):
		self.bikes.append(bike)

	def get_inventory(self):
		return len(self.bikes)

	# def count_bikes(self):
	# 	for bike in self.bikes:
	# 		self.bikes.count(bike)

	def overall_profit(self, bike_cost):
		profit += (bike_cost() - bike.production_cost)
		print profit

	def available_bikes(self, max_costs):
		affordable_bikes = []
		for bike in self.bikes:
			if self.bike_cost(bike) <= max_costs:
				affordable_bikes.append(bike)
		print affordable_bikes

	def purchased_bike(self, bike, customer):
		if bike in self.bikes:
			self.bikes.remove(bike)
			customer.bike_payment(bike_cost)
			self.profit += bike_cost



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


AngiesShop = BikeShops('AngiesShop')
AngiesShop.add_customer(customer1)
AngiesShop.add_customer(customer2)
AngiesShop.add_customer(customer3)

AngiesShop.add_bike(bike1)
AngiesShop.add_bike(bike2)
AngiesShop.add_bike(bike3)
AngiesShop.add_bike(bike4)
AngiesShop.add_bike(bike5)
AngiesShop.add_bike(bike6)

print AngiesShop.get_inventory()
print customer1.name, AngiesShop.available_bikes(customer1.available_funds)
print customer2.name, AngiesShop.available_bikes(customer2.available_funds)
print customer3.name, AngiesShop.available_bikes(customer3.available_funds)

#AngiesShop.inventory will return 60


