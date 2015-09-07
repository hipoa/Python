data = ['a', 'b', 'c', ['abcd', 'efg']]  
#리스트는 어떤 자료형이든 포함할 수 있으며 리스트 안에 리스트를 가지고 있으면 이중배열처럼 생각하면 된다.

data[1] = ['green1', 'green2']   #이 경우는 이중리스트가 생성되고
print(data)
data[1:2] = ['green1', 'green2'] #이 경우는 단일리스트에서 수정된다.
print(data)

print(data[0])
print(data[-1][1]) #efg가 출력된다.
print(data[0:2])

b = ['1', '2', '3']
c = ['life', 'is', 'too', 'short']

f = b+c   #리스트가 병합된다.
g = b*3   #리스트가 3번 반복된다.

print(f)
print(g)

id = ['greenid1', 'greenid2', 'greenid3']
id.insert(1,'pwd1')
id.insert(2,['박준하', '01012341234'])
id.insert(4,'pwd2')
id.insert(5,['강태욱', '01023241234'])
id.insert(7,'pwd3')
id.insert(8,['이택용','01010101010'])

for steps in id:   #steps라는 리스트를 만들어서 id를 인자 하나 하나 출력해주는 것.
    print(steps)

####################################################################################################

for steps in id:
    if isinstance(steps, list):
        for step in steps :
            print(step)
    else :
        print(steps)

#위 구문은 list의 인스턴스인지 확인해서 이중 리스트를 단일 리스트로 분해하는 코드

####################################################################################################

score = [24, 75, 34, 55, 80]
score.sort()
score.reverse()
#top3 = [score[0], score[1], score[2]]
top3 = ['1', '2', '3']

for steps in range(3):
    top3[steps] = score[steps]

print(score)
print(top3)

####################################################################################################

score2 = [35, 35, 37, 49, 15]
num = score2.pop()
print(score2)
print(num)
score2.append(50)
print(score2)
score2.extend([50, 60])
print(score2)
num = score2.count(50)
print(num)