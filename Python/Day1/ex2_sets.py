#SETS 

# Create a list for transactions 
transacton_customer_id = [1,2,5,2,4,8]
print(transacton_customer_id)

# Create a set for active customers - set only holds unique values
active_customers = set(transacton_customer_id)
print(active_customers)

# Create a new set for all customers
all_customers = set(range(1,11))
print(all_customers)

# Create a difference between the two sets - inactive customers
inactive_customers = all_customers - active_customers
print(inactive_customers)

