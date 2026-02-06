import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'\path')
signal_data = df['sen_data'].values
events = df['event_truth'].values

fs = 50
time = np.arange(len(signal_data)) / fs

relevant_signal = signal_data[events == 1]
relevant_signal = relevant_signal - np.mean(relevant_signal)


plt.figure(figsize=(12, 6))
plt.plot(time, signal, 'k-', linewidth=0.5, label='Sensor Data', color='#ffffe4')

relevant_mask = events == 1
plt.fill_between(time, 0, 10000,
                 where=relevant_mask,
                 color='#0652ff', alpha=0.3, label='Relevant')

noise_mask = events == 0
plt.fill_between(time, 0, 10000,
                 where=noise_mask,
                 color='#000000', alpha=0.3, label='Noise')

plt.xlabel('Time (seconds)')
plt.ylabel('Sensor Amplitude')
plt.title('Sensor Data Visualization')
plt.ylim(0, 10000)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()