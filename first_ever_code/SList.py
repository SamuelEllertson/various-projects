def Slist(L):
    F = list(L)
    s = 0
    e = len(L) - 1
    for i in xrange(len(L)-1):
        for t in xrange(len(L)):
            c = L[t]
            for x in xrange(e - s + 1):
                b = F[s + x]
                if c not in b:
                    F.append(c + b)
        s = e + 1
        e = len(F) - 1
    return F

newlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
shortlist = ["A", "B", "C"]
onelist = ["A"]
abc = Slist(newlist)
print len(abc)

