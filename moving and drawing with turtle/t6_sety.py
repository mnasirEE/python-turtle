# Example1
# # import package
# import turtle
 
 
# # check the turtle position
# print(turtle.position())
 
# # set the y coordinate
# turtle.sety(30)
 
# # check the turtle position
# print(turtle.position())
 
# # set the y coordinate
# turtle.sety(-50)
 
# # check the turtle position
# print(turtle.position())

# Example2

# import package
import turtle
 
 
# set turtle direction

 
# loop for pattern
for i in range(4):
   
  # motion
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(20)
  turtle.right(90)
  turtle.forward(100)
   
  # set the x coordinate 
  turtle.up()
  turtle.sety(-40*(i+1))
  turtle.down()
   
  # change the direction
  turtle.left(180)