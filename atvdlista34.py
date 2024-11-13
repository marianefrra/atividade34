#lendo 5 números e armazenando na lista 

nume  = []
for i in range(5):
    num = int(input(f"digite o número {i + 1}: "))
    nume.append(num)

#exibindo cada número com sua posição 
for posicao, num in enumerate(nume):
    print(f"posição {posicao}: número {num}")