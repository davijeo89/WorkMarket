---
title: "FriendlyCompetition"
author: "David Lara"
date: "March 18, 2016"
output: html_document
--
TThis report is for my application to Work Market as an analyst.  It looks at the job postings in NYC and reports on various topics.

This first tasked that was asked was to find the agency with the most job postings. I found it was the Department of Buildings with 502 total job postings. But this includes same job posted internally and externally.


```r
totaljobs = tapply(data$X..Of.Positions, data$Agency, sum)  ##This sums the number of job openings for each agency.
totaljobs = data.frame(totaljobs)
mostjobs = totaljobs[which(totaljobs$totaljobs == max(totaljobs$totaljobs)), ] ##Finds the agency with the most jobs 
mostjobs
```

```
## DEPARTMENT OF BUILDINGS 
##                     502
```
We can look at the most unique jobs, which turned out to be the Department of Health with 240 postings.


```r
jobs = data %>% 
  select(Agency, Business.Title, X..Of.Positions) %>% unique()
totaljobs = tapply(jobs$X..Of.Positions, jobs$Agency, sum)  ##This sums the number of job openings for each agency.
totaljobs = data.frame(totaljobs)
mostjobs = totaljobs[which(totaljobs$totaljobs == max(totaljobs$totaljobs)), ] ##Finds the agency with the most jobs 
mostjobs
```

```
## DEPT OF HEALTH/MENTAL HYGIENE 
##                           240
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
##                      Agency Salary.Range.From Salary.Range.To
## 22 DEPARTMENT OF CORRECTION                69              71
##    Salary.Frequency
## 22           Hourly
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
##                             Agency Salary.Range.From Salary.Range.To
## 202 DEPT OF ENVIRONMENT PROTECTION            198518          198518
##     Salary.Frequency
## 202           Annual
```

```r
max_annual_to
```

```
##                            Agency Salary.Range.From Salary.Range.To
## 269 DEPT OF HEALTH/MENTAL HYGIENE            142859          204122
##     Salary.Frequency
## 269           Annual
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
## 9 OFFICE OF COLLECTIVE BARGAININ                 9              10
##   Salary.Frequency
## 9           Hourly
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
##                            Agency Salary.Range.From Salary.Range.To
## 102 DEPT OF HEALTH/MENTAL HYGIENE             26869           30899
##     Salary.Frequency
## 102           Annual
```

```r
min_annual_to
```

```
##                            Agency Salary.Range.From Salary.Range.To
## 196 DEPT OF HEALTH/MENTAL HYGIENE             29437           29437
##     Salary.Frequency
## 196           Annual
```
Finally, I determined the jobs that are hardest to fill. This is more challenging since we can look at multiple variables. Many variables can be both consequential and beneficial for HR to fill. For instance, highest paying jobs probably require the most experience and/or education which shrinks the job pool. But with only a handful of qualified applicants, the decision might be easier but a higher pay might attract more candidates. Conversely, an entry-level position might have thousands of applicants for one position. HR might have to shift through hundreds of those and interview tens of people to find a qualified hire. Jobs that have been posted the longest time might be hard to fill. This could also because the hiring manager forgot to remove the posting after a hire was made. We can also look at the shifts the applicant would be working. A third shift might not be as appealing and therefore be harder to fill.  In effort to complete this task and send in my application to Work Market I will look at two variables. Reserve more dicussion and research for a later date.

The two variables this report looks at are: 

1. Posting date
  + The longer the jobs has been posted is assumed to be harder to fill

2. Job description 
  + Particularly, I searched for whether a higher degree is looked for (Master's or Doctorate). A job that requires a Doctorates's or more is assumed to be harder to fill

I orginally planned to look at internal vs external job postings. Going through the analysis, I found that most the jobs were posted both internally and externally. So the posting type was not a useful factor to consider. I also planned to differeniate masters's and doctornal requirements. But after looking at postings the qualification listed both as requirements. 


```r
jobfilling = data %>% select(Agency, Business.Title, Minimum.Qual.Requirements, Posting.Date) %>% unique()
##Selecting the agency, title and qualifications
jobfilling$Posting.Date = as.Date(jobfilling$Posting.Date, format="%m/%d/%Y") ##Converting to POSIXT time 

Doctors = jobfilling[grep("docto" , jobfilling$Minimum.Qual.Requirements, ignore.case = TRUE), ] ##There are no postings that list a 'Ph.D' or 'phd'. So only docto* is searched for


postings = Doctors[order(Doctors$Posting.Date, decreasing = FALSE), ]

head(postings %>% select(Agency, Business.Title, Posting.Date))
```

```
##                             Agency
## 7   DEPT OF ENVIRONMENT PROTECTION
## 105  DEPT OF HEALTH/MENTAL HYGIENE
## 20   DEPT OF HEALTH/MENTAL HYGIENE
## 198  DEPT OF HEALTH/MENTAL HYGIENE
## 200  DEPT OF HEALTH/MENTAL HYGIENE
## 215  DEPT OF HEALTH/MENTAL HYGIENE
##                                                                                         Business.Title
## 7                                                                                      Project Manager
## 105                                                           Clinical Systems Integration Coordinator
## 20                                            Research Analyst, Family and Child Health Administration
## 198                                Sentinel Laboratory Trainer, Bureau of the Public Health Laboratory
## 200                                                       City Research Scientist, Bureau of Childcare
## 215 Section Chief for Environmental Water & Sciences, Bureau of Environmental Sciences and Engineering
##     Posting.Date
## 7     2013-07-31
## 105   2014-04-09
## 20    2014-09-24
## 198   2014-10-22
## 200   2014-10-23
## 215   2014-10-28
```
There turns out to be 24 jobs where HR is looking for a Doctoratal candinate. The oldest posting, and hardest to fill in this analysis, is the Project Manager in the Department of Enviromental Sciences. The Department of Health tops this analysis in jobs hardest to fill. 


