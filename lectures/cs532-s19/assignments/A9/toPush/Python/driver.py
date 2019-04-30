
import helper
dataFile = open("distanceFile.txt", 'a')
blognames,words,data = helper.readfile("blogdata.txt")
newline = '\n'
tab = '\t'

# print(blognames)

# line represents row of 1000 word counts
# for line in data:

#blogdata.txt f-meausre index 0  web science index 1

# Distance of k neighbors from f-measure blog
# f_measureDist = helper.knnestimate(data, data[0],1)

# Distance of k neighbors from web science blog
# web_ScienceDist = helper.knnestimate(data,data[1],1)

f_measureDist = helper.knnestimate(data, data[0],1)

dataFile.write(f'F-Measure for k=1 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

for x in f_measureDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'F-Measure for k=2 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
f_measureDist = helper.knnestimate(data, data[0],2)

for x in f_measureDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'F-Measure for k=5 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
f_measureDist = helper.knnestimate(data, data[0],5)

for x in f_measureDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'F-Measure for k=10 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
f_measureDist = helper.knnestimate(data, data[0],10)

for x in f_measureDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'F-Measure for k=20 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
f_measureDist = helper.knnestimate(data, data[0],20)

for x in f_measureDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')


#Data Science


dataFile.write(f'Data Science for k=1 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
web_ScienceDist = helper.knnestimate(data,data[1],1)

for x in web_ScienceDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'Data Science for k=2 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
web_ScienceDist = helper.knnestimate(data,data[1],2)

for x in web_ScienceDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'Data Science for k=5 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
web_ScienceDist = helper.knnestimate(data,data[1],5)

for x in web_ScienceDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'Data Science for k=10 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
web_ScienceDist = helper.knnestimate(data,data[1],10)

for x in web_ScienceDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')

dataFile.write(f'Data Science for k=20 {newline}')
dataFile.write(f'Distance {tab}{tab}{tab} Index {newline}{newline}')

dataFile.write(f'{newline}{newline}')
web_ScienceDist = helper.knnestimate(data,data[1],20)

for x in web_ScienceDist:
	dataFile.write(f'{x[0]} {tab}{tab} {x[1]} {newline}')


#print(helper.knnestimate(data, data[0], 2))

# count_vectorizer = CountVectorizer()
# sparse_matrix = count_vectorizer.fit_transform(documents)


# print(cosine_similarity(sparse_matrix, sparse_matrix))
