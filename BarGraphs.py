import matplotlib.pyplot as plt
import numpy as np

pos = np.arange(6) + 0.5
plt.barh(pos,(4,8,12,17,6,10),align = 'center',color = "red")
plt.xlabel("student",color="blue")
plt.ylabel("height",color="blue")
plt.title("height of students in inches")

plt.show()
