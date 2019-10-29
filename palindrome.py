
def palindrome(m): #definition de la fonction
    i=0 #definition d'un compteur
    longueur = len(m) #definition d'une variable contenant comme valeur la longueur du mot

    while i < longueur: #boucle while pour comparer les lettres du mot
        if m[i] != m[-i - 1]: #condition si la lettre egal a i est differente de la lettre opposer alors renvoie comme valeur false
            return False
        i += 1 #incrementation du compteur
    return True #si boucle while complete la fonction renvoi True

mot=input('entrer un mot : ') #demande un mot a l'utillisateur
if palindrome(mot): #test du mot dans la fonction palindrome definie plus haut
    print("Votre mot est un palindrome.") #si la fonction renvoie vrai alors on affiche que le mot est un palindrome
else: #sinon on affiche que le mot n'est pas un palindrome
    print("Votre mot n'est pas palindrome.")