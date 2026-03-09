#importar la libreria de faker
from faker import Faker

faker = Faker("es_MX")

print ("generado datos dumy con faker")
print(f"nombre: {faker.name()}")
print(f"direccion:{faker.address()}")
print(f"direccion:{faker.phone_number()}")
print(f"direccion:{faker.email()}")
