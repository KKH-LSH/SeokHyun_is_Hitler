def print_Game():
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j]==1:
        print("O",end="  ")
      elif arr[i][j]==0:
        print("X",end="  ")
      else:
        print(" ",end="  ")
    print()
    print("-"*8)
def judge(num):
  if arr[0][0]==num and arr[0][1]==num and arr[0][2] ==num:
    return 1
  elif arr[1][0]==num and arr[1][1]==num and arr[1][2] ==num:
    return 1
  elif arr[2][0]==num and arr[2][1]==num and arr[2][2] ==num:
    return 1
  elif arr[0][0]==num and arr[1][0]==num and arr[2][0] ==num:
    return 1
  elif arr[0][1]==num and arr[1][1]==num and arr[2][1] ==num:
    return 1
  elif arr[0][2]==num and arr[1][2]==num and arr[2][2] ==num:
    return 1
  elif arr[0][0]==num and arr[1][1]==num and arr[2][2] ==num:
    return 1
  elif arr[0][2]==num and arr[1][1]==num and arr[2][0] ==num:
    return 1
arr=[[2,2,2],[2,2,2],[2,2,2]]
print_Game()
print()
print("-"*50)

for i in range(4):
  p1 = int(input("O 위치 입력: "))
  p1-=1
  p1x = p1%3
  p1y = p1//3
  if arr[p1y][p1x]==2:
    arr[p1y][p1x] =1
  print_Game()
  if(judge(1)):
    print("플레이어 1 승리")
    break
  print("-"*50)
  p2 = int(input("X 위치 입력: "))
  if arr[p1y][p1x]==2:
      arr[p1y][p1x] =1
  p2-=1
  p2x = p2%3
  p2y = p2//3
  if arr[p2y][p2x]==2:
    arr[p2y][p2x] =0
  print_Game()
  if(judge(0)):
    print("플레이어 2 승리")
    break
  print("-"*50)

if not (judge(0)or judge(1)):
  p1 = int(input("O 위치 입력: "))
  p1-=1
  p1x = p1%3
  p1y = p1//3
  arr[p1y][p1x] =1
  print_Game()
  if(judge(1)):
    print("플레이어 1 승리")
  else:
    print("무승부")