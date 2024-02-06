def block1():
    for i in range(2):
         for j in range(12):
             print('*', end = '')
         print()

def block2():
      for i in range(4):
          for j in range(3):
              print('*', end = '')
          print()

a = 5
def f10():
   global a
   a = 3
   
   
f10()
print(a)