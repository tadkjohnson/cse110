import math



 
# print("Get the area of a shape")
# sq_side = float(input("what is a sides length of the square? "))
# sq_area = sq_side * sq_side
# print(f"the area of the square is: {sq_area:.3f}")
# # print(f"the area of the square is: {sq_side **2:.3f}") another way to do it 
# print()
# print("Get the area of a circle")
# circle = float(input("what is a radius of the circle? "))
# cir_area = math.pi * circle **2
# print(f"the area of the circle is: {cir_area:.3f}")
# print()
# print("Get the area of a rectangle")
# rec_length = float(input("what is the length of the rectangle? "))
# rec_width = float(input("what is the width of the rectangle? "))
# rec_area = rec_length * rec_width
# print(f"the area of the rectangle is: {rec_area:.3f}")
# # print(f"the area of the rectangle is {rec_length * rec_width}") another way to do it 

#### this is for centimeters 
 
print("Get the area of a shape")
sq_side = float(input("what is a sides length of the square? (in centimeters) "))
sq_area = sq_side * sq_side
print(f"the area of the square is: {sq_area:.3f} cm^2")
# print(f"the area of the square is: {sq_side **2:.3f}") another way to do it 
sq_meters = sq_area / 10000
print(f"in square meters {sq_meters} m^2")
print()
print("Get the area of a circle")
circle = float(input("what is a radius of the circle?(in centimeters) "))
cir_area = math.pi * circle **2
print(f"the area of the circle is: {cir_area:.3f}")
print()
print("Get the area of a rectangle")
rec_length = float(input("what is the length of the rectangle? (in centimeters)"))
rec_width = float(input("what is the width of the rectangle? (in centimeters)"))
rec_area = rec_length * rec_width
print(f"the area of the rectangle is: {rec_area:.3f}")
# print(f"the area of the rectangle is {rec_length * rec_width}") another way to do it 






