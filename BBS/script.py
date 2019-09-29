import csv

def inputUserData(name, degree, email, purpose, item_name, item_description, price):
	#if(purpose=='sell'):
	with open('sale.csv', 'a') as f:
		print("In function", [name, degree, email, item_name, item_description, price])
		line = csv.writer(f, delimiter=' ',
		                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
		line.writerow([name, degree, email, item_name, item_description, price])

