""" Write a python program to build a Rotate My Scores program using Python arrays/lists. They will reverse scores using two pointers, reverse elements in
fixed-size groups, perform left rotation by 1, perform left rotation by n, and find leaders in an array by scanning from the right side."""

scores = [25, 30, 49, 50, 72, 88, 76]

print(f"Original Scores: {scores}")

x = 0
y = len(scores) - 1

while x < y:
    scores[x], scores[y] = scores[y], scores[x]
    x+=1
    y-=1

print(f"Reversed: {scores}")
print()

print("Reverse In groups")

k = 4

for i in range(0, len(scores), k):
    scores[i:i+k] = scores[i:i+k][::-1]

print(f"After Reverse In Group: {scores}")
print()

print("Left Rotate by 1")

firstScore = scores[0]

for i in range(len(scores) - 1):
    scores[i] = scores[i + 1]

scores[-1] = firstScore

n = 3

print(f"Rotate by: {n}")

n = n % len(scores)

for j in range(n):
    firstScore = scores[0]

    for k in range(len(scores) - 1):
        scores[k] = scores[k + 1]

    scores[-1] = firstScore

print(f"After left rotate by {n}: {scores}")
print()

print("Leaders in an Array")

leaders = []

maxFromRight = scores[-1]
leaders.append(maxFromRight)

r = len(scores) - 2

while r >= 0:
    if scores[r] > maxFromRight:
        maxFromRight = scores[r]
        leaders.append(scores[r])

    r -= 1

leaders.reverse()

print(f"Leaders: {leaders}")