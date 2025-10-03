---
title: "Efficient quantum circuit compilation for near-term quantum advantage"
collection: publications
permalink: /publication/2025-06-10-paper-title-number_10
excerpt: 'Approximate compilation method for deep circuit to mitigate noise effects and improve overall fidelity'
date: 2025-06-10
venue: 'EPJ Quantum Technology'
paperurl: 'https://epjquantumtechnology.springeropen.com/articles/10.1140/epjqt/s40507-025-00368-9'
citation: 'Yuchen Guo and Shuo Yang, EPJ Quantum Technol. 12, 69 (2025).'
---
Quantum noise in real-world devices poses a significant challenge in achieving practical quantum advantage, since accurately compiled and executed circuits are typically deep and highly susceptible to decoherence. To facilitate the implementation of complex quantum algorithms on noisy hardware, we propose an approximate method for compiling target quantum circuits into brick-wall layouts. This new circuit design consists of two-qubit CNOT gates that can be directly implemented on real quantum computers, in conjunction with optimized one-qubit gates, to approximate the essential dynamics of the original circuit while significantly reducing its depth. Our approach is evaluated through numerical simulations of time-evolution circuits for the critical Ising model, quantum Fourier transformation, and Haar-random quantum circuits, as well as experiments on IBM quantum platforms. By accounting for compilation error and circuit noise, we demonstrate that time evolution and quantum Fourier transformation circuits achieve high compression rates, while random quantum circuits are less compressible. The degree of compression is related to the rate of entanglement accumulation in the target circuit. In particular, experiments on IBM platforms achieve a compression rate of 12.5 for N = 12, significantly extending the application of current quantum devices. Furthermore, large-scale numerical simulations for system sizes up to N = 30 reveal that the optimal depth d_max to achieve maximal overall fidelity is independent of system size N, suggesting the scalability of our method for large quantum devices in terms of quantum resources.
