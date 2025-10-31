def print_z_pattern(n):
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n - 1:
                print('*', end='')
            elif col == n - row - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

print_z_pattern(5)