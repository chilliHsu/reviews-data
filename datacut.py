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
	save_df = save_df.sort_values(by='frequency',ascending=False)
	save_df.to_excel(writer,label) #將csv檔存在review-data資料夾中

def getAllFile():
	
	path='./'
	files = os.listdir(path)
	csvfile = []

	alreadyfiles = os.listdir('./jiebaword/')

	
	for file in files:
		if file[-4:] == '.csv':
			# print(file[:-4])
			if file[:-4]+'.xls' not in alreadyfiles:
				print(file)
				csvfile.append(file[:-4])
	
	# csvfile = ['com.playrix.homescapes']
	
	return csvfile

def getStopWord():
	stopWords=[]
	with open('./stopword/stopWords.txt', 'r', encoding='UTF-8') as file:
		for data in file.readlines():
			data = data.strip()
			stopWords.append(data)
	return stopWords


jieba.set_dictionary('./dictionary/dict.txt.big.txt') #繁體中文

gamefiles = getAllFile()
stopWords = getStopWord()

for game in gamefiles:
	positiveW = []
	positiveCount = []
	negativeW = []
	negativeCount = []
	name = game
	print(game)
	reviews,scores,dates = getData(name)
	# print(reviews)

	for index in range(len(scores)):
		reviews[index] = re.sub(r'[^\u4e00-\u9fa5]',' ',str(reviews[index]))
		#print(reviews[index])
		seg_list = jieba.cut(reviews[index])
		if scores[index] == 5:
			for word in seg_list:
				#print(i)
				if word not in stopWords and len(word)>1:
					if word not in positiveW :
						positiveW.append(word)
						positiveCount.append(1)
					else:
						pos = positiveW.index(word)
						positiveCount[pos]+=1
		elif scores[index] == 1:
			for word in seg_list:
				if word not in stopWords and len(word)>1:
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


print("positiveword",positiveW)
print("-----------------------------------------------------")
print("nagativeword",negativeW)



	


