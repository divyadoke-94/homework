import matplotlib.pyplot as plt   # ✅ use plt not plot
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label="sin(x)", color="blue", linestyle="--")  # ✅ fixed quotes & spelling
plt.xlabel("x-axis")
plt.ylabel("y-axis")   # ✅ fixed typo (ylable → ylabel)
plt.title("Sine Wave Example")
plt.legend()
plt.grid(True)   # ✅ capital 'T'
plt.show()

import numpy as np

y2 = np.cos(x)
plt.plot(x, y, label="sin(x)",color="red")
plt.plot(x, y2, label="cos(x)", color="green")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and cosine waves")
plt.legend()
plt.show()

categories = ['A','B','C','D']
values = [10,24,36,18]



data = np.random.rand(50)
plt.hist(data, bins=30, colou='purple', edgecolor= 'black')
plt.title("Histogram Example")
plt.show()

x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.sector(x_scatter,y_scatter, color = 'darkgreen')
plt.title("sactter plot Example")

size = [30,20,25,25]
lables = ['Apple','banana','mango','grapes']
plt.pie(sizes, lables=labels, autopct='%1.1f%%,startangle=140')
plt.title("pie chart Example")
plt.show()

fig, axs = plt.subplots(2,2, figsize=(8,8))
axs[0,0].plot(x, y,color='blue')
axs[0,0].set_title("line plot")

axs[0,1].bar(categories,values, color='orange')
axs[0,1].set_title("Bar chart")

axs[1,0].hist(data, bins=20, color='green')
axs[1,0].set_title("histogram")

axs[1,1].scatter(x_scatter,y_scatter,color='red')
axs[1,1].set_title("scatter plot")

plt.tight_layout()
plt.show()