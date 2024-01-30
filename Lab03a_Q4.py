#1
def keepdigit(m):
    return ''.join(filter(str.isdigit, m))
m='abc123def456'
result1=keepdigit(m)
print('Cac so sau khi loai bo cac ki tu: ', result1)
#2
def removesymbol(k):
    return ''.join(filter(lambda x:x.isalnum() or x.isspace(), k))
k= '/*Jon is @developer & musician'
reu=removesymbol(k)
print('Cau sau khi loai bo cac ki tu dac biet: ', reu)
#3
str_list=['Emma', 'Jon', '', 'Kelly', '', 'Eric','']
resu1=list(filter(lambda x: x != '', str_list))
print('Sau khi loai bo string rong ta duoc: ', resu1)
#4
str1='Emma-is-a-data-scientist'
rem=str1.split('-')
print(rem)
