#Atcoder Beginner`s

s = input()
token = s.split()
b = int(tokens[0])
c = int(token[1])


a,b = map(int, input().split())

if a*b%2==0:
    print('Even')
else:
    print('odd')