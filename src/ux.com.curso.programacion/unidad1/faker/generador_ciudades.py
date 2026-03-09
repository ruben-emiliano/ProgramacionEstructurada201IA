from faker import Faker
faker = Faker("es_MX")

#DECLARACIO DE UN VECTOR VACIO
ciudades_ia = []

#OPERACIONES DE LLENADO(CICLO)
for _ in range(5):
    ciudades_ia.append(faker.city())

#ESCRITURA DE ARREGLOS (MOSTRAR RESULTADOS)
print("\n--- DATASET DE CIUDADES GENERADO ---")

for i in range(len(ciudades_ia)):
    print(f"registro{i+1}: {ciudades_ia[i]}")
