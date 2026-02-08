students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append((name, score))

# Get all unique scores and sort them
scores = sorted(set(score for name, score in students))

# Second lowest score
second_lowest = scores[1]

# Get names with second lowest score
names = sorted(name for name, score in students if score == second_lowest)

for n in names:
    print(n)
