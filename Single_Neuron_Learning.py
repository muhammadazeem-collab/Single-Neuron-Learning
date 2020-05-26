import matplotlib.pyplot as plt
import math
x = 1;   				  	# Input 
n = 5;    					# Learning Rate
d = 1;   					# Desired Output
Wo = 0;
W1 = 0;
y =0;     					 # Initial Output
a = [0];   					# List that store the output values(z)
for i in range (7) :
    Wo = Wo - n * (y-d) * (y) * (1-y)
    W1 = W1 - n * (y-d) * (y) * (1-y) * (x)
    y = 1 / ( 1 + math.exp (-Wo-W1*x))
    z = ( round ( y , 4 ))  			# Round off the value up to 4 digits
    a.append(z)             			# Store each value of z in (a)
    print(round(Wo,4), round(W1,4), z)   		# print Wo,W1,z
x1,x2,y1,y2 = plt.axis()  			# Definning both axis coordinates
plt.axis((0,10,0,1))       			# Definning the axis limits
plt.plot(a)                				# Plotting the values in (a)
plt.grid(True)             				# making grid on graph
plt.ylabel('Output')       			# labeling the yaxis
plt.show()