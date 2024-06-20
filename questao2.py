termo1 = int(input("Digite o primeiro termo (um numero inteiro): "))
termo2 = int(input("Digite o segundo termo (um numero inteiro): "))

listaTermos = [termo1, termo2]

print("1° Termo:", listaTermos[0])
print("2° Termo:", listaTermos[1])

for contador in range(0, 20):
  listaTermos.append(
    listaTermos[contador] + listaTermos[contador + 1]
  )
  print(f"{contador+3}° Termo: {listaTermos[contador + 2]}")
