# HPC Workshop
**Executive Summary** This document contains the materials for the UVA residential MSDS workshop on HPC. It is a companion to the initial orientation given prior to the start of classes in June. This workshop is part of a series designed to help students with the world larger than their ocwn laptop. This workshop focuses on traditional High Performance Computing. It is offered on November 1, 2022 and again in the spring semester 2023.

## Outline
1. Introduction
2. Preamble
3. The Data Scientist Minimum for HPC
4. Your first HPC project

## Introduction
1. `whois` lpa2a
2. Goals for today
  * Define HPC
  * Motivate the need for HPC
  * Describe our plan
  * Present the Data Scientist Minimum
  * Make individual plans for building HPC proficiency
  * But really, I just want you to ask questions


## Preamble
![](hpc-preamble.png)
** You have to build solutions for all computers. Not just your personal machine. **

# Part I - The Data Scientist Minimum
## What is HPC
HPC = **H**igh-**p**erformance **C**omputing

## OK but what ... **is** ... HPC

**Exercise**: Read some technobabble and break it down together:

The 59th edition of the TOP500 revealed the Frontier system to be the first true exascale machine with an HPL score of 1.102 Exaflop/s.

The No. 1 spot is now held by the Frontier system at Oak Ridge National Laboratory (ORNL) in the US. Based on the latest HPE Cray EX235a architecture and equipped with AMD EPYC 64C 2GHz processors, the system has 8,730,112 total cores, a power efficiency rating of 52.23 gigaflops/watt, and relies on gigabit ethernet for data transfer.

![](https://www.kotzendes-einhorn.de/blog/wp-content/uploads/2016/02/121Gigawatts.gif)

### How many pieces of jargon can you find?
1. Top500
2. HPL score
3. Exaflop/s
4. HPE Cray EX235a archituecture
5. AMD EPYC 64C 2GHz processors
6. 8,730,112 cores
7. 52.23 gigaflops/watt
8. gigabit ethernet

## Repeat the exercise but with the local UVA HPC resource
"Currently the Rivanna supercomputer has 603 nodes with over 20476 cores and 8PB of various storage."

"Users may submit multiple jobs or job arrays, but the maximum aggregate cpu cores allowed for a single user’s running jobs is 1000."

"Rivanna is a managed resource; users must submit jobs to queues controlled by a resource manager, also known as a queueing system. The manager in use on Rivanna is Slurm. "

"How can I make my Jupyter notebook from JupyterLab to run as a batch job on Rivanna?"
