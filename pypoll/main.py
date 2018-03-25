
import pandas as pd
import datetime
import numpy as np

df = pd.read_csv('election_data_1.csv')

totalvotes = len(df)

candidates = len(df.drop_duplicates('Candidate'))

print("\n Election Results \n --------------------\n",\
       "Total Votes: " + str(totalvotes),\
       "\n ---------------------\n",\
       "\n Total Candidates: " + str(candidates), \
       "\n \n Candidate Names: \n")

series1 = pd.Series(list(df.drop_duplicates('Candidate').iloc[:,2]))

print(" " + series1)

print("\n \n Candidate Total Votes: \n")

print(df.Candidate.value_counts())

print("\n \n Candidate Vote Counts: \n")

print(df.Candidate.value_counts()/ len(df))

print("\n \n AND THE WINNER IS......\n ........ \n ......\n")

df= df.Candidate.value_counts()

print(df.iloc[0])

