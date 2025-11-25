while True:
    file_to_test = input("Write name of the file you want to test\n")
    try:
        with open(f"{file_to_test}", "r"): pass
    except:
        print(f"Incorrect input")
        continue
    break
import os
with open(f"{file_to_test}", "r") as f:
    file_text = f.read()
with open(f"tester_copy.py", "w") as f:
    f.write("import time as t\ntt = 0\nstart = t.time()\nstarted = False\ninputt = input\ndef input(*args, **kwarga):\n    global tt\n    startt = t.time()\n    inp = inputt(*args, **kwarga)\n    endd = t.time()\n    tt += endd - startt\n    return inp\ndef tester_end():\n    end = t.time()\n    print(\"running time:\", end - start - tt)")
with open("file_to_run.py", "w") as f:
    f.write(f"from tester_copy import *\n{file_text}\ntester_end()")
print("file started")
os.system(f"python file_to_run.py")
os.remove(f"tester_copy.py")
os.remove(f"file_to_run.py")
input()
