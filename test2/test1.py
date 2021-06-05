count = 0
number = 88
step = 50
predict = 50
while count != 10:
    count += 1
    step = int(step/2) if step/2 else 1
    #print(step)
    if number > predict:
        predict += step
        print(predict,step, number)
    elif number < predict:
        predict -= step
        print(predict, step)