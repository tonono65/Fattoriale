# -*- coding: utf-8 -*-
"""
Created on Wed Oct  26 2022 
@author: Alessandro Minazzato
"""
# -----------------------------------------------------------------------------

import sys
# setting path
sys.path.append('d:/PROGETTI/Python/myLibraries')
from logPython import log_me
import time
from datetime import datetime

# ----------------COSTANTI ----------------------------------------------------

INDEBUG = False
TRACE = False

# intervallo per stampa risultati intermedi if TRACE
PASSO = 500
# definisco la base per la rappresentazione di moltiplicando e moltiplicatore 
# mille miliardi
BASE = 1000000000000                      



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


# ------------------ main -------------------------------------------------
def main():
    if INDEBUG:
        print("")
        print("*********************** IN DEBUG ***********************************")
        print("*********************** IN DEBUG ***********************************")
        print("*********************** IN DEBUG ***********************************")
        print("")
    log_me("****************************************************************************************" + "\n" +  
          "*********************** CALCOLO FATTORIA ***********************************************" + "\n" +
          "******************************************************************   ìnizio log " + time.strftime("%H:%M:%S") +
          "\n")

    # *************************************************************************
    # input dell'intero per cui calcolare il fattoirale

    fattoriale = int(input("Numero di cui calcolare il fattoriale: "))
    # *************************************************************************


    # Rilevo il tempo di inizio elaborazione
    t0 = time.time()
    t0_localtime = time.localtime(t0)
    t0_str = time.strftime("%d-%m-%Y, %H:%M:%S", t0_localtime)

    # *************************************************************************
    
    # dichiaro e inizializzo le valiabili
    fattorialeRisultato = [1]
    
    # ###################################################### #
    # Determino quanti fattori 5 ci sono nel fattoriale      # 
    # Moltiplicati per altrettanti fattori 2,                #
    # determinano gli zeri del fattoriale.                   # 
    # ###################################################### #
    
    contaCinque = conta_fattore_in_fattoriale(fattoriale, 5)
    contaZeriTotale = contaCinque
    
    if INDEBUG:
        print("numero di zeri finalei a dx del fattoriale: ", contaZeriTotale)
        
    
    # ###################################################### #
    #                      ciclo FOR                         # 
    # ###################################################### #
    for i in range(2, fattoriale + 1,1):
        
        # chiamata alla funzione moltiplica
        fattorialeRisultato = moltiplica(fattorialeRisultato, i, BASE)         
        
        # if TRACE stampo ogni PASSO moltiplicatori per controllo avanzamento
        if TRACE:
            if i % PASSO == 0:
                # Rilevo il tempo ad ogni stampa di TRACE
                t1 = time.time()
                t1_localtime = time.localtime(t1)
                t1_str = time.strftime("%d-%m-%Y, %H:%M:%S", t1_localtime)
                print("i: " + str(i) + "  " + t1_str + "\n")        
                log_me("i: " + str(i) + "  " + t1_str + "\n")        
            
      
        
    
    
    if INDEBUG:
        print("FattorialeRisultato: ", str(fattorialeRisultato))
        print("")
    
    fattorialeRisultatoStr = convertiBase10(fattorialeRisultato, BASE)
    
    # Rilevo la prima cifra significativa (a dx di fattorialerisulatoStr
    primaCifraSignificativa = fattorialeRisultatoStr.rstrip("0")[-1]
    

    #Rilevo il tempo di fine elaborazione
    t1 = time.time()
    t1_localtime = time.localtime(t1)
    t1_str = time.strftime("%d-%m-%Y, %H:%M:%S", t1_localtime)
    
    ore = int((t1-t0) // 3600)
    minuti = int(((t1 - t0) - ore * 3600) // 60)
    secondi = (t1 - t0) - ore * 3600 - minuti * 60 
    
    print("")
    print(fattoriale,"! = ", fattorialeRisultatoStr)
    print("Lunghezza stringa di ",fattoriale,"! = ", len(fattorialeRisultatoStr))
    print("Numero zeri finali        : " + str(contaZeriTotale))
    print("Prima cifra significativa : " + primaCifraSignificativa)
    print("Tempo di calcolo: " + str(ore) + " ore " + str(minuti) + " minuti " + str(secondi) + " secondi")

    log_me(str(fattoriale) + "! = " + fattorialeRisultatoStr + "\n")
    log_me("Lunghezza stringa di " + str(fattoriale) + "! = " + str(len(fattorialeRisultatoStr)) + "\n")
    log_me("Numero zeri finali        : " + str(contaZeriTotale) + "\n")
    log_me("Prima cifra significativa : " + primaCifraSignificativa + "\n")
    log_me("Inizio elaborazione: " + t0_str)    
    log_me("Fine elaborazione  : " + t1_str)
    
    log_me("Tempo di calcolo del fattoriale di " + str(fattoriale) +"!: " 
          + str(ore) + " ore " + str(minuti) + " minuti " + str(secondi) + " secondi")



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

    
    # predispongo matrice[2] come riga dei risultati
    matrice.append([])
    
    # azzero la variabile che contiene il resto delle moltiplicazioni
    restoMoltiplicazione = 0
    
    # ciclo della moltiplicazione
    # si noti che sia in matrice[0] (moltiplicandoi sia in matrice[2] (risultati), 
    # i risultati vanno da sx a dx:
    # nelle colonna [j] c'è il valore da moltiplicare per base**j
    for j in range(len(Moltiplicando)):
        valore_prodotto = matrice[0][j] * Moltiplicatore  + restoMoltiplicazione
        matrice[2].append(valore_prodotto % base)
        restoMoltiplicazione = valore_prodotto // base
    
    # gestisco  il resto che avanza dopo l'ultima moltiplicazione
    #della cifra del moltiplicando nelle posizioni successive alla posizione j
    while restoMoltiplicazione > 0:
        matrice[2].append(restoMoltiplicazione % base)
        restoMoltiplicazione = restoMoltiplicazione // base  
     
    if INDEBUG:
        print("Matrice [2]  : ", str(matrice[2]))
        print("")
    
    # restituisco matrice[2]
    return(matrice[2])


def convertiBase10(vettoreInt, base):
    numeroBase10 = 0
    if INDEBUG:
        print("len(vettoreINT): ", len(vettoreInt))
        
    for i in range (len(vettoreInt)):
            if INDEBUG:
                print("i: ", i, "   vettore[i]: ", str(vettoreInt[i]))
            numeroBase10 += vettoreInt[i]*(base**i)
    if INDEBUG:
        print("numeroBase10: ", numeroBase10)
        
    return(str(numeroBase10))
            


if __name__ == "__main__":
    # execute only if run as a script
    main()
