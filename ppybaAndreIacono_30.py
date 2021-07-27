# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 30 """

# 30. For Loop - Utilizando If e Else

compra_confirmada = True
dados_compra = "Compra no valor de $ 120.50 aprovada."

for enviar in range(3):
    if compra_confirmada == True:
        print (dados_compra)
        print ("Detalhes enviados ao email cadastrado")
        break

else:
        print("falha na compra.")
        
