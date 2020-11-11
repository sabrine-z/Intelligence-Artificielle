import matplotlib.pyplot as plt
def perceptron(w,x,y):
    #  VERIFIER QUE LES POIDS NE CHANGE PAS DE VALEUR A PARTIR D'UN CERTAIN NOMBRE D'ITERATION
    p=[] #UNE LISTE VIDE POUR ENREGISTRER LES VALEUR DES POIDS A CHAQUE BOUCLE ELLA A LA MEME TAILLE QUE LA LISTE DES POIDS W
    for m in range(len(x)):
        xi=x[m]
        s=0
        for i,j in zip(w,xi):
            s+=i*j
        o=int(s>0)
        p.append(o)
    print(" p : ",p)
    # ON A MIS UNE CONDITION D'ARRET Dés QUE LE p = AU NOMBRE DES ENTRES 'X' DU PERCEPTRON
    # c'est a dire il n’y a aucune modification des poids pour tous les entrees
    while(p!=y):
        for i in range(len(x)):
            xi=x[i]
            yi=y[i]
            s=0
            for k,j in zip(w,xi):
                s+=k*j
            o=int(s>0)
            if(o!=yi):
                for i in range(len(w)):
                    w[i]=w[i]+0.1*(yi-o)*xi[i]
            p[i]=o
        print(" p : ",p)
    return(w)

#############################    AND   #########################################

print(" *********** l'opérateur AND ************")
w=[0,1,2] # initialisation des poids
X=[[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
y_et=[0,0,0,1]
w_et=perceptron(w,X,y_et) # APPEL DE LA FONCTION
print(w_et)# AFFICHAHE
# PARTIE PRESENTATION GRAPHIQUE
plt.plot([0,0,1,1],[0,1,0,1],'ro')
plt.plot([None,1],'bs')
plt.plot([w_et[2],w_et[1]])
plt.show()
print(" ****************************************** \n")

#############################   OR  #################################

print(" *********** l'opérateur OR ************")
w=[0,1,2] # initialisation des poids
X=[[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
y_ou=[0,1,1,1]
w_ou=perceptron(w,X,y_ou) # APPEL DE LA FONCTION
print(w_ou) # AFFICHAHE
# PARTIE PRESENTATION GRAPHIQUE
plt.plot([0,0,1,1],[0,1,0,1],'ro')
plt.plot([0,None],'bs')
plt.plot([w_ou[2]-0.5,w_ou[1]-0.5])
plt.show()
print(" ****************************************** \n")


def mise_a_jour(w,xi,yi,o,o1,o2):
    # MISE A JOUR DES POIDS
    l=[]
    l.append(w[0]+(yi-o)*xi[0])
    l.append(w[1]+(yi-o)*xi[3])
    l.append(w[2]+(yi-o)*xi[4])
    l.append(w[3]+(yi-o)*xi[1])
    l.append(w[4]+(yi-o)*xi[3])
    l.append(w[5]+(yi-o)*xi[4])
    l.append(w[6]+(yi-o)*xi[2])
    l.append(w[7]+(yi-o)*o1)
    l.append(w[8]+(yi-o)*o2)
    return(l)


def perceptron_final(w,x,y):
    p=[]
    for m in range(len(x)):
        xi_1=[x[m][0],x[m][3],x[m][4]]
        s=0
        for i,j in zip(w[:3],xi_1):
            s+=i*j
        o1=int(s>0)
        # enregistrer les poids dans t[] pour la comparaison avec les poids apres mise a jour
        xi_2=[x[m][2],x[m][3],x[m][4]]
        s=0
        for i,j in zip(w[3:6],xi_2):
            # calcul de la sortie o
            s+=i*j
        o2=int(s>0)
        
        xi_3=[x[m][2],o1,o2]
        s=0
        for i,j in zip(w[6:],xi_3):
            s+=i*j
        o=int(s>0)
        p.append(o)
    print(" p : ",p)
    while(p!=y):
        for i in range(len(x)):
            xi_1=[x[i][0],x[i][3],x[i][4]]
            s=0
            for k,j in zip(w[:3],xi_1):
                s+=k*j
            o1=int(s>0)
            
            xi_2=xi_1=[x[i][1],x[i][3],x[i][4]]
            s=0
            for k,j in zip(w[3:6],xi_2):
                s+=k*j
            o2=int(s>0)
            
            xi_3=[-1,o1,o2]
            s=0
            for k,j in zip(w[6:],xi_3):
                s+=k*j
            o=int(s>0)
            yi=y[i]
            if(o!=yi):
                w=mise_a_jour(w,x[i],yi,o,o1,o2)
            p[i]=o
        print(" p : ",p)
    return(w)

############################   XOR  ##################################

print(" *********** l'opérateur XOR  *************")
w=[1,2,3,4,5,6,7,8,9]
X_xor=[[-1,-1,-1,0,0],[-1,-1,-1,0,1],[-1,-1,-1,-1,0],[-1,-1,-1,1,1]]
y_xor=[0,1,1,0]
w_xor=perceptron_final(w,X_xor,y_xor) # APPEL DE LA FONCTION
print(w_xor)# AFFICHAGE
# PARTIE PRESENTATION GRAPHIQUE
plt.plot([0,0,1,1],[0,1,0,1],'ro')
plt.plot([0,None],'bs')
plt.plot([None,1],'bs')
plt.plot([(w_xor[2]/2),(w_xor[1]/10)])
plt.plot([(w_xor[2]/2)+1,(w_xor[1]/10)+1])
plt.show()
print(" ****************************************** \n")