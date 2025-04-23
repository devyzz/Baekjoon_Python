# Given the amount of a purchase (1 ≤ P ≤ 99) in cents, determine the way to make "change for a dollar" for that purchase.
# Use four standard US coin denominations: 1, 5, 10, and 25. The way to make change uses the least number coins.

p = int(input())
change = 100 - p
cents = [25, 10, 5, 1]
answer = []

for cent in cents:
    if change >= cent:
        answer.append(str(change // cent))
        change = change % cent
    else:
        answer.append('0')

print(" ".join(answer))