def print_move(src, des):
    print(f'move from {str(src)} to {str(des)}')

def towers(n, src, des, spare):
    if n == 1:
        print_move(src, des)
    else:
        towers(n - 1, src, spare, des)
        towers(1, src, des, spare)
        towers(n - 1, spare, des, src)

print(towers(5, 'tower 1', 'tower 2', 'tower 3'))
