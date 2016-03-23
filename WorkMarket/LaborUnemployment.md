---
title: "Change in Labor Productivity and Unemployment"
author: "David Lara"
date: "March 19, 2016"
output: html_document
---
Here we look at the quarterly non-farm labor productivity in America since 1948 and compare it to the quarterly non-farm unemployment rate. Both data sets are from the Bureau of Labor Statistics. The labor productivity is the percent change from the previous quarter. The labor productivity is the percent change from the previous quarter. I could not get the API pulldown to work so I exported the data into Excel and preprocessed the data a bit (change the format, I stripped the title and explanations and then transposed the data) to make it more compatible with R.

The stacking warning is expected and is caused by the labor productivity values being negative and positive.  

```
## Warning: Stacking not well defined when ymin != 0
```

![plot of chunk plot](figure/plot-1.png)

Understandably, there is a sharp decrease in labor productivity during a recession as unemployment rate increased. What is interesting is the gradual depression (i.e. decrease) of the change in productivity. In other words, pre-computer age there were large increases in labor productivity greater than 10%, sometimes more than 20%. In more recent times, change in labor productivity has been no more and has hovered around 5% since the Great Recession. My theory is the shift of manufacturing jobs from Stateside to oversees. I am assuming the main driver in productivity is manufacturing. What drives increases in productivity is newer technology and/or better utilization of resources. But as the labor force in America has shifted to inside an office and sitting at a desk there is only so much one can do to make the average office worker more productive. The decreasing in the changes to labor productivity could also be the decrease in major techonology advances. Right after WWII, America had a large increase in working men returning from the war looking for work. Followed by great advances in science and technology. While in the past 15 years, we have seen faster computers. But the increase in processing speed is not as substantial as the invention of the computer. Another interesting note is the large changes in labor productivity during the 1970s. Right around when baby boomers turned 20-30 years old. 


