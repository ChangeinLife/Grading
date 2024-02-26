
T1 = int(input("Score Test #1:  "))
T2 = int(input("Score Test #2:  "))
T3 = int(input("Score Test #3:  "))
T4 = int(input("Score Test #4:  "))
T5 = int(input("Score Test #5:  "))

scores = [T1, T2, T3, T4, T5]
print (scores)
100
print(min(scores))
scores.remove(min(scores))
# scores.remove(lowestgrade(scores))
print (scores)


