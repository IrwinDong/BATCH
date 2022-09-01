#%%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

SLO = 1000 #ms
batch_size = 50
time_out = 0.97
inter_arrival = 20.0
data = []
with open(f"Latency_per_request_batch_{batch_size}_inter_arrival_{inter_arrival}_time_out{time_out}_.log", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        arr = line.split("\t")
        #if len(arr) < 7:
        #    continue
        latency = float(arr[1])
        data.append(latency)
        line = fd.readline()
sample = np.percentile(data, 95)

data = np.array(data)
slo_percent = np.count_nonzero(data < SLO) / len(data)

print("latency at 95 percentile =" + str(sample))
print("SLO compliant percentage =" + str(slo_percent))

data = np.sort(data)
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.hist(data, bins=20, cumulative=True, weights=np.ones(len(data))/len(data))
ax.grid(axis='both')
y_ticks = np.arange(0, 1, 0.05)
ax.set_yticks(y_ticks)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.set_xlabel('Request Latency(ms)')
ax.set_ylabel('Percentage')

plt.show()
# %%
