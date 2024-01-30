n=input("Hãy nhập một dãy số:")
l=n.split()
for i in l:
    x=int(i)
    if x%5 == 0:
        if x<=150:
            print(x)
            continue
        if x>500:
            break

y= int(input("Hãy nhập một số bất kỳ"))
def count_digits(y):
    count = 0
    while y > 0:
        count += 1
        y //= 10
    return count
print("Số các chữ số là",count_digits(y))

numbers = input("Hãy nhập một dãy số:")
