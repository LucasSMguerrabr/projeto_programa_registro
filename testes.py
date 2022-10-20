#Fase 1  Desenvolvimento inicial.

data = str(input("Digite  a data:")).strip() #data repete
setor = str(input("Digite seu setor")).strip()#ecoat,banho-asp, banho-imer(perguntar ao usuário) um botao para cada opcao.
nome = str(input("Ïnsira o seu nome: ")).strip().upper() #nome repete
#cliente = str(input("Digite o nome do cliente:")).strip().upper()
#modelotanq = int(input("Digite o modelo do tanque: "))
#codigotanq = int(input("Digite o código do tanque: "))
listaModeTanq = [] #camelCase
listaCodigoTanq = []
listaCliente = []
for index in range(5):
    index += 1 #chegar ate 5 ele para o loop
    cliente = str(input("Digite o nome do cliente:")).strip().upper()
    listaCliente.append(cliente)
    modelotanq = int(input("Digite o modelo do tanque: "))
    listaModeTanq.append(modelotanq)
    codigoTanq = int(input("Digite o código do tanque: "))
    listaCodigoTanq.append(codigoTanq)
    pergunta = str(input("Gostaria de continuar ou finalizar(Digite SIM ou NAO): ")).strip()
    if pergunta == "NAO":
        break
print("Lista de modelo de tanques")
print(listaModeTanq)
print("-=-"*10)
print("Lista de clientes ")
print(listaCliente)
print("-=-"*10)
print("Lista de codigos de tanques " )
print(listaCodigoTanq)
print("-=-"*10)