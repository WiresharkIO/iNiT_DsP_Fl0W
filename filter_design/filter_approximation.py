import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, ellip, filtfilt
import os

df = pd.read_csv(r'\path')
signal_data = df['sen_data'].values
events = df['event_truth'].values

fs = 50
relevant_signal = signal_data[events == 1]
noise_signal = signal_data[events == 0]

lowcut, highcut, order = 0.5, 4.0, 4
nyquist = fs / 2
low, high = lowcut / nyquist, highcut / nyquist

b_butter, a_butter = butter(order, [low, high], btype='band')
b_ellip, a_ellip = ellip(order, 1, 40, [low, high], btype='band')

relevant_butter = filtfilt(b_butter, a_butter, relevant_signal)
relevant_ellip = filtfilt(b_ellip, a_ellip, relevant_signal)
noise_butter = filtfilt(b_butter, a_butter, noise_signal)
noise_ellip = filtfilt(b_ellip, a_ellip, noise_signal)

output_dir = os.getcwd()
print(f"Saving plots to: {output_dir}")

plt.figure(figsize=(12, 6))
time_eat = np.arange(2000) / fs
plt.plot(time_eat, relevant_signal[:2000], '#000000', linewidth=1.0, alpha=0.5, label='Raw')
plt.plot(time_eat, relevant_butter[:2000], '#0652ff', linewidth=1.2, label='Butterworth')
plt.plot(time_eat, relevant_ellip[:2000], '#0cff0c', linewidth=1.2, label='Elliptic')
plt.title('Relevant Signal Filter Output', fontweight='bold', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'plot1_class1_eating_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 6))
time_noise = np.arange(2000) / fs
plt.plot(time_noise, noise_signal[:2000], '#000000', linewidth=1.0, alpha=0.5, label='Raw')
plt.plot(time_noise, noise_butter[:2000], '#0652ff', linewidth=1.2, label='Butterworth')
plt.plot(time_noise, noise_ellip[:2000], '#0cff0c', linewidth=1.2, label='Elliptic')
plt.title('Noise Supression', fontweight='bold', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'plot2_class0_noise_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
