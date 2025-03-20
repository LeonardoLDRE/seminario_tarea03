def merge(l1, l2):
    r, i, j = [], 0, 0  
    while i < len(l1) and j < len(l2):  
        if l1[i].lower() < l2[j].lower():  
            r.append(l1[i])  
            i += 1  
        else:
            r.append(l2[j])  
            j += 1 
    return r + l1[i:] + l2[j:]  
print(merge(["ADAPTADOR", "USB", "TECLADO"], ["MEMORIA", "MOUSE", "IMPRESORA"]))
