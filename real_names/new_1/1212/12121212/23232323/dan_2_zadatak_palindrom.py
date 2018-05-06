#samo jedan string:

def palindrom(word):
    return word == word[::-1]

#ako je u pitanju recenica:

from collections import deque
def palindrom_recenica(word):
    dq = deque(word)
    while dq.__len__()!= 0:
        if dq.pop() != dq.popleft():
            return False
        else: return True

print(palindrom_recenica('ana voli milovana'))
print(palindrom("sale"))

fix
fix
fix
fix
valuesv
fix
fix
valuesfix
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
[FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX][FIX]	[FIX]
>>>>>>> ff53f3d... [FIX][FIX] This is the common squished of ONE ONE TWO TWO THREE THREE
