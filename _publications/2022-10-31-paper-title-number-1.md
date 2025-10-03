---
title: "Quantum Error Mitigation via Matrix Product Operators"
collection: publications
permalink: /publication/2022-10-31-paper-title-number-1
excerpt: 'A new error mitigation approach based on the tensor network representation of the noise channels.'
date: 2022-10-31
venue: 'PRX Quantum'
paperurl: 'https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.040313'
citation: 'Yuchen Guo and Shuo Yang, <i>PRX Quantum</i> 3, 040313 (2022).'
selected: True
tags: ["quantum-computation"]
priority: 2
---
In the era of noisy intermediate-scale quantum devices, the number of controllable hardware qubits is insufficient to implement quantum error correction. As an alternative, quantum error mitigation (QEM) can suppress errors in measurement results via repeated experiments and postprocessing of data. Typical techniques for error mitigation, e.g., the quasiprobability decomposition method, ignore correlated errors between different gates. Here, we introduce a QEM method based on the matrix product operator (MPO) representation of a quantum circuit that can characterize the noise channel with polynomial complexity. Our technique is demonstrated on a depth = 20 fully parallel quantum circuit of up to Nq = 20 qubits undergoing local and global noise. The circuit error is reduced by a several-times factor with only a small bond dimension D' = 1 for the noise channel. The MPO representation increases the accuracy of modeling noise without consuming more experimental resources, which improves the QEM performance and broadens its scope of application. Our method is hopeful of being applied to circuits in higher dimensions with more qubits and deeper depth.
