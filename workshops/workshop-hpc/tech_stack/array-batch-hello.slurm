#!/bin/bash

# execute with sbatch --array=1-10 array-batch-hello.slurm

#SBATCH -A ds4002-lpa2a
#SBATCH --partition=standard   # partition
#SBATCH --output=result_array_id_%a.out

./hello.sh
