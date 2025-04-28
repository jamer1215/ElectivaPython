   

def powTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


print("usando generadores: ")
for value in powTwoGen(5):
    print(value)


