while True:
    num = int(input("Enter any number: "))

    while num >= 1:
        if num == 1:
            print("1")
            break
        if num % 2 == 0:
            print("0")
        else:
            print("1")
        num = num // 2

    print("====Next number====")
