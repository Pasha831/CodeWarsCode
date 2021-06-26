def scramble(s1, s2):
    if s1 == '' or s2 == '':
        return False

    '''
    is_true = True
    for i in range(len(s2)):
        if s2[i] == s2[i - 1] and i != 0:
            continue
        if s2.count(s2[i]) <= s1.count(s2[i]):
            continue
        else:
            is_true = False
    return is_true
    '''

    is_true = True
    alph2 = [0] * 26
    alph1 = [0] * 26

    for i in range(len(s2)):
        alph2[ord(s2[i]) - 97] += 1

    for i in range(len(s1)):
        alph1[ord(s1[i]) - 97] += 1

    for i in range(len(alph2)):
        if alph1[i] >= alph2[i]:
            continue
        else:
            is_true = False
            break

    return is_true



print(scramble('ccccodewars', 'ccccodewars'))