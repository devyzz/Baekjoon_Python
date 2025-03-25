# Input begins with a line containing an integer N (1 ≤ N ≤ 100).
# The next N lines each contain one estimated cost, which is an integer between 0 and 10100. (Some of the workmen overcharge quite a bit.)

# For each estimated cost, output the number of digits required to represent it.

N = int(input())
answer = ""
for i in range(N):
    cost = input()
    answer += (str(len(cost))+"\n")

print(answer)
