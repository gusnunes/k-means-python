import random

def read_file(file_name):
    data = []

    f = open(file_name, "r")
    for line in f:
        line = line.strip("()\n")   # remover os parenteses e quebras de linha da leitura

        aux = line.split(",")
        data.append((float(aux[0]), float(aux[1])))   # transformar as coordenas de str para float
    
    f.close()
    return data

def inicial_centroids(lista, k):   # sortear itens que serao os centroides dos grupos
    centroids = []
    for i in range(k):
        random_data = random.choice(lista)
        centroids.append(random_data)
        lista.remove(random_data)
    
    return centroids

def calc_distancia(p1, p2):   # ponto p1 e ponto p2
    x1,y1 = p1
    x2,y2 = p2

    return (((x2-x1)**2) + ((y2-y1)**2))**0.5

def calc_centroid(group):
    sum_x = sum_y = size = 0

    for x,y in group:
        sum_x += x
        sum_y += y
        size  += 1

    return (sum_x/size, sum_y/size)

def k_means(data, k):
    centroids = inicial_centroids(data[:], k)
    print(f"\nCentroides iniciais: {centroids}\n")
  
    past_centroids = [None]*k   # centroids da iteracao anterior
    
    relocations = True
    while relocations:
        groups = [[] for i in range(k)]

        for coord in data:
            menor = calc_distancia(coord, centroids[0])
            index = 0

            cont = 1
            while cont < k:   # calcular a distancia entre cada dado e o centroide de cada grup
                distancia = calc_distancia(coord, centroids[cont])
                if distancia < menor:
                    menor = distancia
                    index = cont

                cont += 1
            
            groups[index].append(coord)  # insere coordenada no seu devido grupo
            centroids[index] = calc_centroid(groups[index])   # atualiza o centroide do grupo que recebeu nova coordenada
        
        if past_centroids == centroids:   # verificar se houve mudanças nos centroides
            relocations = False
        else:
            past_centroids = centroids[:]
        
    #print(f"Centroides finais: {centroids}\n")
    return groups

def main():
    k = 3   # quantidade de clusters
    data = read_file("data_ex2.txt")   # nome do arquivo como argumento
        
    groups = k_means(data, k)

    for i in range(k):
        print(f"\nCluster {i+1}: \n{groups[i]}\n")
    
main()