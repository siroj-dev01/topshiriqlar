
from functools import reduce
yanvar=[1,2,3,4,5,6,7,4,9]
y=len(yanvar)
fevral=[1,3,4,5,6,3,8,9]
x=len(fevral)
mart=[1,2,3,4,0,6,7,8,9]
z=len(mart)
aprel=[1,2,3,4,5,6,0,8]
w=len(aprel)
# may=[1,2,3,4,5,6,7,8,9]
# iyun=[1,2,3,4,5,6,7,8,9]
# iyul=[1,2,3,4,5,6,7,8,9]
# avgust=[1,2,3,4,5,6,7,8,9]
# sentabr=[1,2,3,4,5,6,7,8,9]
# oktabr=[1,2,3,4,5,6,7,8,9]
# noyabr=[1,2,3,4,5,6,7,8,9]
# dekabr=[1,2,3,4,5,6,7,8,9]
oy=[yanvar , fevral, mart, aprel ]
o1=reduce((lambda x, y: x + y),yanvar)/y
o2=reduce((lambda x, y: x + y),fevral)/x
o3=reduce((lambda x, y: x + y),mart)/z
o4=reduce((lambda x, y: x + y),aprel)/w
if o1*o2>o3*o4:
    if o1>o2:print("yanvar")
    else: print("fevral")
else:
     if o3>o4: print("mart")
     else:print("aprel")

