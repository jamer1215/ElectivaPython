class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        resultado = 2 ** self.n
        self.n += 1
        return resultado
    


print("usando iterators: ")
powtwo1 = PowTwo(5)
powtwo1_iter = iter(powtwo1)

while True:
    try:
        print(next(powtwo1_iter))
    except StopIteration:
        print("concluyó el iterador powtwo1_iter")
        break



