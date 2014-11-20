class Bicycle(object):
	def __init__(self, model_name, weight, production_cost):
		self.model_name = model_name
		self.weight = weight
		self.production_cost = production_cost


class BikeShops(object):
	profit_margin = (.20 x production_cost)
	def __init__(self, name, inventory, overall_profit):
		self.name = name
		self.inventory = inventory
		self.overall_profit = overall_profit


class Customer(object):
	can_buy = True
	def __init__(self, name, available_funds):
		self.name = name
		self.available_funds = available_funds