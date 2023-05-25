from sys import stdin
while True:
    num = stdin.readline().strip()
    if len(num) == 1 and num == "0":
        break
    num2 = list(map(lambda i: i, num))
    num2.reverse()
    num2 = "".join(num2)
    print("yes") if num == num2 else print("no")
