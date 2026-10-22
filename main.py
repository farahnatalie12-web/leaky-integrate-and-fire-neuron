import matplotlib.pyplot as plt

resting_voltage = -70
threshold = -50
reset_voltage = -70

leak_strength  = 0.1



time_steps = 1000
dt = 1 

input_currents = [2, 3, 4, 5, 6, 7, 8]


firing_rates = []



for input_current in input_currents:
    # The membrane begins at its resting potential
    voltage = resting_voltage
    spike_count = 0

    for step in range(time_steps):
        leak = leak_strength * (voltage - resting_voltage)
        voltage = voltage + input_current - leak
    
        # If the membrane reaches threshold, record a spike
        # and reset the neuron.
        if voltage >= threshold:
             voltage = reset_voltage
             spike_count+= 1

    simulation_time_seconds = (time_steps * dt) / 1000
    firing_rate = spike_count / simulation_time_seconds

    firing_rates.append(firing_rate)

   

    print("Input: ", input_current, "Firing rate:", firing_rate, "Hz")



plt.plot(input_currents, firing_rates, marker="o")
plt.xlabel("Input current")
plt.ylabel("Firing rate (Hz)")
plt.title("Input Current vs Firing Rate")
plt.savefig("results/input_current_vs_firing_rate.png")
plt.show()


    



