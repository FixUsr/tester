import time as t
tt = 0
start = t.time()
started = False
inputt = input
def input(*args, **kwarga):
    global tt
    startt = t.time()
    inp = inputt(*args, **kwarga)
    endd = t.time()
    tt += endd - startt
    return inp
def tester_end():
    end = t.time()
    print("running time:", end - start - tt)