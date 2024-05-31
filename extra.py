"""Одно задание из тестовых на стажировку"""
s = input()
s1 = s.replace(',', ' ')
s2 = s.replace(' ,', ',')
s3 = s2.replace(', ', ',')
s4 = s3.replace(',', ', ')
s5 = s4.split()
c = 0
b = ''
l = len(max(s1.split(), key=len))*3
for i in s5:
    t = b
    b += i + ' '
    if len(b)-1 == l:
        print(b[:-1])
        b = ''
    elif len(b)-1 > l:
        print(t[:-1])
        b = i + ' '
    else:
        pass
print(b[:-1])
