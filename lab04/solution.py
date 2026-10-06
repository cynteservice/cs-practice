#names_test =  ["Аня", "Боря", "Вика"]
#scores_test = [7.0,   9.0,    9.0]

#python solution.py
import math

def winner(names, scores):
    w, hs = None, -1E+23
    i = 0
    for student in names:
        if scores[i]>hs:
            hs = scores[i]
            w = student
        i+=1
    return w

def average(scores):
    if len(scores)==0:
        return 0.0
    s = 0
    for i in scores:
        s += max(i,0)
    return round(s/len(scores), 2)

def ranking(names, scores):
    new_names = names.copy()
    return sorted(new_names, key=lambda n: -max(scores[names.index(n)],0))

def above_average(names, scores):
    new_names = []
    avg = average(scores)
    i = 0
    for student in names:
        if max(scores[i],0)>avg:
            new_names.append(student)
        i+=1
    return new_names


if __name__=='__main__':
    names_test =  ["Аня", "Боря", "Вика"]
    scores_test = [7.0,   9.0,    912312.0]
    print(winner(names_test, scores_test))
