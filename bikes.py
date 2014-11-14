from bicycle_industry import *

bicycles = [
Bicycle('Cruiser', 10, 400.00),
Bicycle('Anti-Cruister', 40, 655.00),
Bicycle('Uphill Tank', 8, 150.00),
Bicycle('Fixed Fixie', 13, 800.00),
Bicycle('Lazy Cat', 10, 545.00),
Bicycle('Torpedo', 11, 1275.00)
]

angies_shop = BikeShop('angies_shop')

for bike in bicycles:
	angies_shop.add_bike(bike)

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
	print customer.name
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