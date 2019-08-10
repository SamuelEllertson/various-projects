def Rlist(L):
    n = len(L)
    if n > 2:
        U = []
        for i in xrange(0, len(L)):
            D = list(L)
            D.remove(L[i])
            W = Rlist(D)
            for t in xrange(0, len(W)):
                if len(W[t]) == (n-1):
                    U.append(L[i] + W[t])
                    if not W[t] in U:
                        U.append(W[t])
                else:
                    if not W[t] in U:
                        U.append(W[t])
        return U
    elif n == 2:
        U = list(L)
        U.append(L[0] + L[1])
        U.append(L[1] + L[0])
        return U
    else:
        return L


List = ["A", "B", "C", "D", "E", "F", "G", "H"]
newlist = Rlist(List)
print len(newlist)

