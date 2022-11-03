# -*- coding: utf-8 -*-
"""
Created on Wed Oct  26 2022 
@author: Alessandro Minazzato
"""
# -----------------------------------------------------------------------------

import sys
# setting path
sys.path.append('d:/PROGETTI/Python/myLibraries')
from logPython import log_me, logMe
from tools_fattoriale import conta_fattore_in_fattoriale, moltiplica, converti_in_base_10    
import time
from datetime import datetime

# ----------------COSTANTI ----------------------------------------------------

INDEBUG = False
TRACE = False

# intervallo per stampa risultati intermedi if TRACE
PASSO = 500

# definisco la base per la rappresentazione di moltiplicando e moltiplicatore 
# 1*10e64
BASE = 10000000000000000000000000000000000000000000000000000000000000000                      


# ------------------ main -------------------------------------------------
def main():
    print("\n" * 3)
    print("****************************************************************************************" + "\n" +  
          "*********************** CALCOLO FATTORIA ***********************************************" + "\n" +
          "******************************************************************   ìnizio log " + time.strftime("%H:%M:%S") +
          "\n")
    log_me("****************************************************************************************" + "\n" +  
          "*********************** CALCOLO FATTORIA ***********************************************" + "\n" +
          "******************************************************************   ìnizio log " + time.strftime("%H:%M:%S") +
          "\n")

    
    # input dell'intero per cui calcolare il fattoirale
    fattoriale = int(input("Numero di cui calcolare il fattoriale: "))


    # Rilevo il tempo di inizio elaborazione
    t0 = time.time()
    t0_localtime = time.localtime(t0)
    t0_str = time.strftime("%d-%m-%Y, %H:%M:%S", t0_localtime)


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
        fattorialeRisultato = moltiplica(fattorialeRisultato, i, BASE, INDEBUG)         
        
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
    
    fattorialeRisultatoStr = converti_in_base_10(fattorialeRisultato, BASE, INDEBUG)
    
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
    log_me("Tempo di calcolo: " + str(ore) + " ore " + str(minuti) + " minuti " + str(secondi) + " secondi")





if __name__ == "__main__":
    # execute only if run as a script
    main()
