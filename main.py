import random
from lgs import *
#configure the script
SOL_MIN = 0
SOL_MAX = 40



#change nothing beyond here
x1 = random.randint(SOL_MIN,SOL_MAX)
x2 = random.randint(SOL_MIN,SOL_MAX)
x3 = random.randint(SOL_MIN,SOL_MAX)

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
print(r1)
print(r2)
print(r3)
