menu = """
-----------------------
####### Menu #######
-----------------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
-----------------------
=> """

extrato_menu = """
-----------------------
###### Extrato ######
-----------------------"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  #Operação DEPÓSITO
  if opcao.lower() == "d":
      print("Depósito")

      deposito = float(input("Insira o valor que deseja depositar =>"))
      
      if deposito > 0:
        saldo += deposito

        extrato += f"Deposito: R$ {deposito:.2f}\n"
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
  
      else:
        print("Valor de depósito inválido!")

  #Operação SAQUE
  elif opcao.lower() == "s":
      print("Saque")

      saque = float(input("Insira o valor que deseja sacar =>"))

      if saque > saldo:
        print("Não foi possível fazer o saque. Saldo insuficiente!")
      
      elif saque > limite:
        print("Não foi possível fazer o saque. O valor excede o limite!")

      elif numero_saques >= LIMITE_SAQUES:
        print("Não foi possível fazer o saque. Limite de saques diários excedido!")

      elif saque > 0:
        numero_saques += 1
        saldo -= saque
        
        extrato += f"Saque: R$ {saque:.2f}"
        print(f"Saque Realizado de R$ {saque:.2f}\nSaldo atual R$ {saldo:.2f}")
        
      else:
        print("Operação inválida! Digite um valor válido!.")
        continue

  #Operação EXTRATO
  elif opcao.lower() == "e":
      print(extrato_menu)
      
      if not extrato:
        print(f"Não foram realizadas movimentações na conta!\nSaldo atual: R$ {saldo:.2f}")
      else:
        print(f"{extrato}\nSaldo atual R$ {saldo:.2f}")

  #Operação SAIR2
  elif opcao.lower() == "q":
    print("Obrigada por usar nosso sistema bancário!")
    break

  #Informação fora do código
  else:
      print("Operação inválida! Por favor selecione novamente a operação desejada.")