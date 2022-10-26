# -*- coding: utf-8 -*-
"""
Created on Tued Oct 26 2022 
@author: Alessandro Minazzato
"""
# -----------------------------------------------------------------------------

import sys
# setting path
sys.path.append('d:/PROGETTI/Python/myLibraries')
from logPython import log_me, logMe

# ----------------COSTANTI ----------------------------------------------------

INDEBUG = True
TRACE = True


# ------------------ conta_fattore_in_fattoriale -----------------------------

def conta_fattore_in_fattoriale(fattoriale, fattore):
    """
     Si usa per determinare quanti fattori 5 ci sono nel fattoriale       
     Moltiplicati per altrettanti fattori 2, determinano gli zeri del fattoriale.                    
    """
    conta_fattore = 0

    if fattoriale <= 0:
        print("fattore incongrunete - deve essere > 0")
    else:
        i = fattoriale
        while i >= fattore:
            conta_fattore += i // fattore
            # conta quante volte fattore sta in fattoriale
            i = i // fattore
            # conta quante volte fattore sta in fattoriale/fattore         (es-1000 / 5 = 200)
            # così facendo conta quante colte fattore ^2 sta in fattoriale (es. 200 / 5 = 40)
            # quante colte fattore ^ 3 sta in fattoriale e così via        (es. 40 / 5 = 8)
            # quante colte fattore ^ 4 sta in fattoriale e così via        (es.  8 / 5 = 1)
            # fino a che i non diventa < di fattoriale                     i = 1 che è < 5   
        # end while
    # end else
    return conta_fattore



# ------------------ conta_fattore_in_fattoriale -----------------------------
def moltiplica(Moltiplicando, Moltiplicatore, base):
    
    
    if INDEBUG:
        print("Moltiplicando: ", str(Moltiplicando))
        print("Moltiplicatore: ", str(Moltiplicatore))
        log_me("Moltiplicando: " + str(Moltiplicando))
        log_me("Moltiplicatore: " + str(Moltiplicatore))

    
    
    #inizializzo la matrice che conterrà 
    # moltiplicando, moltiplicatore e risultati
    matrice = []

    # inserisco il moltiplicando in matrice[0]
    # si noti che i risultati vanno da sx a dx:
    # nelle colonna [j] c'è il valore da moltiplicare per base**j
    
    matrice.append(Moltiplicando)
    
    if INDEBUG:
        print("Moltiplicando: ", str(Moltiplicando))
        print("Matrice [0]  : ", str(matrice[0]))

   # inserisco il moltiplicatore in matrice[1]
    matrice.append(Moltiplicatore)
    
    if INDEBUG:
        print("Moltiplicatore: ", str(Moltiplicatore))
        print("Matrice [1]  : ", str(matrice[1]))

    
    # predispongo matrice[2] come riga dei riusltati
    matrice.append([])
    
    # azzero la variabile che contiene il resto delle moltiplicazioni
    restoMoltiplicazione = 0
    
    # ciclo della moltiplicazione
    # si noti che i risultati vanno da sx a dx:
    # nelle colonna [j] c'è il valore da moltiplicare per base**j
    for j in range(len(Moltiplicando)):
        if (matrice[0][j] + restoMoltiplicazione) == 0:
            matrice[2].append(0)
            continue
        else:
            valore_prodotto = matrice[0][j] * Moltiplicatore  + restoMoltiplicazione
            matrice[2].append(valore_prodotto % base)
            restoMoltiplicazione = valore_prodotto // base
        
        # gestisco  il resto che avanza dopo l'ultima moltiplicazione
        #della cifra del moltiplicando nelle posizioni successive alla posizione j
        while restoMoltiplicazione > 0:
            matrice[2].append(restoMoltiplicazione % base)
            restoMoltiplicazione = restoMoltiplicazione // base

        
  
        
    # restituisco matrice[2]
    return(matrice[2])
    
if __name__ == "__main__":
    result = moltiplica([0, 5], 20, 10)
    print("50 * 20", result)

    result = moltiplica([0, 0, 5], 23, 10)
    print("500 * 23", result)
