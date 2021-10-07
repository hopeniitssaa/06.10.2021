matrice=[]
n=int(input('introdu numarul de linii (2<=n<=10):'))
if ((n>=2)and(n<=10)):
    print("introdu elementele matricei:")
    for linie in range(0,n):
        linie=[]
        for element in range(0,n):
            element=int(input())
            linie.append(element)
        matrice.append(linie)
    print(matrice)
    diag_princ=[]
    diag_sec=[]
    msus_princ=[]
    mjos_princ=[]
    msus_sec=[]
    mjos_sec=[]
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i==j:
                diag_princ.append(matrice[i][j])
            if(i+j)==(len(matrice)-1):
                diag_sec.append(matrice[i][j])
            if i<j:
                msus_princ.append(matrice[i][j])
            if i>j:
                mjos_princ.append(matrice[i][j])
            if (i+j)<(len(matrice)-1):
                msus_sec.append(matrice[i][j])
            if (i+j)>(len(matrice)-1):
                mjos_sec.append(matrice[i][j])       
print('Suma elementelor diagonalei principale=', sum(diag_princ))
print('Suma elementelor diagonalei secundare=', sum(diag_sec))
print('Suma elementelor aflate mai sus de diagonala principala=', sum(msus_princ))
print('Suma elementelor aflate mai jos de diagonala principala ', sum(mjos_princ))
print('Suma elementelor aflate mai sus de diagonala secundara=',sum(msus_sec))
print('Suma elementelor aflate mai jos de diagonala secundara=', sum(mjos_sec))