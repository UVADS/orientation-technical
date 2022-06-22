library(tidyverse)
surveydata <- read_csv("2022-06-14-survey.csv")

surveydatanew <- surveydata %>% 
  filter(`CPU Cycle Rate (in GHz)`< 5)


surveydatalm <- lm(`CPU Cycle Rate (in GHz)` ~ `RAM (in GB)` , data = surveydatanew)
summary(surveydatalm)

ggplot(data = surveydatanew) + geom_point(mapping = aes(`RAM (in GB)`, `CPU Cycle Rate (in GHz)`, color = `Operating System`))

ggplot(data = surveydatanew) + geom_bar(mapping = aes(`Operating System`, fill = `Operating System`))

ggplot(data = surveydatanew) + geom_histogram(mapping = aes(`Hard Drive Size (in GB)`))
