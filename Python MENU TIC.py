menu = {
    "Comidas": {
        "1": {"Prato do dia(Catxupa)": 1500.00},
        "2": {"Bifana" :150.00},
        "3": {"Hambúrguer": 300.00},
        "4": {"Salada mista": 1000.00},
        "5": {"Camarão": 800.00},
        "6": {"Spaghetti": 300.00},
        "7": {"Polvo": 2000.00},
        "8": {"Bacalhau": 2500.00}
    },
    "Bebidas": {
        "9": {"Refrigerante": 120.00},
        "10": {"Cerveja": 150.00},
        "11": {"Vinho": 300.00},
        "12": {"Suco de frutas" :100}, 
        "13": {"Água": 30.00}
    },
    "Sobremesas": {
        "13": {"Bolo de chocolate": 200.00},
        "14": {"Pudim": 150.00},
        "15": {"Gelado": 100.00}
    }
}

print("=" * 50)
print("                   Bem-vindo ao Restaurante Sabor & Terra".center(50))
print("=" * 50)
print("Aqui está o nosso menu:")
print("--" * 50)
for secao, itens in menu.items():
    print(f"                                      {secao.upper()}")
    print("--" * 50)
    for id_item, info_item in itens.items():
        nome_item = list(info_item.keys())[0]
        preco_item = list(info_item.values())[0]
        print(f"{id_item} - {nome_item:<20}   |          Preço: {preco_item:,.2f} ECV")
    print("--" * 50)

print("(Digite \"fim\" para terminar o pedido)")
print("")
pedido_final = {}
total = 0
while True:
    pedido = input("Digite o número do item que deseja pedir\nMENU: ")
    print("")
    if pedido == "fim":
        break
    else:
        for secao, itens in menu.items():
            if pedido in itens:
                quantidade = int(input("Digite a quantidade que deseja abaixo\nQuanidade: "))
                print("")
                preco_item = float(list(itens[pedido].values())[0])
                print(f"Você escolheu {quantidade} unidade(s) de {list(itens[pedido].keys())[0]} no valor de {preco_item:,.2f} ECV cada")
                print("=" * 50)
                total_item = preco_item * quantidade
                if pedido in pedido_final:
                    pedido_final[pedido]["quantidade"] += quantidade
                    pedido_final[pedido]["valor_total"] += total_item
                else:
                    pedido_final[pedido] = {"quantidade": quantidade, "valor_total": total_item}
                total += total_item
                break
        else:
            print("Opção inválida. Por favor, escolha um número válido do menu.")
            print("=" * 50)

print("=" * 50)
print("                                       RECIBO")
print("=" * 50)
for id_pedido, info_pedido in pedido_final.items():
    for secao, itens in menu.items():
        if id_pedido in itens:
            nome_item = list(itens[id_pedido].keys())[0]
            quantidade_item = info_pedido["quantidade"]
            total_item = info_pedido["valor_total"]
            print(f"{quantidade_item} unidade(s) de {nome_item:<20} - {total_item:,.2f} ECV")
print("--" * 50)
print(f"TOTAL DA COMPRA: {total:,.2f} ECV")
