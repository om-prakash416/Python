s1= float(input('input first side value: '))
s2= float(input('input second side value: '))
s3= float(input('input third side value: '))

sp= (s1+s2+s3)/2

area = (sp*(sp-s1) * (sp-s2) * (sp-s3)) ** 0.5

print(sp)
print('the area of the triangle is : ', area)