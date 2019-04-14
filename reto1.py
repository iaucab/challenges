'''Reto 1. Estructuras de datos y control de versiones
Rojo, es un entrenador pokémon de la región de Kanto. Él se encontraba en Pueblo Paleta (0) acariciando su Pikachu cuando le llegan noticias que en la Pueblo Lavanda (6) están poniendo música tétrica que horroriza a los vecinos. Como lleva tiempo sin salir, Rojo decide caminar hacia el lugar para ayudar. ¿Cuál puede ser uno de los trayectos que puede realizar Rojo para llegar al pueblo sin pasar dos veces por la misma ruta? (Solo puede ir por los caminos señalados en blanco o azul). A continuación se muestra una matriz de adyeacencias:

  mapa = [00],
          1[1,0,1,0,0,0,0,0,0,0,0,1,0],
          2[0,1,0,1,0,0,0,0,0,0,0,0,0],
          3[0,0,1,0,1,1,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,1,1,1,0,0,0,0],
          [0,0,0,1,0,1,0,0,1,1,0,0,0],
          [0,0,0,0,0,1,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,1,0,0,1,0,0,0],
          [0,0,0,0,0,0,1,1,1,0,1,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0]]'''

mapa =    [
          [0,1,0,0,0,0,0,0,0,0,1,0,0],
          [1,0,1,0,0,0,0,0,0,0,0,1,0],
          [0,1,0,1,0,0,0,0,0,0,0,0,0],
          [0,0,1,0,1,1,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,1,1,1,0,0,0,0],
          [0,0,0,1,0,1,0,0,1,1,0,0,0],
          [0,0,0,0,0,1,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,1,0,0,1,0,0,0],
          [0,0,0,0,0,0,1,1,1,0,1,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0]]

class City:
  neighbors=[]

  def __init__(self, number):
    self.number=number
    self.check=False
    self.neighbors  = []

cities = []

# Creamos las ciudades
for i in range(len(mapa)):
  cities.append(City(i))


#Añadimos los vecinos
for i in range(len(mapa)):
  for j in range(len(mapa)):
    if mapa[i][j] == 1:
      cities[i].neighbors.append(cities[j])

for i in cities:
  print("City ", i.number, end ="-> ")
  for j in i.neighbors:
    print("Neighbor",j.number, end=" ")
  print()



def path(startCity, endCity):
  # Se llegó a la ciudad?
  if startCity == endCity:
    return [startCity] #devuelve la ciudad de llegada
  else:
    minPath=[]
    #Recorro los vecinos de la ciudad
    for n in startCity.neighbors:
      #Si no ha sido visitado el vecino
      if not n.check:
        #Marco la ciudad de partida
        startCity.check=True
        #Concateno el resultado a la ciudad de partida
        p=[startCity]+path(n, endCity)
        #Desmarco la ciudad para que futuros vecinos puedan visitarla
        startCity.check=False
        #Si hay más de dos ciudades (se obtuvo un resultado) y el trayecto es menor al anterior
        if len(p)>1 and (len(p)<len(minPath) or 
        len(minPath)==0):
          minPath = p #Trayecto mínimo es el obtenido anteriormente
    return minPath


arr = path(cities[0],cities[6])

for i in arr:
  print(i.number,end=" ")
