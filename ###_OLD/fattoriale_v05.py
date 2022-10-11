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
    
    # dichiaro e inizializzo le valiabili
    fattorialeRisultatoStr = "1"
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
            fattorialeRisultatoStr = moltiplica(fattorialeRisultatoStr,str(i))         
    
    # Rilevo la prima cifra significativa (a dx di fattorialerisulatoStr
    primaCifraSignificativa = fattorialeRisultatoStr[-1]
    # Aggiungo una stringa di contaZeriTotale zeri a fattorialerisulatoStr
    fattorialeRisultatoStr = fattorialeRisultatoStr + "0" * contaZeriTotale
    

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



def moltiplica(strMoltiplicando, strMoltiplicatore):
    
    #inizializzo lista dei risultati: la stringa con il fattoriale (senza zeri a dx)  
    # e l'intero con il numerozeri degli zeri a dx
    risultati = ["",0]
    

    #se il moltiplicatore ha piu' cifre del moltiplicando li scambio
    if INDEBUG:
        print("strMoltiplicando: ", strMoltiplicando)
        print("strMoltiplicatore: ", strMoltiplicatore)
        logMe("strMoltiplicando: " + strMoltiplicando)
        logMe("strMoltiplicatore: " + strMoltiplicatore)

    
    
    #calcolo le righe della matrice
    # le righe sono:
    # - 2 per moltiplicando e moltiplicatore
    # - len(moltiplicatore) per i risultati intermedi del calcolo
    # - 1 per il risultato finale
    
    righeMatrice=len(strMoltiplicatore) + 3

    #calcolo le colonne della matrice ( nnn * mm ha sempre meno di nnnmm cifre -
    # perché, intuitivamente, mm << 100)
    
    colonneMatrice = len(strMoltiplicando) + len(strMoltiplicatore)


    #inizializzo la matrice righeMatrice * colonneMatrice con tutti 0
    
    matrice = [[0 for x in range(colonneMatrice)]
                  for y in range(righeMatrice)]

    # inserisco l'int dei digit di moltiplicando in matrice[0]
    # allineo il numero nelle colonne a dx


    for i in range(-1, -len(strMoltiplicando)-1, -1):
        matrice[0][i] = int(strMoltiplicando[i])

    
   # inserisco l'int dei digit di moltiplicatore in matrice[1]
   # allineo il numero nelle colonne a dx
    
    for i in range(-1, -len(strMoltiplicatore)-1, -1):
        matrice[1][i] = int(strMoltiplicatore[i])

    # calcolo dei risultati intermedi
    #sono tante righe quante sono le cifre del moltiplicatore
   
    for i in range(len(strMoltiplicatore) ):
        restoMoltiplicazione = 0
        for j in range(-1, -len(strMoltiplicando) - 1, -1 ):
            matrice[2+i][-i+j] += ( matrice[0][j] * matrice[1][-i-1] + restoMoltiplicazione) % 10
    
            # metto il resto che avanza dopo l'ultima moltiplicazione
            #della cifra del moltiplicando nella posizione -i+j-1
    
            matrice[2+i][-i+j-1] += ( matrice[0][j] * matrice[1][-i-1] + restoMoltiplicazione) // 10
        
        
    # calcolo del risultato finale
    # somma delle righe della matrice con i risultati intermedi
    
    restoAddizione = 0
    for j in range(-1, -colonneMatrice -1, -1):
        sommaAddendi = 0
        for i in range(len(strMoltiplicatore)):
            sommaAddendi =  sommaAddendi + matrice[2+i][j]
        matrice[righeMatrice - 1][j] = (sommaAddendi + restoAddizione ) % 10
        restoAddizione = (sommaAddendi + restoAddizione) // 10
        risultato = "".join(map(str, matrice[righeMatrice -1]))
        
    # Rimuovi gli "0" a sx di risultato
    stringaRisultatoSenzaZeriSx = risultato.lstrip("0")
    stringaRisultatoSenzaZeriSxDx = stringaRisultatoSenzaZeriSx.rstrip("0")
    
        
    if INDEBUG:
        print("risultato: ", risultato)
        print("stringaRisultatoSenzaZeri a Sx        : " , stringaRisultatoSenzaZeriSx)
        print("stringaRisultatoSenzaZeri a Sx e a Dx : " , stringaRisultatoSenzaZeriSxDx)
        print("Conta zeri a sx                       : " , contaZeri)
        logMe("risultato: " + risultato)
        logMe("stringaRisultatoSenzaZeri a Sx        : " + stringaRisultatoSenzaZeriSx)
        logMe("stringaRisultatoSenzaZeri a Sx e a Dx : " + stringaRisultatoSenzaZeriSxDx)
        logMe("Conta zeri a sx                       : " + str(contaZeri))
        
        for i in range (righeMatrice):
            print("i: ", i, "matrice[",i,"]: ", matrice[i])
        print("Risultato: ",matrice[righeMatrice -1][::-1])
        print(str(matrice[righeMatrice -1][::-1]))
    
    
    # restituisco stringaRisultatoSenzaZeriSxDx
    return(stringaRisultatoSenzaZeriSxDx)


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
