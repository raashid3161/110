import random 
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

df = pd.read_csv("newdata.csv")
#data1 = df["temp1"].tolist()
print(df.head())
column_name = "temp"
if column_name not in df.columns:
    print("error occured") 
    data = df[column_name].tolist()
    fig = ff.create_distplot([data], ["temp"], show_hist=False )


    def randMean(counter):
        dataset = []
        for i in range(0, counter):
            random_index = random.randint(0, len(data) - 1)
            value = data[random_index]
            dataset.append(value)
        mean = statistics.mean(dataset)
        return mean
        """
def setUp():
    mean_list = []
    for i in range (0, 1000):
        set_of_means = randMean(100)
        """