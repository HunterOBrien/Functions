def check_factor(bigger_num, smaller_num):
    return num[0] % num[1] == 0


# Main
num = int(input()).split()
if check_factor(num[0], num[1]):
    print(f"{num[1]} is a factor of {num[0]}")
else:
    print(f"{num[1]} is not a factor of {num[1]}")
