#names_test =  ["Аня", "Боря", "Вика"]
#scores_test = [7.0,   9.0,    9.0]

#python solution.py

def winner(names, scores):
    w, hs = None, 0
    i = 0
    for student in names:
        if max(scores[i],0)>hs:
            hs = scores[i]
            w = student
        i+=1
    return w

def average(scores):
    if len(scores)==0:
        return 0.0
    return round(abs(sum(scores))/len(scores), 2)

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


def does_nothing_a():
    print('fuck you')

def does_nothing_b():
    print('you should kill yourself NOW')

#print(ranking(names_test, scores_test))
