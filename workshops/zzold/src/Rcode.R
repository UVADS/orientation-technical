

library(ggplot2)

data = `2022.06.14.survey`
data2 = data[-2,]

ggplot(data = data2) + geom_smooth(mapping = aes(x = RAM..in.GB., y = CPU.Cycle.Rate..in.GHz.))
ggplot(data = data2) + geom_smooth(mapping = aes(x = Operating.System, y = CPU.Cycle.Rate..in.GHz.))
ggplot(data = data2) + geom_point(mapping = aes(x = Operating.System, y = RAM..in.GB.))

ggplot(data = data2) + 
  geom_point(mapping = aes(x = RAM..in.GB., y = CPU.Cycle.Rate..in.GHz.)) + 
  facet_wrap(~Operating.System , nrow =2 )

hist(data2$)

ggplot(data = data2) + geom_bar(mapping = aes(x = data2$Operating.System))

min(data2$Timestamp)

data2$date = as.Date(data2$Timestamp)







