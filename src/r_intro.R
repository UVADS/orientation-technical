library(tidyverse)
library(ggplot2)

survey1<-read.csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv")
survey2<-read.csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv")
survey2<-survey2[-c(2), ]

#change column names
colnames(survey1)<-c("timestamp", "operating.system", "cpu.cycle.rate", "cpu.num.cores", "ram", "hard.drive.size", "gpu")
colnames(survey2)<-c("timestamp", "operating.system", "cpu.cycle.rate", "cpu.num.cores", "ram", "hard.drive.size", "gpu", "gpu.cuda.num.cores")

#number of rows and columns
nrow(survey2)
ncol(survey2)

plot(survey2$cpu.num.cores, survey2$hard.drive.size, col="black", pch=20, cex=1, xlab="Num of CPU Cores", ylab="Hard Drive Size (GB)", main="Num of CPU Cores vs. Hard Drive Size")

table(survey2$operating.system, survey2$cpu.num.cores)

summary(survey2$ram)

#grouped scatter plot
plot(survey2$cpu.cycle.rate, survey2$hard.drive.size, pch=19, col=factor(survey2$operating.system), xlab="CPU Cycle Rate (GHz)", ylab="Hard Drive Size (GB)", main="CPU Cycle Rate vs. Hard Drive Size by OS")

legend("topleft",
       legend = levels(factor(survey2$operating.system)),
       pch = 19,
       col = factor(levels(factor(survey2$operating.system))))
