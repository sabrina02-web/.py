
def exibir_cardapio(): 
    print("\n---------------- CARDÁPIO ----------------") 
    print("Código 101 - Cachorro Quente - R$ 12.00") 
    print("Código 102 - X-Salada - R$ 18.00") 
    print("Código 103 - X-Burguer - R$ 20.00") 
    print("Código 104 - Refrigerante - R$ 6.00") 
    print("Código 105 - Suco Natural - R$ 8.00")
    print("------------------------------------------\n")

def calcular_desconto(valor_total):
    if valor_total < 50.0:
        return 0
    elif valor_total < 100.0:
        return 5
    else:
        return 10
    
print("BEM-VINDO AO SISTEMA DE ATENDIMENTO DA LANCHONETE")
nome_cliente = input("Digite o nome do cliente: ")

exibir_cardapio()

total_compra = 0.0
deseja_continuar = "S"

while deseja_continuar.upper() == "S":
    codigo = input("Digite o código do produto desejado: ")
    preco_unitario = 0.0
    nome_produto = ""
    codigo_valido = True

    if codigo == "101":
        nome_produto = "Cachorro Quente"
        preco_unitario = 12.00
    elif codigo == "102":
        nome_produto = "X-Salada"
        preco_unitario = 18.00
    elif codigo == "103":
        nome_produto = "X-Burguer"
        preco_unitario = 20.00
    elif codigo == "104":
        nome_produto = "Refrigerante"
        preco_unitario = 6.00
    elif codigo == "105":
        nome_produto = "Suco Natural"
        preco_unitario = 8.00
    else:
        codigo_valido = False
        print("Código inválido! Tente novamente.\n")

    if codigo_valido:
        quantidade = int(input(f"Digite a quantidade de '{nome_produto}': "))
        subtotal = preco_unitario * quantidade

        total_compra = total_compra + subtotal

        print(f" Adicionado: {quantidade}x {nome_produto} = R$ {subtotal:.2f}")
        print(f" Total parcial: R$ {total_compra:.2f}\n")

    deseja_continuar = input("Deseja adicionar mais algum item?: ")

porcentagem_desconto = calcular_desconto(total_compra)
valor_desconto = total_compra * (porcentagem_desconto / 100)
valor_final = total_compra - valor_desconto

print("\n FORMA DE PAGAMENTO")
print("1 - Dinheiro")
print("2 - PIX")
print("3 - Cartão")

opcao_pagamento = input("Escolha a opção de pagamento (1, 2 ou 3): ")

while opcao_pagamento != "1" and opcao_pagamento != "2" and opcao_pagamento != "3":
    print("⚠️ Opção inválida! Escolha 1, 2 ou 3.")
    opcao_pagamento = input("Escolha a opção de pagamento (1, 2 ou 3): ")

if opcao_pagamento == "1":
    forma_pagamento_texto = "Dinheiro"
elif opcao_pagamento == "2":
    forma_pagamento_texto = "PIX"
else:
    forma_pagamento_texto = "Cartão"

print("\n" + "=" * 45)
print("            RECEIBO / COMPROVANTE")
print("=" * 45)
print(f"Cliente: {nome_cliente}")
print(f"Valor Original: R$ {total_compra:.2f}")
print(f"Desconto Aplicado: {porcentagem_desconto}% (R$ {valor_desconto:.2f})")
print(f"VALOR FINAL A PAGAR: R$ {valor_final:.2f}")
print(f"Forma de Pagamento: {forma_pagamento_texto}")
print("=" * 45)
print("Obrigado pela preferência!") 
