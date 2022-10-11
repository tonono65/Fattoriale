# -*- coding: utf-8 -*-
"""
Created on Wed Apr  11 

@author: Alessandro Minazzato
"""
# -----------------------------------------------------------------------------

import time
from datetime import datetime


# ----------------COSTANTI ----------------------------------------------------

INDEBUG = False
TRACE = True


# ----------------COSTANTI ----------------------------------------------------
    

def main():
    if INDEBUG:
        print("")
        print("*********************** IN DEBUG ***********************************")
        print("*********************** IN DEBUG ***********************************")
        print("*********************** IN DEBUG ***********************************")
        print("")
    logMe("****************************************************************************************" + "\n" +  
          "*********************** CALCOLO FATTORIA ***********************************************" + "\n" +
          "******************************************************************   ìnizio log " + time.strftime("%H:%M:%S") +
          "\n")

    #input dell'intero per cui calcolare il fattoirale
    fattoriale = int(input("Numero di cui calcolare il fattoriale: "))
    
    #Rilevo il tempo di inizio elaborazione
    t0 = time.time()
    t0_localtime = time.localtime(t0)
    t0_str = time.strftime("%d-%m-%Y, %H:%M:%S", t0_localtime)

    # definisco la base per la rappresentazione di moltiplicando e moltiplicatore 
    base = 10000000
    
    # dichiaro e inizializzo le valiabili
    fattorialeRisultato = [1]
    contaZeriTotale = 0
    contaCinque = 0
    
    # ###################################################### #
    # Determino quanti fattori 5 ci sono nel fattoriale      # 
    # Moltiplicati per altrettanti fattori 2,               #
    # determinano gli zeri del fattoriale.                   # 
    # ###################################################### #
    contaCinque = 0
    
    i = fattoriale
    while i >= 5:
        contaCinque += i // 5
        i = i // 5
    
    contaZeriTotale = contaCinque
    
    if INDEBUG:
        print("numero di zeri finalei a dx del fattoriale: ", contaCinque)
        
    
    # ###################################################### #
    #                      ciclo FOR                         # 
    # ###################################################### #
    for i in range(2, fattoriale + 1,1):
        
        #stampo ogni 500 moltiplicatori per controllo avanzamento
        if TRACE:
            if i % 500 == 0:
              #Rilevo il tempo ad ogni stampa di TRACE
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
    logMe("Numero zeri finali        : " + str(contaZeriTotale) + "\n")
    logMe("Prima cifra significativa : " + primaCifraSignificativa + "\n")
    logMe("Inizio elaborazione: " + t0_str)    
    logMe("Fine elaborazione  : " + t1_str)
    
    logMe("Tempo di calcolo del fattoriale di " + str(fattoriale) +"!: " 
          + str(ore) + " ore " + str(minuti) + " minuti " + str(secondi) + " secondi")



def moltiplica(Moltiplicando, Moltiplicatore, base):
    
    
    if INDEBUG:
        print("Moltiplicando: ", str(Moltiplicando))
        print("Moltiplicatore: ", str(Moltiplicatore))
        logMe("Moltiplicando: " + str(Moltiplicando))
        logMe("Moltiplicatore: " + str(Moltiplicatore))

    
    
    #calcolo le righe della matrice
    # le righe sono:
    # - 2 per moltiplicando e moltiplicatore
    # - 1  per i risultati intermedi del calcolo
    
    
    righeMatrice = 3

    #calcolo le colonne della matrice ( nnn * mm ha sempre meno di nnnmm cifre -
    # perché, intuitivamente, mm << 100)
    
    colonneMatrice = len(Moltiplicando) + 1


    #inizializzo la matrice righeMatrice * colonneMatrice con tutti 0
    
    matrice = [[],[],[]]
    print ("************************************matrice: ")
    print ("matrice: ", str(matrice))
    print ("***********************************matrice: ")
    # inserisco l'int dei digit di moltiplicando in matrice[0]
    # allineo il numero nelle colonne a dx


    matrice[0].extend(Moltiplicando)
    
    if INDEBUG:
        print("Moltiplicando: ", str(Moltiplicando))
        print("Matrice [0]  : ", str(matrice[0]))

    
   # inserisco l'int dei digit di moltiplicatore in matrice[1]
   # allineo il numero nelle colonne a dx
    
    print(str(matrice))
    matrice[1].append(Moltiplicatore)
    if INDEBUG:
        print("Moltiplicatore: ", str(Moltiplicatore))
        print("Matrice [1]  : ", str(matrice[1]))

    
    # calcolo dei risultati intermedi
    #sono tante righe quante sono le cifre del moltiplicatore
   
    restoMoltiplicazione = 0
    
    for j in range(len(Moltiplicando)):
        matrice[2].append(( matrice[0][j] * matrice[1][0] + restoMoltiplicazione) % base)
        restoMoltiplicazione = ( matrice[0][j] * matrice[1][0] + restoMoltiplicazione) // base
        # metto il resto che avanza dopo l'ultima moltiplicazione
        #della cifra del moltiplicando nella posizione +j+1
    if restoMoltiplicazione != 0:
        matrice[2].append(restoMoltiplicazione)
        
  

    
        
    if INDEBUG:
        for i in range (righeMatrice):
            print("i: ", i, "matrice[",i,"]: ", matrice[i])
            print("Risultato: ",matrice[2])
    
    
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
            

def logMe(text, ritornaFileLog = False):
    if not hasattr(logMe, "logFilename"):
        logMe.logFilename = 'D:/LOG/PYTHON/' + datetime.now().strftime("%Y%m%d_%H%M%S_")+ 'LOG.TXT'
    try:
        logFile = open(logMe.logFilename, "a")
        try:
          # compose formatted msg
            logFile.write(str(text) + "\n")
        finally:
            logFile.close()
    except IOError:
        pass
    if ritornaFileLog:
        return logMe.logFilename


if __name__ == "__main__":
    # execute only if run as a script
    main()
