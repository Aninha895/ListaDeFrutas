# Criando tuplas
coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

# Acessando elementos
print("X:", coordenadas[0], "| Y:", coordenadas[1])

# Slicing (fatiamento) em tuplas
print("Primeiro 3 dias:", dias[:3])

# Tamanho
print("Tamanho da tupla 'dias':", len(dias))

# Verificar se um elemento esta na tupla
print("Tem 'segunda'?", "segunda" in dias)

# Contagem e índice em tuplas
print("Contagem de 'terça':", dias.count("terça"))
print("Índice de 'quarta':", dias.index("quarta"))