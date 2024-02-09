library(tidyverse)
df <- read_csv("data-for-r.csv")
myBreaks <- c(1,10,100,1000,10000,100000,1000000)
myBreaks <- 33
hist(df$`Annual Salary`,breaks=myBreaks)
summary(df)
bigMoney <- filter(df,df$`Annual Salary`>200000)
