from math import sqrt

def differencer():
    for x in range(1,9):
      for y in range(1,9):
          for x2 in range(1,9):
            for y2 in range(1,9):
                if(x2==x)&(y2==y):
                    continue
                else:
                    dst = sqrt((x2-x)**2+(y2-y)**2)

                print(x,x2,y,y2,dst)

differencer()
