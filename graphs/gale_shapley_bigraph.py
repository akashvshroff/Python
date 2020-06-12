def stableMatching(n, menPreferences, womenPreferences):
    '''
    Finds the stable match in any bipartite graph, i.e a pairing where no 2 objects prefer each other over their partner.
    Here marriage is used to make the variable names easier and so the algorithm can be intuitively understood.
    The function accepts the preferences of the men and women (where both are named from 0 to n-1) and returns a list where index
    position corresponds to the man and value at the index is the woman he is marrying.
    E.g:
    n = 4
    menPreferences = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    womenPreferences = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    >>>print(stableMatching(n,menPreferences,womenPreferences))
    [1,2,3,0]
    P.S: Marriages are heterosexual since it is a bipartite graph where there must be 2 distinct sets of objects to be matched - i.e
    patients and organ donors.
    To better understand the algorithm, see also:
    https://github.com/akashvshroff/Gale_Shapley_Stable_Matching (Detailed README).
    https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s (Numberphile YouTube Video).
    '''
    unmarriedMen = [i for i in range(n)]
    manSpouse = [None for i in range(n)]
    womanSpouse = [None for i in range(n)]
    nextManChoice = [0 for i in range(n)]
    while unmarriedMen:
        man = unmarriedMen[0]
        his_preferences = menPreferences[man]
        woman = his_preferences[nextManChoice[man]]
        nextManChoice[man] += 1
        her_preferences = womenPreferences[woman]
        husb = womanSpouse[woman]
        if husb != None:
            if her_preferences.index(husb) > her_preferences.index(man):
                womanSpouse[woman], manSpouse[man] = man, woman
                unmarriedMen.append(husb)
                unmarriedMen.remove(man)
        else:
            womanSpouse[woman], manSpouse[man] = man, woman
            unmarriedMen.remove(man)
    return manSpouse
