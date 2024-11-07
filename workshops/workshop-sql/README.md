# HPC Workshop
**Executive Summary** This document contains the materials for the UVA residential MSDS workshop on HPC. It is a companion to the initial orientation given prior to the start of classes in June. This workshop is part of a series designed to help students with the world larger than their ocwn laptop. This workshop focuses on traditional High Performance Computing. It is offered on November 1, 2022 and again in the spring semester 2023.

## Outline
1. Warm up
2. Introduction
3. Preamble
4. The Data Scientist Minimum for HPC
5. Your first HPC project

## Warm up
Write a python program to generate 100 numbers from the standard normal distribution.

## Introduction
1. `whois` lpa2a
2. Goals for today
    * Define and Motivate HPC
    * Prt I: Present the Data Scientist Minimum
    * Part II: Make individual plans for building HPC proficiency
    * _Secret goal: But really, I just want you to ask questions_


## Preamble
![](hpc-preamble.png)

**You have to build solutions for all computers. Not just your personal machine.**

# Part I - The Data Scientist Minimum
## What is HPC
HPC = **H**igh-**p**erformance **C**omputing

## OK but what ... **is** ... HPC

**Exercise**: Read some technobabble and break it down together:

"The 59th edition of the TOP500 revealed the Frontier system to be the first true exascale machine with an HPL score of 1.102 Exaflop/s.

The No. 1 spot is now held by the Frontier system at Oak Ridge National Laboratory (ORNL) in the US. Based on the latest HPE Cray EX235a architecture and equipped with AMD EPYC 64C 2GHz processors, the system has 8,730,112 total cores, a power efficiency rating of 52.23 gigaflops/watt, and relies on gigabit ethernet for data transfer." [1]

![](https://www.kotzendes-einhorn.de/blog/wp-content/uploads/2016/02/121Gigawatts.gif)[2]

### How many pieces of jargon can you find?
1. Top500
2. HPL score
3. Exaflop/s
4. HPE Cray EX235a archituecture
5. AMD EPYC 64C 2GHz processors
6. 8,730,112 cores
7. 52.23 gigaflops/watt
8. gigabit ethernet

**Exercise:** Divide these up and do a little research in pairs, then report results.

## Repeat the exercise but with the local UVA HPC resource

All quotes below are from: https://www.rc.virginia.edu/userinfo/rivanna/overview/
1. "Currently the Rivanna supercomputer has 603 nodes with over 20476 cores and 8PB of various storage."
2. "Users may submit multiple jobs or job arrays, but the maximum aggregate cpu cores allowed for a single user’s running jobs is 1000."
3. "Rivanna is a managed resource; users must submit jobs to queues controlled by a resource manager, also known as a queueing system. The manager in use on Rivanna is Slurm. "
4. "How can I make my Jupyter notebook from JupyterLab to run as a batch job on Rivanna?"


## Why HPC?
1. Set it and forget it (jobs run in batch mode) --> I don't need to leave my laptop open
2. Run many jobs at the same time --> I don't need to buy a thousan laptops
3. The need for speed --> I don't need to buy an expensive fancy laptop

![](https://media.giphy.com/media/26AHLNr8en8J3ovOo/giphy.gif)[4]
![](2022-09-30-cas7kvf.png)[5]

## Exercise
![](deer.jpg)[6]
1. Logon to rivanna
2. Submit a batch job of "hello world", have the computer say its name
3. Submit 100 batch jobs of "hello world", have the computers say their name

**Hint: Documentation [here](https://www.rc.virginia.edu/userinfo/rivanna/slurm/) and [here](https://slurm.schedmd.com/documentation.html)**

**Hint: use `allocations` to find an allocation**

## Exercise
1. Logon to rivanna
2. Upload some code you have already written
3. Submit a batch job to run the code

# Part II
**Objective: Create an individual plan for you to practice your HPC skills**

This part is just an exercise. Individually you will explore your github account for a project that you can scale up with HPC. Then you will make a plan for scaling it up. At the end you will leave with a new github repository and a set to tasks to accomplish to put your new HPC knowledge into practice. By working this plan over time you will build proficiency with HPC.

# Wrap up
1. Please think of one thing you liked and one thing you would change about this workshop. And a few sentences about why.
2. Then make a pull request and add them to this repo in the folder workshop-gnu-linux/feedback.
![](../workshop-gnu-linux/swanson-please.png)


# Footnotes
[1] https://www.top500.org/news/ornls-frontier-first-to-break-the-exaflop-ceiling/
[2] https://www.kotzendes-einhorn.de/blog/wp-content/uploads/2016/02/121Gigawatts.gif
[3] https://www.rc.virginia.edu/userinfo/rivanna/overview/
[4] https://media.giphy.com/media/26AHLNr8en8J3ovOo/giphy.gif
[5] cas7kvf
[6] https://cdn.sanity.io/images/z2aip6ei/production/2d6e54d6b6ba1cd2867e9f1c9b5d75f788d04284-2560x1060.jpg


