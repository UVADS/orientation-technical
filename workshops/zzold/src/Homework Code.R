print('Hello World!')
x<-runif(1000, min=1, max=100)
x<round(x)
numbs <- rnorm(1000, mean=0, sd=1)
print(numbs)
install.packages(tidyr)
install.packages(dplyr)
install.packages('tidyr')
install.packages('dplyr')
survey <- read.csv('https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv', )
survey2 -> read.csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv")
library(dplyr)
survey %>%
  filter(!CPU.Cycle.Rate..in.GHz. > 10)
surveycleaned <- survey %>%
  filter(!CPU.Cycle.Rate..in.GHz. > 10)
a <- ggplot(survey$CPU.Number.of.Cores..int., aes(x = weight))
ggplot(survey$RAM..in.GB., aes(x=weight)) + geom_histogram()
install.packages('ggplot2')
a <- ggplot(survey$CPU.Number.of.Cores..int., aes(x = weight))
a <- ggplot(survey, aes(x = weight))
a <- ggplot(survey, aes(x = surveycleaned$CPU.Number.of.Cores..int.))
a + geom_boxplot(width = 0.5) +
  geom_dotplot(aes(fill = supp), binaxis='y', stackdir='center')+
  scale_fill_manual(values = c("#00AFBB", "#E7B800"))
rlang::last_error()
p<-ggplot(surveycleaned, aes(x= surveycleaned$Operating.System, y=surveycleaned$CPU.Number.of.Cores..int)) + 
  geom_dotplot(binaxis='y', stackdir='center')
p
logGPU <- log2(surveycleaned$GPU.CUDA.Number.of.Cores..int.)
nozeroes <- filter(surveycleaned, surveycleaned$GPU.CUDA.Number.of.Cores..int. >0)
nozeroescore <- nozeroes$GPU.CUDA.Number.of.Cores..int.  
hist(log2(nozeroescore))
hist(log2(nozeroescore), col = c("blue", "red", "gray", "green", "black", "yellow", "orange"))
hist(log2(nozeroescore), col = c("blue", "green"))
