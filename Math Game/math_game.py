import time
import random

opreators = ["*","+","-"]
max = 12
min = 3
total_op = 10

def generate():
    left= random.randint(min , max)
    right = random.randint(min, max)
    opreator = random.choice(opreators)

    exp = str(left) + " "+ opreator+" " +str(right)
    ans = eval(exp)
    return exp, ans

wrong = 0

input("Press enter to start.....")

stt = time.time()

for i in range (total_op):
    exp, ans =generate()
    while True:
        guess = input("Problem#"+ str(i+1)+":"+exp+"=")
        if guess == str(ans):
            break
        wrong +=1

sot= time.time()
tt= sot-stt
print("--------------------------------------")
print(f"You finished in {tt} seconds")
