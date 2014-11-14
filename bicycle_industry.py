#!/usr/bin/env python
class Bicycle(object):
    def __init__(self, model_name, weight, production_cost):
		self.model_name = model_name
		self.weight = weight
		self.production_cost = production_cost
		self.sale_price = production_cost

    def set_sale_price(self, price):
        self.sale_price = price

class BikeShop(object):
	profit_margin = .20 
	def __init__(self, name):
		self.bikes = []
		self.customers = []
		self.name = name
		self.profit = 0
		self.inventory = {}

	def set_bike_price(self, bike):
		bike.sale_price = bike.production_cost * (1 + self.profit_margin)
		
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
			if self.set_bike_price(bike) <= max_costs:
				affordable_bikes.append(bike)
		return affordable_bikes

	def sell_bike(self, bike, customer):
		if self.inventory[bike.model_name] > 0:
			self.inventory[bike.model_name] -= 1
			customer.buy_bike(bike)
			self.profit += bike.sale_price - bike.production_cost


class Customer(object):
	def __init__(self, name, available_funds):
		self.name = name
		self.available_funds = available_funds
		self.bikes = []

	def buy_bike(self, bike):
		self.available_funds = self.available_funds - bike.sale_price
		self.bikes.append(bike)