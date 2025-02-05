Y, M, D = map(int, input().split())

# Write your code here!
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

yun_year = False

if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            yun_year= True
    else:
        yun_year = True


if yun_year:
    month_day[1] = 29

if month_day[M - 1] < D:
    print(-1)
else:
    if M >= 3 and M <=5:
        print("Spring") 
    elif M >= 6 and M <= 8:
        print("Summer")
    elif M >= 9 and M <= 11:
        print("Fall")
    else:
        print("Winter")