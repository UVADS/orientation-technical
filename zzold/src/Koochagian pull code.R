install.packages('readr')
#the libraries

library(readr)
library(tidyverse)

#getting the file from github
file_2022 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv"

#reading the data
newdata=read_csv(url(file_2022))
newdata= newdata[-c(2),]


#reading the data
head(newdata)
View(newdata)

#creating the column names
colnames(newdata) = c('time', 'os', 'cpu_rate','cpu_cores','ram','hdrive','gpu','gpu_cuda')

#some plotting practice
ggplot(data=newdata)+ geom_point(mapping=aes(x= os, y=cpu_rate))

ggplot(data=newdata)+ geom_bar(mapping=aes(x=cpu_cores,y=hdrive),stat='identity')



