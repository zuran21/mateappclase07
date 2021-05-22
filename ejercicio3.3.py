import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,1.5,4,2.5,6,4,3,5.5,5,2]
y=[3,4,8,4.5,10,5,15,9,5,16,13,3]
plt.scatter(x,y,color="red")
plt.title("grafico de linea")
plt.xlabel("X")
plt.ylabel("Y")

linear_model=np.polyfit(x,y,2)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,7)
plt.plot(x_s,linear_model_fn(x_s),color="green")

plt.show()
