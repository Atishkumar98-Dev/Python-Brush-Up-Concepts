import turtle

atish_turtle = turtle.Turtle()
s  = input('enter value')
atish_turtle.speed(100)

def square():
  
  atish_turtle.forward(int(s))
  atish_turtle.right(90)
  atish_turtle.forward(100)
  atish_turtle.right(90)
  atish_turtle.forward(100)
  atish_turtle.right(90)
  atish_turtle.forward(100)
  
# square()
# atish_turtle.forward(400)
# square()

# bing_weight = 300 
# tring_weight = 20

# if bing_weight < tring_weight:
#   square()
# else:
#   atish_turtle.forward(200)
# print(300<20)
# atish = 'happy' 
# while atish == 'happy': 
#   atish_turtle.forward(150)

for count in range(4):
  square() 
atish_turtle.forward(200)
for count in range(4):
  square() 
atish_turtle.forward(100)
atish_turtle.right(90)
atish_turtle.forward(200)
atish_turtle.right(90)
atish_turtle.forward(100)
for count in range(4):
  square()


 

