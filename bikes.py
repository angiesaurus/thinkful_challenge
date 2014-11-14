#!/usr/bin/env python

import random

class Bicycle(object):
    def __init__(self, model_name, weight, production_cost):
		self.model_name = model_name
		self.weight = weight
		self.production_cost = production_cost
		self.sale_price = production_cost

    def set_sale_price(self, price):
        self.sale_price = price

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
		self.bikes = []
		self.customers = []
		self.name = name
		self.profit = 0
		self.inventory = {}

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def bike_cost(self, bike):
		bike.sale_price = bike.production_cost * (1 + self.profit_margin)
		return bike.sale_price
		
	def add_customer(self, customer):
		self.customers.append(customer)
	
	def add_bike(self, bike):
			self.bikes.append(bike)

	def create_inventory(self):
		for bike in self.bikes:
			self.inventory[bike.model_name] = 10

	def get_inventory(self):
		return self.inventory

	def total_profit(self):
		return self.profit

	def available_bikes(self, max_costs):
		affordable_bikes = []
		for bike in self.bikes:
			if self.bike_cost(bike) <= max_costs:
				affordable_bikes.append(bike)
		return affordable_bikes

	def sell_bike(self, bike, customer):
		if self.inventory[bike.model_name] > 0:
			self.inventory[bike.model_name] -= 1
			customer.buy_bike(bike)
			self.profit += bike.sale_price - bike.production_cost


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
		self.bikes = []

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def buy_bike(self, bike):
		self.available_funds = self.available_funds - bike.sale_price
		self.bikes.append(bike)
		
        
customers = ["Bob","Mary","Jack"]
dollars = [200.00,500.00,1000.00]

for (name, money) in zip(customers, dollars):
    angies_shop.add_customer(Customer(name, money))

angies_shop.create_inventory()

print 'The initial shop inventory is '
for (k,v) in angies_shop.get_inventory().items():
	print "%s:\t%s" % (k,v)
print 

print "The following customers are looking to buy a bike: "
for customer in angies_shop.customers:
	print customer
print

for customer in angies_shop.customers:
	bike = angies_shop.available_bikes(customer.available_funds)[0]
	angies_shop.sell_bike(bike, customer)
	print "Angie's Shop Sold {0} to {1} for ${2:.2f}".format(bike.model_name, customer.name, bike.sale_price)
	print "%s now has $%.2f." % (customer.name, customer.available_funds)
	print
	print 'The current shop inventory is '
	for (k,v) in angies_shop.get_inventory().items():
		print "%s:\t%s" % (k,v)
	print "Angie's shop has made $%.2f" % angies_shop.total_profit()
	print 

# print angies_shop.get_inventory()
# print angies_shop.total_profit()

