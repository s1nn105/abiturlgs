import random
import time
from lgs import *
#configure the script
SOL_MIN = 0
SOL_MAX = 10



#change nothing beyond here
x1 = random.randint(SOL_MIN,SOL_MAX)
x2 = random.randint(SOL_MIN,SOL_MAX)
x3 = random.randint(SOL_MIN,SOL_MAX)
sol_array= [x1,x2,x3] #becomes handy for for one-liners and is a lot simpler give as an argument to
#functions
# The Form
# Row I. [a*x1,b*x2,c*x3,d]
#Row II. [a*x1,b*x2,c*x3,d]
#Row III. [ax1*,b*x2,c*x3,d] surprise xD
#but to generate :
# Row I. [a*x1,b*x2,c*x3,d]
#Row II. [0*x1,b*x2,c*x3,d]
#Row III. [0x1*,0*x2,c*x3,d]
# IN a matrice which is obviously the form prefered this leads to
# [ a,b,c,d]
# [0,b,c,d]
# [0,0,c,d]
#and then scramble the thing with operations why ( to gurantee a simple solution)
r1 = create_row(0)
r2 = create_row(1)
r3 =create_row(2)
#r1 = solve_row(r1,sol_array)
#swaps the rows r1 isent the same row after that ( not neccessarily but surley)
r1,r2,r3 = obfusecate([r1,r2,r3])
##add the d parameter to the rows
r1 = minimize(r1)
r2 = minimize(r2)
r3 = minimize(r3)
r1 = solve_row(r1,sol_array)
r2 = solve_row(r2,sol_array)
r3 =solve_row(r3,sol_array)
t1= time.time()
print(r1)
print(r2)
print(r3)
input("press any key if finised")
t2 = time.time()
print(F"you needed {int(t2-t1)} seconds here are the results")
print(" x1 x2 x3")
print(sol_array)
