import time
#Two players playing if more add few of classes
import random
class Shooter:
    total = 0
    print("Total is",total)
    time.sleep(1)
    rack1 = random.randrange(0, 7)
    print (rack1, "/6")
    total += rack1
    print("Total is",total)
    time.sleep(1)
    rack2 = random.randrange(0, 7)
    print (rack2, "/6")
    total += rack2
    print("Total is",total)
    time.sleep(1)
    rack2 = random.randrange(0, 7)
    print (rack2, "/6")
    total += rack2
    print("Total is",total)
    time.sleep(1)
    mdew_ball_right = random.randrange(1, 3)
    if mdew_ball_right == 1:
        deep_ball_right = 3
        total += deep_ball_right
        print (deep_ball_right, "/3")
        print("Total is",total)
    else:
        deep_ball_right = 0
        print (deep_ball_right, "/3")
        print("Total is",total)
    time.sleep(1)
    rack3 = random.randrange(0, 7)
    print (rack3, "/6")
    total += rack3
    print("Total is",total)
    time.sleep(1)
    mdew_ball_left = random.randrange(1, 3)
    if mdew_ball_left == 1:
        deep_ball_left = 3
        total += deep_ball_left
        print (deep_ball_left, "/3")
        print("Total is",total)
    else:
        deep_ball_left = 0
        print (deep_ball_left, "/3")
        print("Total is",total)
    time.sleep(1)
    rack4 = random.randrange(0, 7)
    print (rack4, "/6")
    total += rack4
    print("Total is",total)
    time.sleep(1)
    rack5 = random.randrange(0, 11)
    if (rack5 % 2) == 0:
        print (rack5, "/10")
    else:
        rack5 += 1
        print (rack5, "/10")
    total += rack5
    print("Total is",total)
p1 = Shooter
p1_total = Shooter.total
print("Player 1 total is", p1_total,"/40")
class Shooter2:
    total = 0
    print("Total is",total)
    time.sleep(1)
    rack1 = random.randrange(0, 7)
    print (rack1, "/6")
    total += rack1
    print("Total is",total)
    time.sleep(1)
    rack2 = random.randrange(0, 7)
    print (rack2, "/6")
    total += rack2
    print("Total is",total)
    time.sleep(1)
    rack2 = random.randrange(0, 7)
    print (rack2, "/6")
    total += rack2
    print("Total is",total)
    time.sleep(1)
    mdew_ball_right = random.randrange(1, 3)
    if mdew_ball_right == 1:
        deep_ball_right = 3
        total += deep_ball_right
        print (deep_ball_right, "/3")
        print("Total is",total)
    else:
        deep_ball_right = 0
        print (deep_ball_right, "/3")
        print("Total is",total)
    time.sleep(1)
    rack3 = random.randrange(0, 7)
    print (rack3, "/6")
    total += rack3
    print("Total is",total)
    time.sleep(1)
    mdew_ball_left = random.randrange(1, 3)
    if mdew_ball_left == 1:
        deep_ball_left = 3
        total += deep_ball_left
        print (deep_ball_left, "/3")
        print("Total is",total)
    else:
        deep_ball_left = 0
        print (deep_ball_left, "/3")
        print("Total is",total)
    time.sleep(1)
    rack4 = random.randrange(0, 7)
    print (rack4, "/6")
    total += rack4
    print("Total is",total)
    time.sleep(1)
    rack5 = random.randrange(0, 11)
    if (rack5 % 2) == 0:
        print (rack5, "/10")
    else:
        rack5 += 1
        print (rack5, "/10")
    total += rack5
    print("Total is",total)
p2 = Shooter2
p2_total = Shooter2.total
print("Player 2 total is", p2_total,"/40")
if p2_total > p1_total:
    print ("Player 2 wins!")
elif p2_total < p1_total:
    print ('Player 1 wins!')
else:
    print("Tie!")
    #do more code for when tie if you want
