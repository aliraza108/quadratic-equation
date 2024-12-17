
from cmath import sqrt


# a = int(input("what is your a: "))
# b = int(input("what is your b: "))
# c = int(input("what is your c: "))

# bminus = -b
# bsqr = b**2 - (4*a*c) 
# bsqr= bsqr**2
# a2 = (2*a)
# final = bminus + bsqr / a2
# print(final)
# x = 200
# z = sqrt(x)
# print(z)

# -b + B2 - 4ac
# _____________
#       2a

a= int(input("Input your A"))
b= int(input("Input your B"))
c= int(input("Input your C"))

sq1 = sqrt((b*b)-(4*a*c))
final1 = (-b+sq1)/(2*a)
final2 = (-b-sq1)/(2*a)
# ans = -b + (b*b - (4*a*c)) **0.5 / (2*a)

# ans = -b + sqrt((b*b - (4*a*c))) / (2*a)

print(f"Your X Coordinate is {final1}")
print(f"Your y Coordinate is {final2}")
# print("Your y Coordinate is", final2)