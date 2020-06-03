import random

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
    sum_x = sum_y = 0
    size  = len(group)

    for x,y in group:
        sum_x += x
        sum_y += y

    return (sum_x/size, sum_y/size)

def k_means(data, k):
    centroids = inicial_centroids(data[:], k)
    print(f"\nCentroides iniciais: {centroids}\n")
  
    past_centroids = [None]*k   # centroids de uma iteracao anterior
    
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
            past_centroids = centroids
        
    return groups

def main():
    # por enquanto os dados sao constantes
    # para fins de teste
    data = [(1.0,1.0), (1.5,2.0), (3.0,4.0), (5.0,7.0),
            (3.5,5.0), (4.5,5.0), (3.5,4.5)]
    k = 2
    groups = k_means(data, k)

    for i in range(k):
        print(f"Cluster {i+1}:",groups[i])

main()