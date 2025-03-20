def merge(l1, l2):
    r, i, j = [], 0, 0  # Inicializa lista resultado y punteros i, j
    while i < len(l1) and j < len(l2):  # Mientras haya elementos en ambas listas
        if l1[i].lower() < l2[j].lower():  # Comparar sin distinguir mayúsculas
            r.append(l1[i])  # Agregar el menor
            i += 1  # Avanzar en l1
        else:
            r.append(l2[j])  # Agregar el menor
            j += 1  # Avanzar en l2
    return r + l1[i:] + l2[j:]  # Agregar elementos restantes
print(merge(["ADAPTADOR", "USB", "TECLADO"], ["MEMORIA", "MOUSE", "IMPRESORA"]))
