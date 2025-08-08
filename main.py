"""
Students: Emil Rahbek Ladekjær & David Antoine Probst
"""

import numpy as np


def demand_n_days(days, avgdemand):
    demand_list=[]
    for i in range(days):
        demand=np.random.poisson(avgdemand)
        demand_list.append(demand)
    return demand_list

def demand_stats(list):
    mean_demand=np.mean(list)
    std_demand=np.std(list)
    percentile5=np.percentile(list, 5)
    percentile95=np.percentile(list, 95)  
    print(f"mean demand: {mean_demand}")
    print(f"standard deviation: {std_demand}")
    print(f"lowest 5% {percentile5}")
    print(f"highest 5% {percentile95}")
    return percentile95

def sim_1000(sims):
    simlist=[]
    for i in range(sims):
        demand=demand_n_days(n,avg_daily_demand)
        monthdemand=np.sum(demand)
        simlist.append(monthdemand)
    return simlist

def user_interface():
    avgdemand=int(input("What is the daily average demand?\n"))
    servlevel= int(input("what service level do you want, write in whole numbers (95 for 95%)\n"))
    return avgdemand, servlevel

#main program
avg_daily_demand, service_level= user_interface()
n=30
simulations=1000
demand_list=demand_n_days(n,avg_daily_demand)
simulatedlist=sim_1000(simulations)
demand_stats(demand_list) #for 1 month
safety_stock=demand_stats(simulatedlist) # for 1000 months
optimal_stock=np.percentile(simulatedlist, service_level)
print(f"If the company wants to service their customers {service_level}% of the time they must have stock of {np.ceil(optimal_stock)} each month")
