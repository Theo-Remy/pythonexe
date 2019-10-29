def position(c,seq):
    if seq.count(c)!=0:
        return True
    else:
        return False

sequence = input('entrer la sequence du suspect : ')
brin1= input("entrer le premier brin d'adn : ")
brin2= input("entrer le second brin d'adn : ")

test1 = position(brin1,sequence)
test2 = position(brin2,sequence)

if test1==test2:
    print("c'est le coupable !")
else :
    print("ce n'est pas le coupable !")