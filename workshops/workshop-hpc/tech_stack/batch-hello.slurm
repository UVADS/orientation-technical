#!/bin/bash

# execute with sbatch batch-hello.slurm

#SBATCH -A ds4002-lpa2a
#SBATCH --partition=standard   # partition
#SBATCH --output=result.out

./hello.sh
