import BioPythonFunctions as bpf
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def simple_scores_plot(df):
	lev=[1,2,3,4,5,6] 
	fig = plt.scatter(df['cnt'],  df['scores'], c=df['scores'],marker='H',s=200, cmap='copper')
	plt.grid(which='major', axis='y', color='grey', linestyle='--', linewidth=0.35)
	plt.grid(which='major', axis='x', color='lightgrey', linestyle='--', linewidth=0.2)
	plt.minorticks_on()
	plt.xticks(ticks=df['cnt'], labels=df['seq'])
	plt.yticks(ticks=lev, labels=lev)
	plt.tick_params(axis='both', which='both', length = 0)
	plt.margins(y=0.3)
	for index, row in df.iterrows():
		plt.text(row['cnt'], row['scores'], row['seq'], horizontalalignment='center', verticalalignment='center', size='medium', color='white', weight='semibold')
	
	return(fig)	

def plot_scores(df,chunksize):
	numchunks=sqlen//chunksize +1
	i=0
	n=1
	plt.figure(figsize=(20, 15), dpi=80)
	while i < sqlen:
		subdf=df.iloc[i:i+chunksize]	
		plt.subplot(numchunks,1,n)
		simple_scores_plot(subdf)
		i+=chunksize
		n+=1
	plt.suptitle('FLEXIBILITY SCORE BY RESIDUE', y=0.93 , size=35)
	plt.subplots_adjust(hspace=0.35)
	plt.savefig('flex_score_by_residue.png')
	sys.stderr.write("Scores figure written in flex_score_by_residue.png file\n")

if __name__ == "__main__":

	infasta=bpf.get_fasta("P38401.fasta")
	query_seq=infasta[1]
	sqlen=len(query_seq)

	scores=[random.randint(1,6) for x in range(sqlen)]
	df = pd.DataFrame(
		{'cnt':[x for x in range(sqlen)],
		'seq':[char for char in query_seq], 
		'scores': scores }
		)

	plot_scores(df,60)

