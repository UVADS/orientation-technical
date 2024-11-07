# SQL Workshop
**Executive Summary** This document contains the materials for the UVADS workshop on SQL by Professor Alonzi. 

## Outline
2. Introduction
3. Preamble
4. The Data Scientist Minimum for SQL
5. Your first SQL project


## Introduction
1. `whois` lpa2a
2. Goals for today
    * Define and Motivate SQL
    * Prt I: Present the Data Scientist Minimum
    * Part II: Make individual plans for building SQL proficiency
    * _Secret goal: But really, I just want you to ask questions_


## Preamble
![](sql-meme.png)

**You have to have some moves. But you really need to be able to talk to the nerd in the corder.**

# Part I - The Data Scientist Minimum
## What is SQL
SQL = **S**tructured-**Q**uery-**L**anguage

pronounced S-Q-L; less commonly "sequel"; now, sometimes "squirrel" [citation needed]

## OK but what ... **is** ... SQL

# ~!~!~!~!~!! resume here !!~!~!~!~!~!~

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

# Resources
* Fun Lecture - ![Introduction to NoSQL • Martin Fowler • GOTO 2012](https://youtu.be/qI_g07C_Q5I?si=pEkFdkTYquHfcv85)
* Good Book - ![Learning SQL by Alan Beaulieu from O'Reilly](https://search.lib.virginia.edu/sources/uva_library/items/u11457927)
* SQL Practice Platform - ![Cloud Beaver](Tool: https://demo.cloudbeaver.io)

# Footnotes
[1] 

[2] 
