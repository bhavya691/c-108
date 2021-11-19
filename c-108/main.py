import random
import plotly.express as px
import statistics
counts = []
dice_result = []
for i in range(0,100):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_result.append(dice_1+dice_2)
    counts.append(i)
print(counts,dice_result)
print(statistics.mean(dice_result))
print(statistics.median(dice_result))
print(statistics.mode(dice_result))
fig =px.bar(x=dice_result, y=counts)
fig.show()