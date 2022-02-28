number_10digits = range(1000000000, 10000000000)
prime = [2, 3, 5, 7, 11, 13, 17]


for num in number_10digits:
    temp_str = str(num)
    divisible = True
    for i in range(1, 8):
        temp_int = int(temp_str[i:i+3])
        if (temp_int%prime[i-1] != 0):
            divisible = False
            break

    if (divisible):
        print(num)
