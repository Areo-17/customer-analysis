from generate_data import Generator

generator = Generator(0)
customers = []
for i in range(50):
    customer = generator.user()
    customers.append(customer)
print(customers)