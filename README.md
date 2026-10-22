# Leaky Integrate-and-Fire Neuron Simulation
A small computational neuroscience experiment exploring how
input current affects neuronal firing behavior.

![Input Current vs Firing Rate](results/input_current_vs_firing_rate.png)

## Research Question
How does input current affect the firing rate of a simplified
leaky integrate-and-fire neuron?

## Hypothesis
Stronger input current will cause the neuron to reach its firing
threshold more frequently, increasing its firing rate.

## Model
Briefly explain:
- resting voltage
- threshold
- reset voltage
- leak
- input current
- firing rate

## Method
- simulated 1000 time steps
- each step represents 1 ms
- tested currents from 2 to 8
- counted spikes
- calculated spikes per second

## Results
Describe what your graph shows.

## Limitations
This is a simplified model and does not simulate the full biological
mechanisms of an action potential.

## Future Work
- use a more realistic LIF equation
- add noise
- investigate spike timing
- compare different neuron parameters