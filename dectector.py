a=float(input('ENTER THE FIRST SIDE: '))
b=float(input('ENTER THE SECOND SIDE: '))
c=float(input('ENTER THE THIRD SIDE: '))
if a == b == c:
    print('This is an EQUILATERAL TRIANGLE')
elif a == b or b == c or a == c:
    print('This is an ISOSCELES TRIANGLE')
else:
    (print('This is a SCALENCE  TRIANGLE'))