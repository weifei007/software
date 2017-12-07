#!/usr/bin/env python
#coding=utf8
import sys
if len(sys.argv)<5:
	print "\tpython cor_pic.py <cluster|corr> <data> <outdir> <corr:corr file> <corr|cluster pic file>\n"
	sys.exit()


import pandas as pd
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
#plt.style.use("ggplot")
#rc={'axes.labelsize': 2, 'font.size': 2, 'legend.fontsize': 2.0, 'axes.titlesize': 2}
#plt.rcParams.update(rc)
class Pic():
	def __init__(self,data,outdir):
		self.data=data
		self.outdir=outdir
	def _getcorr(self):
		dfile=self.data
		dat=pd.read_table(dfile,sep="\t")
		datcorr=dat.corr(method='pearson')
		return datcorr
	def output(self,name):
		info=self._getcorr()
		type(info)
		outdir=self.outdir
		outf=outdir+"/"+name
		info.to_csv(outf,sep="\t")
	def corrpic(self,name):
		outd=self.outdir
		picname=outd+"/"+name
		corr=self._getcorr()
		sns.set(font_scale=0.8)
		fig,ax=plt.subplots()
		plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
		sns.heatmap(corr,cmap='RdBu_r',linewidths=0.05,ax=ax,vmin=-1,vmax=1,annot=True,annot_kws={"size":5})
		ax.set_title('Correlation between features')
		ax.set_xticklabels(ax.get_xticklabels(),rotation=-90)
		plt.savefig(picname,dpi=300)
	def cluster(self,name):
		#da=self._getcorr()
		da=pd.read_table(self.data,sep="\t",index_col=0)
		outd=self.outdir
		picname=outd+"/"+name
		sns.set(font_scale=0.8)
		fig,ax=plt.subplots()
		sns.clustermap(da,annot=True,cmap='Blues',annot_kws={"size":5})
		plt.savefig(picname,dpi=300)
if __name__=="__main__":
	if sys.argv[1]=="corr":
		Step=Pic(sys.argv[2],sys.argv[3])
		Step.output(sys.argv[4])
		Step.corrpic(sys.argv[5])
	elif sys.argv[1]=="cluster":
		Step=Pic(sys.argv[2],sys.argv[3])
		Step.cluster(sys.argv[4])

		
		
		
		
