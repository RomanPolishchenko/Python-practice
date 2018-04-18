n = [6, 7, 16574084374686347, 16093907498351251, 15385049478870551, 10889686321387879, 16811942780384527]
for num in n:
    flag = True
    for j in range(2, num // 2):
        if j == 137:
            pass
        if num % j == 0:
            flag = False
            break
    if flag:
        print(num, "- простое")
    else:
        print(num, "- не простое")
