n=int(input("Nhập một số bất kỳ:"))
def print_pattern(n):
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))
print_pattern(n)
def sum_of_numbers(n):
    return n * (n + 1) // 2
print("Tổng của các số là", sum_of_numbers(n))