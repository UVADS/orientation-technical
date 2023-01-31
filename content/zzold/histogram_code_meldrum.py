import csv

with open('survey.csv','r') as file:
    reader = csv.reader(file)
    y = []
    for row in reader:
        y.append(row)
    y.remove(y[0])
    cycle_rate=[]
    ram=[]
    cores = []
    for item in y:
        cycle_rate.append(float(item[2]))
        ram.append(int(item[4]))
        cores.append(float(item[3]))
    
    from matplotlib import pyplot as plt
    import numpy as np
    plt.hist(cycle_rate, list(range(0,33)), color='#a64d70', label = "CPU Cycle Rate (GHz)")
    plt.hist(ram, bins = list(range(0,33)), color = '#45818e', label = "Ram (GB)")
    plt.hist(cores, bins = list(range(0,33)), color= '#fff2cc', label = "CPU Number of Cores")
    plt.legend()
    
