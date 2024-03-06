papa = 0
yuca = 0
zanahoria = 0
cultivoStr = (input('Cual cultivo vas a regar? \n1.papa\n2.yuca\n3.zanahoria\n ->'))


if cultivoStr == '1':
    for i in range(3):
        litrosregados =int(input('Cuantos litros regaste hoy? ->'))
        papa += litrosregados
    print('El total de litros de agua regados en el cultivo de papa esta semana fueron:' , papa)

if cultivoStr == '2':
    for i in range(2):
        litrosregados = int(input('Cuantos litros regaste hoy? ->'))
        yuca += litrosregados
    print('El total de litros de agua regados en el cultivo de yuca esta semana fueron:' , yuca)

if cultivoStr == '3':
    for i in range(2):
        litrosregados = int(input('Cuantos litros regaste hoy? ->'))
        zanahoria += litrosregados
    print('El total de litros de agua regados en el cultivo de zanahoria esta semana fueron:' , zanahoria)
