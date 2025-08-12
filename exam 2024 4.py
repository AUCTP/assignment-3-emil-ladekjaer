# An ice cream manufacturing company produces and sells ice cream to local businesses. The
# demand for ice cream varies significantly, and the company must decide how many units of
# ice cream to produce each day to maximize profits. Here are the details of the cost and sales
# structure:
# • The cost of producing a unit of ice cream is $4.
# • Ice cream is sold for $15 per unit.
# • If a customer wants to buy ice cream and none is available, the company incurs a
# penalty of $10 per unit in lost sales and reputation.
# • Any unsold ice cream units at the end of the day are disposed of with no additional
# cost or revenue.
# The daily demand for ice cream follows a Poisson distribution with a mean of 800 units. The
# company can manufacture up to 1200 units per day.
# Your task is to develop a simulation that models this scenario.
# Tasks:
# 1. Optimal Production Calculation:
# o Develop a function optimal_production() that determines the optimal
# number of ice cream units to produce each day to maximize total profit. Use
# the given cost and sales structure.
# o Conduct at least 1000 simulations to determine the optimal production
# quantity.
# o show the profit depending on the production quantity to visualize your results
# 2. Impact of Increased Production Costs:
# o Analyze how the optimal production quantity changes if the cost of producing
# a unit of ice cream increases to $5.
# o Conduct at least 1000 simulations to determine the optimal production quantity
# under the new production cost.

def daily_profit(avgdemand, production):
    demand=np.random.poisson(avgdemand)
    if demand> production:
        penaltynumber= demand-production
    else:
        penaltynumber=0
    cost_pr_unit = 4
    selling_price = 15
    penalty_per_unit = 10
    Profit=selling_price * min(demand, production) - cost_pr_unit * production - penalty_per_unit * penaltynumber
    return Profit

def optimal_production(production, simulations):
    profit=[]
    for sim in range(simulations):
        profit.append(daily_profit(average_demand, production))
    print(f"Production level: {production} yields an average profit of {np.mean(profit)}")
            



#main program with unit costs as 4$
import numpy as np
average_demand = 800
production= [500, 600, 700, 800, 900, 1000, 1100, 1200]
simulations=1000
for productionnumber in production:
    optimal_production(productionnumber, simulations)