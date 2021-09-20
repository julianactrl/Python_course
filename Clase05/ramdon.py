import random
# caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
# print(random.choice(caras))
# print(random.choices(caras,k=5))

# dado = random.randint(1,6)
# print(dado)

r = [random.randint(1,6) for _ in range(5)]
print(r)