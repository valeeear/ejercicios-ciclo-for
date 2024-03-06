kmtotal = 0
etapas = int(input('Cuantas etapas va a realizar? ->'))
for i in range(etapas):
    kmrecorridos = int(input('Cuantos km recorriste en esta etapa? ->'))
    kmtotal += kmrecorridos
print('La cantidad de kilometros recorridos son:' , kmtotal)
print('La cantidad de etapas recorridas son:' , etapas)
