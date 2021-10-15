import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        r_index = random.randint(0, len(data)-1)
        value = data[r_index]
        dataset.append(value)

    d_mean = statistics.mean(dataset)
    return d_mean

def setup():
    meanlist = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        meanlist.append(set_of_means)
    s_mean = statistics.mean(meanlist)
    print("Mean of the sample claps data is: ", s_mean)

df = pd.read_csv('medium_data.csv')
data = df["claps"].tolist()
p_mean = statistics.mean(data)
print("Mean of the Claps in data is: ", p_mean)

print('\n')


setup()