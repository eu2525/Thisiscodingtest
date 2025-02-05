n = int(input())

# Write your code here!
def down_number(num):
    if num == 0:
        return

    print(num, end = ' ')
    down_number(num - 1)

def up_number(num):
    if num == n:
        print(num)
        return

    print(num, end = ' ')
    up_number(num + 1)


up_number(1)
down_number(n)
