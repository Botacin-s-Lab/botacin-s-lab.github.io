---
title: HPC Security
---

# HPC Security

<span class="pill">ongoing</span> · Funded by [NSF Award #2327427](../funding/index.md) · PI: Marcus Botacin · 2024 to 2027

**Can the performance counters already built into every CPU serve as the next generation of antivirus?** Hardware Performance Counters (HPCs) count low-level events such as branches, cache misses and instructions retired. Moving malware detection into hardware would let it run alongside the system instead of slowing it down. This project asks how to design such a detector and how well it would hold up.

## Research questions

1. **How many counters are enough?** Evaluate architectures with an unlimited number of HPCs to establish whether HPCs are viable for malware detection, then determine the minimum number an actual CPU design would need.
2. **Can attackers mimic benign behavior?** Study HPC susceptibility to mimicry attacks by building compiler extensions that automatically create code diversity.
3. **Can we explain detections?** Build explainable AI models that show humans how an attack is detected at the HPC level.

## Expected outputs

- A formal methodology to evaluate hardware antivirus designs, and to tell which parts of a system best indicate malware.
- A simulation tool for prototyping hardware-based antivirus products.
- Open-source code for every tool developed in the project.

## People

Master's student **Sahil Kaushal** is writing a thesis on hardware performance counters (Fall 2026). Undergraduates have contributed through the NSF REU supplement.

## Publications acknowledging this award

NSF's award record lists these papers, all with Prof. Botacin as an author:

- *On the uniqueness of AntiVirus labels: How many labels do we need to fingerprint an AV?* J. Comput. Virol. Hack. Tech., 2025. [DOI](https://doi.org/10.1007/s11416-024-00541-1)
- *ML-Based Behavioral Malware Detection Is Far From a Solved Problem.* IEEE SaTML, 2025. [DOI](https://doi.org/10.1109/SaTML64287.2025.00056)
- *Towards more realistic evaluations: The impact of label delays in malware detection pipelines.* Computers & Security, 2025. [DOI](https://doi.org/10.1016/j.cose.2024.104122)
- *Fuzzing and Symbolic Execution for Multipath Malware Tracing.* ACM Digital Threats: Research and Practice, 2024. [DOI](https://doi.org/10.1145/3700147)
- *What do malware analysts want from academia?* RAID 2024. [DOI](https://doi.org/10.1145/3678890.3678892)
- *Cross-Regional Malware Detection via Model Distilling and Federated Learning.* RAID 2024. [DOI](https://doi.org/10.1145/3678890.3678893)
- *SoK: All You Need to Know About On-Device ML Model Extraction.* USENIX Security 2024. [Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/nayan)

!!! info "Code and data"
    Repositories for this project will be linked here as they are released.
