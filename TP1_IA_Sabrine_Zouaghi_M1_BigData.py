#Importation des bibliothèques necessaires
import time
import random

def successors(s):
    # changer le joueur
    player = s[-1]
    piles = s[0]
    successor_states = []
    successors = []
    new_piles = piles
    if player == 1:
        player = 2
    if player == 2:
        player == 1
    # parcourir les listes de listes pour verifier que la liste finale ne contient que 1 ou 2
    for i, pile in enumerate(piles):
        if pile < 3 :
            j = 1
        else :
            ran = round(pile/2)
            for remove in [1, ran]:
                    result = pile - remove
                    if result != 0:
                        next_piles = sorted(piles[:i] + [result] + piles[i+1:])
                    else:
                        next_piles = sorted(piles[:i] + piles[i+1:])
                    next_piles.append(remove)
                    successor_states.append(next_piles)

    import itertools
    successor_states.sort()
    successor_states = list(successor_states for successor_states, _ in itertools.groupby(successor_states))
    for i in range(len(successor_states)):
        successors.append([successor_states[i], player])
    return successors

# VERIFIER SI ON EST DANS L'ACTION FINALE OU BIEN ON PEUT JOUER ENCORE
def terminal_test(state):
    terminal_state = False
    for i in state[0] :
        if i < 3: # IL FAUT QUE TOUS LES ELEMENTS DE LA PILE < 3 POUR QU'ON S'ARRÊTE
            terminal_state = True
    return terminal_state


def utility_test(state):
    for i in state[0] :
        if i < 3 :
            utility = 1
        else:
            utility = -1
    return utility


def max_value(max_state):
    v = 1
    terminal_state, utility = terminal_test(max_state)
    if not terminal_state:
        for s in successors(max_state):
            v = min(v, min_value(s))
        return v
    else:
        return terminal_test(max_state)


def min_value(min_state):
    v = -1
    terminal_state, utility = terminal_test(min_state)
    if not terminal_state:
        for s in successors(min_state):
            v = max(v, max_value(s))
        return v
    else:
        return terminal_test(min_state)

def min_max(state):
    if state[1] == 1:
        utility = max_value(state)
    else:
        utility = min_value(state)
    if utility == 1:
        print("Max")
    if utility == -1:
        print("Min")
    return utility


def max_value_ab(min_state, a, b):
    v = 1
    terminal_state = terminal_test(min_state)
    utility = utility_test(min_state)
    if not terminal_state:

        for s in successors(min_state):

            if v > utility:
                utility = v
            if v >= b:
                return utility
            if v > a:
                a = v
        v = min(v, min_value_ab(min_state, a, b))
    return utility


def min_value_ab(max_state, a, b):
    v = -1
    terminal_state = terminal_test(max_state)
    utility = utility_test(max_state)
    if not terminal_state:

        for s in successors(max_state):

            if v < utility:
                utility = v
            if v <= a:
                return utility
            if v < b:
                b = v
        v = max(v, max_value_ab(max_state, a, b))
    return utility


def minimax_ab(state):
    start = time.time()
    alpha = 0
    beta = 0
    if state[1] == 1:
        utility_value = min_value_ab(state, alpha, beta)
    else:
        utility_value = max_value_ab(state, alpha, beta)
    end = time.time()
    print("Machine en reflexion...")
    print("Time taken in seconds: ", end - start)
    return utility_value


def game():
    print(" ********** Let's Play ************ ")
    number_of_piles = int("1")
    print(" Donner le nombre de Jetons pour commencer le jeu ")
    maximum_pile_size = int(input("Nombre de Jetons: n =  "))
    print(" Qui voulez-vous commencer ?")
    print(" Si vous voulez commencer choisissez  2 sinon choisissez 1 pour que la machine commence à jouer ")
    print(" IMORTANT : L'indice des piles commence toujours par 1  !! ")
    first_player = int(input(" Le Premier Joueur est : "))
    initial_piles = []
    for pile in range(0, number_of_piles):
        pile_size = maximum_pile_size
        initial_piles.append(pile_size)
    state = (initial_piles, first_player)
    while True:
        # Print game state
        if state[1] == 2:
            player = "Joueur"
        else:
            player = "Machine"
        print(" ************** C'est le tour de ", player," **************")
        print(" La pile est : ", state[0])
        if state[1] == 2:
            piles = state[0]
            pile_number = (int(input("Donner l'indice de la pile ci-dessus que vous allez diviser: ")) - 1)
            pile = piles[pile_number]
            while True :
                pick = int(input("Nombre de jetons a déplacer sans dépasser la moitié : "))
                if (pile%2==0):
                    ran = pile//2
                else:
                    ran=(pile+1)//2
                if pick < ran:
                    piles[pile_number] = pile - pick
                    piles.append(pick)
                    state = (piles, 1)
                    break
                else:
                    print(" ERRUR !! choisir un autre nombre :")
        elif state[1] == 1:
            list_of_successors = successors(state)
            number_of_next_states = len(list_of_successors)
            for s, next_state in enumerate(list_of_successors):
                utility_value = minimax_ab(next_state)
                if utility_value == -1:
                    state = next_state
                elif utility_value == 1:
                    state = list_of_successors[random.randrange(0, number_of_next_states)]
                    state = next_state
        ending = 1
        for j in state[0]:
            if j > 2 :
                ending = 0
        if ending == 1 :
            util = utility_test(state)
            if util == -1:
                print("Gagant : ",player)
                break
            elif util == 1:
                print("Gagnant : ",player)
                break
    print("****** Game over *******")
game()
