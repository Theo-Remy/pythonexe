
def distance_hamming(m1,m2): #definition de la fonction avec deux variable
    difference=0 #variable comptant le nombre de lettre differente
    i=0 #compteur pour la boucle while
    while i< len(m1): #boucle while lier a la longueur du mot
        if m1[i] != m2[i]: #recherche de la difference de lettre
            difference=difference+1 #incrementation de la variable difference
        i=i+1 #incrementation du compteur
    return (difference) #la fonction renvoie le nombre de lettre differente

mot1=input('entrer un premier mot : ') #demande un premier mot a l'utilisateur
mot2=input('entrer un second mot de meme longueur : ') #demande un second mot de meme longueur a l'utilisateur
d=0 #variable pour le return de la fonction

if len(mot1) != len(mot2): #verification des longueur des deux mot
    print('erreur les deux mots a comparer ne sont pas de la meme longueur !')

else : #application de la fonction
    d=distance_hamming(mot1,mot2)
    print('la distance de hamming entre vos deux mots est de : ',d)