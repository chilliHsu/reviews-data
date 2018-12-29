import jieba
import pandas as pd

#獲得該app的評論、日期、跟分數
def getData():
	name = 'com.yilegame.mshztw.android.csv'
	df = pd.read_csv(name)

	reviews = df['reviews']
	scores = df['Score']
	dates = df['Date']

	return reviews,scores,dates

positiveW = []
nagativeW = []

reviews,scores,dates = getData()
for index in range(len(scores)):
	seg_list = jieba.cut(reviews[index])
	if scores[index] == 5:
		for word in seg_list:
			#print(i)
			if word not in positiveW and len(word) > 1:
				positiveW.append(word)
	elif scores[index] == 1:
		for word in seg_list:
			if word not in nagativeW and len(word) > 1:
				nagativeW.append(word)

print("positiveword",positiveW)
print("-----------------------------------------------------")
print("nagativeword",nagativeW)


	


