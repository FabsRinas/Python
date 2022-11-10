print("-="*15)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
       'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
       'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
       'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print("-="*15)
print(f"Lista de times do Brasileirão: {times}")
print("-="*15)
print(f"Os primeiros 5 times são: {times[0:5]}")
print("-="*15)
print(f"Os 4 últimos times são: {times[-4:]}")
print("-="*15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-="*15)
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição')
