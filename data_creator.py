import pandas as pd
import numpy as np
from random import randint, shuffle

dates = pd.date_range(start="2010-01-01", end="2024-12-31").tolist()
selected_dates = sorted(
    [dates[i] for i in np.random.choice(len(dates), size=1000, replace=False)]
)

for _ in range(10):
    i, j = randint(0, len(selected_dates) - 1), randint(0, len(selected_dates) - 1)
    selected_dates[i], selected_dates[j] = selected_dates[j], selected_dates[i]

values = np.random.randint(1, 1000, size=len(selected_dates))
df = pd.DataFrame({"date": selected_dates, "values": values})
df.to_csv("data.csv", index=False)
