1212#-------------------------------------------------------------------------------
# Name:        modulo1
# Purpose:
#
# Author:      alessandro
#
# Created:     18/12/2016
# Copyright:   (c) alessandro 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    moltiplicando =     str(input("Moltiplicando:  "))
    moltiplicatore = str(input("Moltiplicatore: "))
    moltiplica(moltiplicando, moltiplicatore)

'''
    print("Moltiplicando:  ",moltiplicando)
    print("Moltiplicatore: ",moltiplicatore)
'''
    




def moltiplica(strMoltiplicando, strMoltiplicatore):

    #se il moltiplicatore ha piu' cifre del moltiplicando li scambio

    if(len(strMoltiplicatore) >  len(strMoltiplicando)):
        strComodo = strMoltiplicatore
        strMoltiplicatore = strMoltiplicando
        strMoltiplicando = strComodo

    #rovesciamo le stringhe in modo da avere le stringhe con le unita' in [0]
    #in pratica i numeri sono scritto da sx a dx2256
    strMoltiplicando = strMoltiplicando[::-1]
    strMoltiplicatore = strMoltiplicatore[::-1]

    #calcolo le righe della matrice
    # le righe sono:
    # - 2 per moltiplicando e moltiplicatore
    # - len(moltiplicatore) per i risultati intermedi del calcolo
    # - 1 per il risultato finale
    righeMatrice=len(strMoltiplicatore) + 3

    #calcolo le colonne della matrice ( nnn * mm ha sempre meno di nnnmm cifre -
    # perche' intuitivamente mm << 100)
    colonneMatrice = len(strMoltiplicando)+len(strMoltiplicatore)



    matrice = [
                [0 for x in range(colonneMatrice)]
                for y in range(righeMatrice)]

    #inserisco l'int dei digit di moltiplicando in matrice[0]
    # inserisco l'int dei digit di moltiplicatore in matrice[1]

    for i in range(len(strMoltiplicando)):
        matrice[0][i] = int(strMoltiplicando[i])
    for i in range(len(strMoltiplicatore)):
        matrice[1][i] = int(strMoltiplicatore[i])

    #calcolo dei risultati intermedi
    for i in range(len(strMoltiplicatore) ):
        resto = 0
        for j in range(len(strMoltiplicando) ):
            matrice[2+i][i+j] = ( matrice[0][j] * matrice[1][i] + resto) % 10
            resto = ( matrice[0][j] * matrice[1][i] + resto) // 10
        #metto il resto che avanza dopo l'ultima moltiplicazione 
        #della cifra del moltiplicando nella posizione i+j+1
        matrice[2+i][i+j+1] = resto

        #calcolo del risultato finale


    resto = 0
    for i in range(colonneMatrice):
        sommaAddendi = 0
        for j in range(len(strMoltiplicatore)):
            sommaAddendi =  sommaAddendi + matrice[2+j][i]
        matrice[righeMatrice - 1][i] = (sommaAddendi + resto ) % 10
        resto = sommaAddendi // 10

    for i in range (righeMatrice):
        print("i: ", i, "matrice[",i,"]: ", matrice[i])
    print("Risultato: ",matrice[righeMatrice -1][::-1])
    print(str(matrice[righeMatrice -1][::-1]))


"""



"""


if __name__ == '__main__':
    main()




