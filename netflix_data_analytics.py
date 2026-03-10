import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")  # file must be in same folder

print(df.head())
print(df.info())

df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV on Netflix")
plt.show()
