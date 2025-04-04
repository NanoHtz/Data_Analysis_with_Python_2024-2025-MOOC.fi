#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
	df = pd.read_csv("src/municipal.tsv", sep= "\t", index_col="Region 2018")
	subset = df.loc["Akaa":"Äänekoski",
		[
			"Population",
			"Share of Swedish-speakers of the population, %",
			"Share of foreign citizens of the population, %",
		],
	]
	return subset

def main():
	df = subsetting_with_loc()
	print(df)

if __name__ == "__main__":
    main()
