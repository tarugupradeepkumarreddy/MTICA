def gen__int(n):
    for i in range(n):
        yield i
def gen__2(gen):
    for n in gen :
        if n%2:
            yield n
for i in gen__2(gen__int(10)):
    print(i)






















