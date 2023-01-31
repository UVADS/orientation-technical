## Load Packages
library(readr)
library(tidyverse)

## Read Files from Github
file_2021 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv"
file_2022 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv"

## Load Data from Files
data_old = read_csv(url(file_2021))
data_new = read_csv(url(file_2022))
colnames(data_old) = c('time', 'os', 'cpu_rate', 'cpu_cores', 'ram', 'storage', 'gpu')
colnames(data_new) = c('time', 'os', 'cpu_rate', 'cpu_cores', 'ram', 'storage', 'gpu', 'gpu_cores')
data_new = data_new[-c(2),] # Remove Outliers

## View Data
#View(data_old)
#View(data_new)

## Data Exploration
ggplot(data = data_old) + geom_point(mapping = aes(x = os, y = cpu_rate)) 
ggplot(data = data_new) + geom_point(mapping = aes(x = os, y = cpu_rate))

## Min.Median.Max
ggplot(data = data_old) + 
  stat_summary(
    mapping = aes(x = os, y = cpu_rate),
    fun.min = min,
    fun.max = max, 
    fun = median)

#Operation System
ggplot(data = data_old) + geom_bar(mapping = aes(x = os))
ggplot(data = data_new) + geom_bar(mapping = aes(x = os))

#CPU Rate
ggplot(data = data_old) + geom_bar(mapping = aes(x = cpu_rate))
ggplot(data = data_new) + geom_bar(mapping = aes(x = cpu_rate))

#CPU Cores
ggplot(data = data_old) + geom_bar(mapping = aes(x = cpu_cores))
ggplot(data = data_new) + geom_bar(mapping = aes(x = cpu_cores))

#RAM
ggplot(data = data_old) + geom_bar(mapping = aes(x = ram))
ggplot(data = data_new) + geom_bar(mapping = aes(x = ram))

#Storage
ggplot(data = data_old) + geom_bar(mapping = aes(x = storage))
ggplot(data = data_new) + geom_bar(mapping = aes(x = storage))