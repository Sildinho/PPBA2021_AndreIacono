# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 24 """

# 24. If, Else

velocidade = int(input("Informe sua velocidade: "))
permitida = 80

if velocidade > 80:
    print(f"Você está a {velocidade} km/h. Acima da velocidade permitida. reduza para {permitida} km/h.")
elif velocidade < 72:
    print(f"Você está a {velocidade} km/h. Favor aumente sua velocidade e não ultrapasse {permitida} km/h.")
elif velocidade <= 40:
    print(f"Você está a {velocidade} km/h. A baixa velocidade em rodovias tb é perigoso. Favor aumente sua velocidade e nao ultrapasse {permitida} km/h.")
else:
    print(f"Você está a {velocidade} km/h. Permaneça dentro do limite de velocidade {permitida} km/h.")
