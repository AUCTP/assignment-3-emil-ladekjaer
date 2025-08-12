import random

def simulate_customers(num_customers):
    sales = []
    for customer in range(num_customers):
        if random.random() < 0.5:
            item_id = random.randint(0, len(items) - 1)
            if endinventories[item_id] > 0:
                endinventories[item_id] -= 1
                sales.append(item_id)
    return sales

def process_sales(sales):
    total_revenue = 0
    for item_id in sales:
        total_revenue += prices[item_id]
    print(f"Total Revenue: ${total_revenue}")

def generate_report():
    for i in range(len(items)):
        print(f"{items[i]}:\n ending inventory: {endinventories[i]}\n revenue: ${prices[i]*(startinventories[i] - endinventories[i])}\n costs: ${startinventories[i] * (prices[i] / 2)}\n profit: ${prices[i]*(startinventories[i] - endinventories[i]) - startinventories[i] * (prices[i] / 2)}")
    
def calculate_costs():
    total_costs = 0
    for i in range(len(items)):
        costs = startinventories[i] * (prices[i] / 2)
        total_costs += costs
    print(f"Total Costs: ${total_costs}")

#Main program
items=["coffee", "tea", "sandwich", "salad"]
prices=[10, 5, 35, 20]
startinventories=[200, 150, 100, 80]
endinventories=startinventories.copy()
n=int(input("Enter the number of customers: "))
sales=simulate_customers(n)
process_sales(sales)
calculate_costs()
generate_report()