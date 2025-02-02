i = 1
while i <= 7:
    if i == 1 or i == 3 or i == 5 or i == 6 or i == 7:
        j = 1
        while j <= i:
            print(i, end="")
            j += 1
        print("\n")
    i += 1