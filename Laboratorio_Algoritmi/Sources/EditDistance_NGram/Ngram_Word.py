def Ngram_Word(n_gram, word):
    seq = ''
    Q = []
    for j in range (0, len(word) - n_gram + 1):
        for i in range(0, n_gram):
            seq = seq + word[i+j]
        Q.append(seq)
        seq = ''
    return Q