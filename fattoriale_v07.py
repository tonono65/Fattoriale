# -*- coding: utf-8 -*-
"""
Created on Wed Apr  11 
@author: Alessandro Minazzato
"""
# -----------------------------------------------------------------------------

import sys
# setting path
sys.path.append('d:/PROGETTI/Python/myLibraries')
from logPython import log_me, logMe
import time
from datetime import datetime
from tools_fattoriale import conta_fattore_in_fattoriale, INDEBUG, TRACE


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
    # definisco la base per la rappresentazione di moltiplicando e moltiplicatore 
    
    base = 1000000000
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
        
        #stampo ogni 500 moltiplicatori per controllo avanzamento
        if TRACE:
            if i % 500 == 0:
                # Rilevo il tempo ad ogni stampa di TRACE
                t1 = time.time()
                t1_localtime = time.localtime(t1)
                t1_str = time.strftime("%d-%m-%Y, %H:%M:%S", t1_localtime)
                print("i: " + str(i) + "  " + t1_str + "\n")        
                logMe("i: " + str(i) + "  " + t1_str + "\n")        
            
        # finché i è divisibile per 5 
        # totalizzo i fattori 5 in numerCinque e divido i per 5
        while i % 5 == 0:
            i = i // 5
            # finché ho capienza in contaCinque 
            # se i è divisibile per 2 lo divido per 2 
        while (i % 2 == 0) and (contaCinque > 0):
            i = i // 2
            contaCinque -= 1

        # chiamata alla funzione moltiplica se i <> 1
        if i != 1:
            fattorialeRisultato = moltiplica(fattorialeRisultato, i, base)         
    
    
    if INDEBUG:
        print("FattorialeRisultato: ",str(fattorialeRisultato))
        print("")
    
    fattorialeRisultatoStr = convertiBase10(fattorialeRisultato, base)
    
    # Aggiungo una stringa di contaZeriTotale zeri a fattorialerisulatoStr
    fattorialeRisultatoStr = fattorialeRisultatoStr + "0" * contaZeriTotale
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

    logMe(str(fattoriale) + "! = " + fattorialeRisultatoStr + "\n")
    logMe("Lunghezza stringa di " + str(fattoriale) + "! = " + str(len(fattorialeRisultatoStr)) + "\n")
    log_me("Numero zeri finali        : " + str(contaZeriTotale) + "\n")
    log_me("Prima cifra significativa : " + primaCifraSignificativa + "\n")
    log_me("Inizio elaborazione: " + t0_str)    
    log_me("Fine elaborazione  : " + t1_str)
    
    log_me("Tempo di calcolo del fattoriale di " + str(fattoriale) +"!: " 
          + str(ore) + " ore " + str(minuti) + " minuti " + str(secondi) + " secondi")




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
