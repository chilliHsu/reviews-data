import jieba
import pandas as pd
import os
import re

#獲得該app的評論、日期、跟分數
def getData(name):
	df = pd.read_csv(name+'.csv')

	reviews = df['reviews']
	scores = df['Score']
	dates = df['Date']

	return reviews,scores,dates

def save_excel(words,count,label):
	dict = {"word list " : words,"frequency":count} #save relevant data into dataframe
	save_df = pd.DataFrame(dict)
	save_df.to_excel(writer,label) #將csv檔存在review-data資料夾中

def getAllFile():
	
	path='./'
	files = os.listdir(path)
	csvfile = []
	for file in files:
		if file[-4:] == '.csv':
			print(file[:-4])
			csvfile.append(file[:-4])
	
	#csvfile = ['com.playrix.homescapes']
	return csvfile

positiveW = []
positiveCount = []
negativeW = []
negativeCount = []

gamefiles = getAllFile()

for game in gamefiles:
	name = game
	#print(game)
	reviews,scores,dates = getData(name)
	#print(reviews)

	for index in range(len(scores)):
		reviews[index] = re.sub(r'[^\u4e00-\u9fa5]',' ',str(reviews[index]))
		#print(reviews[index])
		seg_list = jieba.cut(reviews[index])
		if scores[index] == 5:
			for word in seg_list:
				#print(i)
				if len(word) > 1:
					if word not in positiveW :
						positiveW.append(word)
						positiveCount.append(1)
					else:
						pos = positiveW.index(word)
						positiveCount[pos]+=1
		elif scores[index] == 1:
			for word in seg_list:
				if len(word) > 1:
					if word not in negativeW :
						negativeW.append(word)
						negativeCount.append(1)
					else: 
						pos = negativeW.index(word)
						negativeCount[pos]+=1

	writer = pd.ExcelWriter('./jiebaword/'+name+'.xls')
	save_excel(positiveW,positiveCount,"positive")
	save_excel(negativeW,negativeCount,"negative")
	writer.save()
	print(name,"ok!!")

"""
print("positiveword",positiveW)
print("-----------------------------------------------------")
print("nagativeword",negativeW)
"""


	


