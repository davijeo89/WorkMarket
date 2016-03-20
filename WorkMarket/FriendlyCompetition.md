---
title: "FriendlyCompetition"
author: "David Lara"
date: "March 18, 2016"
output: html_document
---
This report is for my application to Work Market as an analyst. But also any other companies that are looking to hire an entry-level analyst.  It looks at the job postings in NYC
and reports on various topics. 

This first tasked that was asked was to find the agency with the most job postings. I found it was 
the Department of Buildings with 502 total job postings

```r
totaljobs = tapply(data$X..Of.Positions, data$Agency, sum)  ##This sums the number of job openings for each agency.
```

```
## Error in FUN(X[[i]], ...): invalid 'type' (character) of argument
```

```r
totaljobs = data.frame(totaljobs)
```

```
## Error in data.frame(totaljobs): object 'totaljobs' not found
```

```r
mostjobs = totaljobs[which(totaljobs$totaljobs == max(totaljobs$totaljobs)), ] ##Finds the agency with the most jobs 
```

```
## Error in eval(expr, envir, enclos): object 'totaljobs' not found
```

```r
mostjobs
```

```
## Error in eval(expr, envir, enclos): object 'mostjobs' not found
```
The next task was to find the agency with the highest paying positions. This is slighly more nuanced, since the postings were both salaried and hourly and the postings gave a range of pay. I split the postings into hourly and salaried to report the highest paying upper and lower salaries for both types. I found the Department of Health, the Department of Corrections and the Department of Enviromental Protection all have the highest paid postings. 

I did not look at number of shift hours. But that would also affect salaries of hourly employees.

```r
##using some ddplyr. I selected the hiring agencys and salary ranges and employment type. Since most postings are repeated for internal and external, unique() removes any duplicative postings
salaryinfo = data %>% 
  select(Agency, Salary.Range.From, Salary.Range.To, Salary.Frequency) %>% unique()

##Creating 2 tables one with salaried employees the other with hourly employees.
Annum = filter(salaryinfo, Salary.Frequency == "Annual")
Hourly = filter(salaryinfo, Salary.Frequency == "Hourly")

##Finding the max salaries
max_hourly_from = Hourly[which(Hourly$Salary.Range.From == max(Hourly$Salary.Range.From)), ]
max_hourly_to = Hourly[which(Hourly$Salary.Range.To == max(Hourly$Salary.Range.To)), ]

max_annual_from = Annum[which(Annum$Salary.Range.From == max(Annum$Salary.Range.From)), ]
max_annual_to = Annum[which(Annum$Salary.Range.To == max(Annum$Salary.Range.To)), ]
max_hourly_from
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 9 OFFICE OF COLLECTIVE BARGAININ                 9              10
##   Salary.Frequency
## 9           Hourly
```

```r
max_hourly_to
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 18 DEPT OF HEALTH/MENTAL HYGIENE                65              83
##    Salary.Frequency
## 18           Hourly
```

```r
max_annual_from
```

```
##                            Agency Salary.Range.From Salary.Range.To
## 36 DEPT OF ENVIRONMENT PROTECTION             92899          102263
##    Salary.Frequency
## 36           Annual
```

```r
max_annual_to
```

```
##                             Agency Salary.Range.From Salary.Range.To
## 135 HOUSING PRESERVATION & DVLPMNT             66970           98864
##     Salary.Frequency
## 135           Annual
```

The Department of Collective Bargining has the lowest hourly rates. The Department of Health has the lowest annual salaries. 


```r
##Finding the min salaries
min_hourly_from = Hourly[which(Hourly$Salary.Range.From == min(Hourly$Salary.Range.From)), ]
min_hourly_to = Hourly[which(Hourly$Salary.Range.To == min(Hourly$Salary.Range.To)), ]

min_annual_from = Annum[which(Annum$Salary.Range.From == min(Annum$Salary.Range.From)), ]
min_annual_to = Annum[which(Annum$Salary.Range.To == min(Annum$Salary.Range.To)), ]
min_hourly_from
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 10 DEPT OF HEALTH/MENTAL HYGIENE                10              14
##    Salary.Frequency
## 10           Hourly
```

```r
min_hourly_to
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 9 OFFICE OF COLLECTIVE BARGAININ                 9              10
##   Salary.Frequency
## 9           Hourly
```

```r
min_annual_from
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 93      DEPARTMENT OF CORRECTION            100000          120000
## 185 CIVILIAN COMPLAINT REVIEW BD            100000          120000
##     Salary.Frequency
## 93            Annual
## 185           Annual
```

```r
min_annual_to
```

```
##                           Agency Salary.Range.From Salary.Range.To
## 50       DEPARTMENT OF BUILDINGS             49492          100000
## 68  DEPT OF INFO TECH & TELECOMM             81290          100000
## 104 DEPT OF INFO TECH & TELECOMM             49492          100000
## 221      DEPARTMENT OF BUILDINGS             51757          100000
##     Salary.Frequency
## 50            Annual
## 68            Annual
## 104           Annual
## 221           Annual
```
Finally, it was tasked to detemine the jobs that are hardest to fill. This is more challanging since we can look at multiple variables. Many variables can be consequential and benefical for HR to fill. For instance, highest paying jobs probably require the most experience and/or education which shrinks the job pool. But with only a handful of qualified applicants, the decison might be easier. Conversly, an entry-level position might have thousands of applicants for one position. And HR might have to shift through hundreads of those and interview tens of people to find a qualifed hire. In addition, jobs that have been posted the longest time might be hard to fill. This could also because the hiring manager forgot to remove the posting after a hire was made. We can also look at the shifts the applicant would be working. A third shift might not be as appealing and therfore be harder to fill. We can look at job descripton as well. In effort to complete this task and send in my application to Work Market I will look at three variables. Reserve more dicussion for a later date.

The three varaibles this report looks at are: 

1. Posting date
  + The longer the jobs has been posted is assumed to be harder to fill

2. Job description 
  + Particularly, I searched for years of experience and whether a higher degree is looked for (master's or Doctorate). A job that requires a Master's or more is assumed to be harder to fill

I orginally considered looking at internal vs external job postings. Going through the analysis, I found that all the postings were both internal and external. So the posting type was not a useful factor to consider.


```r
jobfilling = data %>% select(Agency, Business.Title, Posting.Type, Minimum.Qual.Requirements, Posting.Date)

Masters = jobfilling[grep("Master", jobfilling$Minimum.Qual.Requirements, ignore.case = TRUE), ]  ##Since there were only 2 postings (<1% of all postings) which named a MBA so these were ignored. 
Doctors = jobfilling[grep("docto" , jobfilling$Minimum.Qual.Requirements, ignore.case = TRUE), ] ##There are no postings that list a 'Ph.D' or 'phd'. So only docto* is searched for
jobfilling$Posting.Date = dmy(jobfilling$Posting.Date)
```

```
## Warning: All formats failed to parse. No formats found.
```

```r
postings = Masters[order(Masters$Posting.Date, decreasing = TRUE), ]
```





