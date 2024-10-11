import matplotlib.pyplot as plt

years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
revenue = [180600000, 1054233825.96, 2454571141, 7107185956.58, 18059000000]
expenses = [69885000, 263873000, 597002114.10, 1446438683.16, 2903025746.15]

profit = [r - e for r, e in zip(revenue, expenses)]
profit_margin = [(p / r) * 100 for p, r in zip(profit, revenue)]

plt.plot(years, profit_margin, marker='o', linestyle='-', color='green')

plt.xlabel("Years (yr)")
plt.ylabel("Profit Margin (%)")

plt.yticks(range(25, 101, 25))

plt.title("Profit margin over 5 years")

plt.show()