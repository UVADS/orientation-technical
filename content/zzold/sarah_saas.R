#Sarah Saas code for hsitogram for orientation 

library (readr)

file = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv"

github_data <-read_csv(url(file))

github_data

library(ggplot2)

# creating a histogram to show the distribution of CPU cycle rate across
# across MSDS students that filled out the survey

hist(github_data$'Hard Drive Size (in GB)')

ggplot(github_data, aes(github_data$`Hard Drive Size (in GB)`)) + 
  geom_histogram(bins = 6) + ggtitle("Histogram of Hard Drive Size (in GB)") +
  xlab("Hard Drive Size (GB)") + ylab("Count")





