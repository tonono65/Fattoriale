# -*- coding: utf-8 -*-
"""
Created on Wed Apr  11 

@author: Alessandro Minazzato
"""

#-------------------------------------------------------------------------------


# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

import sys
import time
from logPython import *

sys.setrecursionlimit(10**6)

INDEBUG = False
TRACE = True


if INDEBUG:
    print("")
    print("")
    print("*********************** IN DEBUG ***********************************")
    print("*********************** IN DEBUG ***********************************")
    print("*********************** IN DEBUG ***********************************")
    print("")
    print("")
    

def main():
    logMe("\r\n" * 5)       
    logMe(("\r\n*********************** IN DEBUG **************************************************** INIZIO LOG  " + time.strftime("%H:%M:%S") + "  *****************************")*5)

    
    #input dell'intero per cui calcolare il fattoirale
    fattoriale = int(input("Numero di cui calcolare il fattoriale: "))
    
    #Rilevo il tempo di inizio elaborazione
    t0 = time.time()
    t0_localtime = time.localtime(t0)
    t0_str = time.strftime("%d-%m-%Y, %H:%M:%S", t0_localtime)
    
    #inizializzo valiabili
    fattorialeRisultatoStr = "1"
    contaZeriTotale = 0
    
    #ciclo moltiplicazione fattori - i = moltiplicatore
    for i in range(2, fattoriale + 1,1):
        #se i è divisibile per 10 elimino gli zeri a dx e li aggiungo agli zeri totali
        if i % 10 == 0:
            zeriMoltiplicatore = len(str(i))-len(str(i).rstrip("0"))
            contaZeriTotale += zeriMoltiplicatore
        #stampo ogni 250 moltiplicatori per controllo avanzamento
        if TRACE:
            if i % 500 == 0:
                print(i)
        # i diventa i senza gli zeri a dx
        i = int(str(i).rstrip("0"))

                #ciclo di calcolo
        fattorialeRisultatoStr,  zeriRisultato = moltiplica(fattorialeRisultatoStr,str(i))         
        contaZeriTotale += zeriRisultato
    
    #Aggiungo una stringa di (contaZeriTotale)zeri a fattorialerisulatoStr
    primaCifraSignificativa = fattorialeRisultatoStr[-1]
    fattorialeRisultatoStr = fattorialeRisultatoStr + "0" * contaZeriTotale
    print(fattoriale,"! = ", fattorialeRisultatoStr)
    print("Lunghezza stringa di ",fattoriale,"! = ", len(fattorialeRisultatoStr))
    print("Numero zeri finali        : " + str(contaZeriTotale))
    print("Prima cifra significativa : " + primaCifraSignificativa)
    

    #Rilevo il tempo di fine elaborazione
    t1 = time.time()
    t1_localtime = time.localtime(t1)
    t1_str = time.strftime("%d-%m-%Y, %H:%M:%S", t1_localtime)
    
    ore = int((t1-t0) // 3600)
    minuti = int(((t1 - t0) - ore * 3600) // 60)
    secondi = (t1 - t0) - ore * 3600 - minuti * 60 
    
    logMe(str(fattoriale) + "! = " + fattorialeRisultatoStr)
    logMe("\r\n" * 2)
    logMe("Lunghezza stringa di " + str(fattoriale) + "! = " + str(len(fattorialeRisultatoStr)))
    logMe("\r\n")
    logMe("Numero zeri finali        : " + str(contaZeriTotale))
    logMe("Prima cifra significativa : i : " + primaCifraSignificativa)
    logMe("\r\n" * 2)
    logMe("Tempo inizio: " + t0_str)    
    logMe("Tempo fine  : " + t1_str)
    
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
    # perche' intuitivamente mm << 100)
    colonneMatrice = len(strMoltiplicando) + len(strMoltiplicatore)


    #inizializzo la matrice righeMatrice * colonneMatrice con tutti 0
    matrice = [
                [0 for x in range(colonneMatrice)]
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
        resto = 0
        for j in range(-1, -len(strMoltiplicando) - 1, -1 ):
            matrice[2+i][-i+j] += ( matrice[0][j] * matrice[1][-i-1] + resto) % 10
            #metto il resto che avanza dopo l'ultima moltiplicazione
            #della cifra del moltiplicando nella posizione -i+j-1
            matrice[2+i][-i+j-1] += ( matrice[0][j] * matrice[1][-i-1] + resto) // 10
        
        
    #calcolo del risultato finale
    #somma delle righe della matrice con i risultati intermedi
    resto = 0
    
    for j in range(-1, -colonneMatrice -1, -1):
        sommaAddendi = 0
        for i in range(len(strMoltiplicatore)):
            sommaAddendi =  sommaAddendi + matrice[2+i][j]
        matrice[righeMatrice - 1][j] = (sommaAddendi + resto ) % 10
        resto = (sommaAddendi + resto) // 10
        risultato = "".join(map(str, matrice[righeMatrice -1]))
        
    # Rimuovi gli "0" a sx di risultato
    stringaRisultatoSenzaZeriSx = risultato.lstrip("0")
    
    # Rimuovi gli "0" a dx di stringaRisultatoSenzaZeriSxe salvo gli zeri a dx in contaZeri
    stringaRisultatoSenzaZeriSxDx = stringaRisultatoSenzaZeriSx.rstrip("0")
    contaZeri = len(stringaRisultatoSenzaZeriSx) - len( stringaRisultatoSenzaZeriSxDx)
    
    # Assegno la stringa senza zeri a sx e a dx a risultati[0] e contaZeri a risultati[1]
    risultati = (stringaRisultatoSenzaZeriSxDx,  contaZeri)
    
    
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
    
    
    #restituisco risultati[]
    return(risultati)

if __name__ == "__main__":
    # execute only if run as a script
    main()
