import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal as scipy_signal

df = pd.read_csv(r'\path')
signal_data = df['sen_data'].values
events = df['event_truth'].values

fs = 50
time = np.arange(len(signal_data)) / fs

relevant_signal = signal_data[events == 1]
relevant_signal = relevant_signal - np.mean(relevant_signal)


fft_result = np.fft.fft(relevant_signal)
freq = np.fft.fftfreq(len(relevant_signal), d=1/fs)

positive_freqs = freq[:len(freq)//2]
positive_fft = np.abs(fft_result[:len(fft_result)//2])
positive_fft = positive_fft / len(relevant_signal)

dominant_idx_fft = np.argmax(positive_fft[1:]) + 1
dominant_freq_fft = positive_freqs[dominant_idx_fft]

frequencies_psd, psd = scipy_signal.welch(relevant_signal, fs=fs, nperseg=1024)

dominant_idx_psd = np.argmax(psd[1:]) + 1
dominant_freq_psd = frequencies_psd[dominant_idx_psd]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: FFT Magnitude
ax1.plot(positive_freqs, positive_fft, color='#047495', linewidth=1.5)
ax1.axvline(dominant_freq_fft, color='#e50000', linestyle='--', linewidth=2,
            label=f'Dominant: {dominant_freq_fft:.2f} Hz')
ax1.set_xlabel('Frequency (Hz)', fontsize=12)
ax1.set_ylabel('Normalized Amplitude', fontsize=12)
ax1.set_title('FFT Magnitude Spectrum', fontsize=13, fontweight='bold')
ax1.set_xlim(0, 10)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Plot 2: PSD
ax2.plot(frequencies_psd, psd, color='#363737', linewidth=1.5)
ax2.axvline(dominant_freq_psd, color='#e50000', linestyle='--', linewidth=2,
            label=f'Dominant: {dominant_freq_psd:.2f} Hz')
ax2.set_xlabel('Frequency (Hz)', fontsize=12)
ax2.set_ylabel('Power Spectral Density (units²/Hz)', fontsize=12)
ax2.set_title('PSD (Welch Method)', fontsize=13, fontweight='bold')
ax2.set_xlim(0, 10)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()