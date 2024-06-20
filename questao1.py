idade = int(
  input("Digite a idade do nadador (número inteiro): ")
)
categoria = "Sem categoria"

if(idade < 5):
  print("O nadador não tem a idade mínima necessária.")
  exit()
elif(idade >= 5 and idade <= 7):
  categoria = "Infantil A"
elif(idade <= 10):
  categoria = "Infantil B"
elif(idade <= 13):
  categoria = "Juvenil A"
elif(idade <= 17):
  categoria = "Juvenil B"
elif(idade > 17):
  categoria = "Adulto"

print(f"A categoria do nadador é: {categoria}")
