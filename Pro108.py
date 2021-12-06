import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data1 = df["Avg Rating"].tolist()

ss = ff.create_distplot([data1],["Phones"],show_hist=True)
ss.show()