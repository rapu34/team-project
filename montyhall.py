from random import randint

k = int(input('Enter the number of repetitions'))

def montihol(time):

    suc = 0 # 자동차를 고른 횟수
    fail = 0 # 염소를 고른 횟수
    
    for i in range(time):
        car = randint(0,2) #자동차가 있는 곳을 랜덤으로 선택

        doors = [0, 0, 0] #문 만들기

        doors[car] += 1 #차가 있는 곳을 1로 만들기

        choice = randint(0,2) #처음 고르기

        if doors[choice] == 0: #만약 염소를 골랐다면 고른 곳을 2로 바꾸어준다
            doors[choice] += 2
        else: #만약 차를 골랐다면 고른곳을 3으로 바꾸어준다
            doors[choice] = 3

        doors.remove(0) #염소가 있는 곳 하나를 개방 : 위에서 2나 3으로 바꾼 이유는 개방 안되게 할려고

        if 2 in doors: #만약 염소를 골랐다면 다른 염소는 개방되어있다. 바꾸면 차를 고른것이다.
            suc += 1
        else:
            fail += 1 #위의 경우가 아니라면 차를 골랐던 경우이다. 바꾸면 염소이므로 염소를 고른것이다.

    arr = [suc,fail,suc+fail,suc/(suc+fail)] #리턴할때 성공,실패,총 경우, 성공확률 리스트 리턴
    return arr

arr = montihol(k)

print('Success %d, Fail %d, success Rate %f%%' %(arr[0],arr[1],arr[3]*100))

