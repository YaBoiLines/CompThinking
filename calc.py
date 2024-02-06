
'''
import turtle

t = turtle
for x in range(4):
    t.forward(100)
    t.right(90)
t.done()
'''
num_steps = 6
for r in range(num_steps):
    for c in range(r):
        print(' ', end='')
    print('#')