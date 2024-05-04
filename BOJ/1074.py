n, r, c = map(int,input().split())


def recursive(board, row, col, start_num):
    if(board == 1):
        num = start_num + row * 2 + col        
        return num
    else:
        board_length = pow(2,board)
        mid = board_length // 2
        if row >= mid:
            row -= mid
            if col >= mid:
                start_num += 3 * pow(mid,2)
                col -= mid
            else:
                start_num += 2 * pow(mid,2)

        else:
            if col >= mid:
                start_num += pow(mid,2)
                col -= mid
        board -= 1

        return recursive(board, row, col, start_num)


num = recursive(n,r,c,0)
print(num)