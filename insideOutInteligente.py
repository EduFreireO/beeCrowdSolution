n = int(input())
for c in range(0,n):
    string = input()
    string2 = string[0:len(string)//2]
    string2 = string2[::-1]
    string3 = string[len(string)//2:]
    string3 = string3[::-1]
    print(string2+string3)