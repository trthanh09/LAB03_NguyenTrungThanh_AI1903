#1
def middle(character_str):
    mid=len(character_str)
    middle_start=(mid-4)//2
    middle_end=middle_start+4
    middle_4_chars=character_str[middle_start:middle_end]
    return middle_4_chars
result=middle('HoSongHu')
print(result)
#2
def mid(s1, s2):
    length=len(s1)
    middle=length//2
    s3=s1[:middle]+s2+s1[middle:]
    return s3
s1='Ault'
s2='Kelly'
resultt=mid(s1, s2)
print(resultt)
#3
def firstmiddlelast(s3, s4):
    middleS1=len(s3)//2
    middleS2=len(s4)//2
    firstS1=s3[0]
    firstS2=s4[0]
    lastS1=s3[-1]
    lastS2=s4[-1]
    S3= firstS1+firstS2+s3[middleS1]+s4[middleS2]+lastS1+lastS2
    return middleS1, middleS2, firstS1, firstS2, lastS1, lastS2, S3
s3='America'
s4='Japan'
resul=firstmiddlelast(s3, s4)
print(resul)
#4
def sort1(s):
    return ''.join(sorted(s, key=lambda x: (x.isupper(), x)))
Custom='aodwOJIOAJaoidwOJOdwjoKdjapK'
resu=sort1(Custom)
print('Sap xep tu chu thuong den chu in hoa: ', resu)
#5
n=input('Nhap vao 1 cau: ')
Chars=0
Digit=0
Symbol=0
for i in range(len(n)):
    if '0' <= n[i] <= '9':
        Digit+=1
    elif 'a' <= n[i] <= 'z' or 'A' <= n[i] <= 'Z':
        Chars+=1
    else:
        Symbol+=1
print('Total counts of chars: ', Chars)
print('Total counts of digits: ', Digit)
print('Total counts of symbols: ', Symbol)