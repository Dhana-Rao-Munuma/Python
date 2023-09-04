scores = []
for i in range(3) :
    score = int(input("score:"))
    # scores.append (score)
    scores += [score]
avg = sum(scores) / len(scores)
print(avg)

"""
scores = [ 10, 20, 30, 45]
avg = sum(scores) / len(scores)
print(avg)
"""