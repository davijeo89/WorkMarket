##This script plots the frequency of alphanumeric characters in my plain text resume. My resume was copied and pasted from MS Word. I made no changes to it. 
import re
from collections import Counter
#import plotly
#import plotly.graph_objs
import numpy as np
import matplotlib.pyplot as plt

with open('resumetext.txt', 'r') as resume:
    resumetext = resume.read().replace('\n', '') ##Reading my plain text resume

onlyalnum = re.sub(r'[^\w]', '', resumetext) ##Removing any symbols/whitespace
onlyalnum = onlyalnum.lower() ##Making all the letters lowercase

sortedcharacters = sorted(Counter(onlyalnum).items()) ##Counting and sorting the alphanumeric characters. The output does not include any non-exisiting characters. 
#In this case '8' does not show up in my resume anywhere, so '8' will be missing in my graph

character, freq = zip(*sortedcharacters)

##I like Plotly it makes nicer graphs. But Matplotlib is much faster
indexes = np.arange(len(character))
plt.bar(indexes, freq)
plt.xticks(indexes + 0.5, character)
plt.title('Frequency of Alphanumeric Characters in my Resume')
plt.ylabel('Frequency')
plt.xlabel('Character \n 8 is not present in my resume so it is absent from the graph')
plt.show()
