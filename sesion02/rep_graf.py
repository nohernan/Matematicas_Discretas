mi_grafica = { "a" : ["b", "c","d"],
               "b" : ["a", "c"],
               "c" : ["a", "b"],
               "d" : ["a"],
               "e" : []
              }


def generar_aristas(grafica):
    aristas = []
    for v in grafica:
        for adyacente in grafica[v]:
            aristas.append({v, adyacente})

    return aristas

print(generar_aristas(mi_grafica))
