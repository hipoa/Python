################2015.9.9 python lec3############################

dic = {'name' : 'pey', 'phone' : '01053776459'}
a = {1:'hi'}
a[2] = 'hello'
b = {'a' : [1,2,3]}
print(dic['name'])
print(a[2])
print(b['a'])
c = a.keys()
print(list(c))
d = a.values()
print(list(d))

####################################################dictionary

movie = {'박준하' : {'암살' : '3점', '베테랑' : '4점'},
         '강태욱' : {'암살' : '4점', '베테랑' : '3점'}}

print(movie.keys())
print(movie.values())
print(movie['박준하'])
print(movie['박준하']['암살'])
print(movie.get('박준하').get('암살'))  #바로 위 라인과 똑같다

###########################################dictionary 응용

s1 = set([1,2,3,2,1,2,3,2])  ##############입력을 이렇게 주어도 {1,2,3}만을 입력받는다
a = list(s1)
print(a)
print(s1)

#######################################################조건문

answer = input("would you like express shipping?")
if answer.upper() == "YES" :
    print("that will be an extra $10")

#######################################################반복문

num = [(1,2), (3,4), (5,6)]
#for(first,last) in num:
#    print(first+last)   
#for steps in num:
#    print(steps)

#####################################################구구단
for i in range(2,10):
    for j in range(1,10):
        print('{0:3d} * {1:d} = {2:3d}' .format(i,j,i*j), end = " ")
    print('')

#####################################################리스트내의 for문
number = [1,2,3,4]
result = []
result = [num*3 for num in number]
print(result)

########################################################터틀(turtle)

import turtle
nsides = 5
for steps in range(nsides):
    turtle.forward(100)
    turtle.right(360/nsides)
    for moresteps in range(nsides):
        turtle.forward(50)
        turtle.right(360/nsides)

for steps in ['red', 'blue', 'green', 'black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

#########################################################