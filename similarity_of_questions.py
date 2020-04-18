import cosSim

name = "ExperiencesinCloseRelationshipsScale"
man = "Jeremy"

def gettingDic(dname):
    dic = {}
    with open("./data/{}.txt".format(dname), "r") as f:
        for n, question in enumerate(f):
            dic["Q"+dname[0]+str(n+1)] = cosSim.clean_string(question[:-1])
    return dic

def mostSimilar(similar):
    lKeys = {}
    first = ""
    for k, qt in similar.items():
        lowvalue = -0.01
        for qn, s in qt.items():
            if lowvalue < s:
                first = qn
                lowvalue = s

        lKeys[k] = first
    return lKeys


if __name__ == "__main__":
    similarity = {}
    Q = gettingDic(name)  #main personality questions
    Guy = gettingDic(man) #his own personality statements
    H = {**Q, **Guy} 
    vectH = cosSim.vectorize(H)
    vectQ = vectH[:len(Q)]
    vectGuy = vectH[len(Q):]
    for key1, question in Guy.items():
        n = list(Guy).index(key1)
        helper = {}
        for key2, question2 in Q.items():
            m = list(Q).index(key2)
            sim = cosSim.cosine_sim_vectors(vectGuy[n], vectQ[m])
            helper[key2] = sim
        similarity[key1] = helper
    matchingQuestion = mostSimilar(similarity)

    _file = open("{}_matched.txt".format(man), 'w')

    for guyq, mainq in matchingQuestion.items():
        print(mainq+'.', file = _file)
    _file.close()