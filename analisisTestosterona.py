
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./test.txt", header=None)

# testosterona promedio
mu = 600

plt.plot(range(30),data, 'bo')
plt.axhline(y=mu, color='r')
plt.xlabel("Ciclistas")
plt.ylabel("Testosterona (ng/mL)")
plt.show()

