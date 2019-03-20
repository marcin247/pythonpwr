#1
for x in range(56,101):
    print("For x=",x,"results is",2*x**2+2*x+2)
#2
import math
print('Insert your value here:')
y = int(input())
z=math.factorial(y)

print("Factorial value of inserted number is",z)
#3
print("Insert array value")
y=input()
def numbers(testx):
    z= min(testx)
    xx=testx.index(z)
    print("Lowest value",z)
    print("Index number",xx)
    return
numbers(y)
#4
import numpy as np
import matplotlib.pyplot as plt
print("Insert length plot value")
l=int(input())
x = np.linspace(0, l, 100)
y =2*x+2+x*x
plt.plot(x, y,color="darkorange",label="y=2x+2+x^x")
plt.legend(loc="lower right")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph of the function")
plt.savefig('Graph of the function.pdf')
plt.show()
