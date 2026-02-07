__: So the raw signal used in this project looks somewhat like this (let it be application agnostic) :__

<p align="center">
   <img width="900" height="600" alt="temp" src="https://github.com/user-attachments/assets/47933219-fc48-46df-8abc-a44f15852c29" />
</p>

__: Intuitively what a filter does :__

> Before filtering: 
1. signal we saw in raw format has big waves (low frequency and could be cyclic) 
2. small ripples (high frequency) 
3. jagged edges (noise patterns - non cyclic or rhythmic)

> After filtering (expected):

The ripples outside 0.5 - 4 Hz (this consist of the dominant frequency obtained = 1.x hz) vanish, keeps only the waves required.

> #### Processes Involved

<p align="center">
<img width="300" height="400" alt="Untitled presentation" src="https://github.com/user-attachments/assets/bf62b49a-ccb1-4900-92ea-75cb5dcdc850" />
</p>


It starts with raw data (anything from anywhere) in hand, and since it is being processed in a digital system (discrete-time and discrete value captured at that time) we might need to have knowledge about the sampling frequency used to discretize this raw real-time continuous signal to make a representation of it in the digital system.




> Spectrum Analysis?

Spectrum analysis decomposes a signal into its frequency components and revealing the amplitude of each frequency component present in it. This mainly helps in understanding the frequency components of a signal. By analyzing the spectrum, we can determine the frequency distribution, amplitude, and phase of the signal. This information is crucial for understanding the characteristics and behavior of the signal-in-hand.

__"SO, FOR SIGNAL CHARACTERIZATION"__


![filter_simulation](https://github.com/user-attachments/assets/f4c04654-6a14-47fd-b3fe-a7335b58fcf6)

