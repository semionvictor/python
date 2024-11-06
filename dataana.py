import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fff.csv", encoding="ISO-8859-1")

df["value"].plot(kind="line", title="A graph")
plt.xlabel("index")
plt.ylabel("value")
plt.show()

plt.savefig("b.png")