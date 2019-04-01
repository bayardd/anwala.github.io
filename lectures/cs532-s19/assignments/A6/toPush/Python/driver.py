import recommendations

allSimilar = []
file = open("data.txt", 'a')
newline = '\n'
tab = '\t'

file.write(f'First User Chosen: {tab} 368{newline}')
file.write(f'Second User Chosen: {tab} 81 {newline}')
file.write(f'Third User Chosen: {tab} 135 {newline}{newline}')

pref = recommendations.loadMovieLens()

# Get sorted list of user ratings
userRatings1 = (sorted(pref['368'].items(), key = 
             lambda kv:(kv[1], kv[0]))) 
userRatings2 = (sorted(pref['81'].items(), key = 
             lambda kv:(kv[1], kv[0]))) 
userRatings3 = (sorted(pref['135'].items(), key = 
             lambda kv:(kv[1], kv[0]))) 

# Get top 5 for each user
userRatings1.reverse()
userRatings2.reverse()
userRatings3.reverse()

# Formatted File output
file.write(f'First User Rating: {newline}')
file.write(f'ID 368 Top 3 Rated Movies: {newline}{newline}')

for x in range(0,3):
	name = userRatings1[x][0]
	rating = userRatings1[x][1]

	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')

file.write(f'{newline}ID 368 Bottom 3 Rated Movies: {newline}')
userRatings1.reverse()

for x in range(0,3):
	name = userRatings1[x][0]
	rating = userRatings1[x][1]

	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')


file.write(f'{newline}Second User Rating: {newline}')
file.write(f'ID 81 Top 3 Rated Movies: {newline}{newline}')

for x in range(0,3):
	name = userRatings2[x][0]
	rating = userRatings2[x][1]

	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')

userRatings2.reverse()
file.write(f'{newline}ID 81 Bottom 3 Rated Movies: {newline}{newline}')

for x in range(0,3):
	name = userRatings2[x][0]
	rating = userRatings2[x][1]

	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')


file.write(f'{newline}Third User Rating: {newline}')
file.write(f'ID 135 Top 3 Movies: {newline}{newline}')

for x in range(0,3):
	name = userRatings3[x][0]
	rating = userRatings3[x][1]

	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')

userRatings3.reverse()
file.write(f'{newline}ID 135 Bottom 3 Rated Movies: {newline}{newline}')

for x in range(0,3):
	name = userRatings3[x][0]
	rating = userRatings3[x][1]
	file.write(f'Name of Movie: {name} {tab} Rating: {rating} {newline}')

file.write(f'{newline}{newline}Substitute User ID: 368 {newline}{newline}')

# Find most correlated users
closest_5 = recommendations.topMatches(pref, '368')

# Find least correlated users
furthest_5 = recommendations.worstMatches(pref, '368')

# Output for least and most correlated users
file.write(f'Five other users with highest correlation: {newline}{newline}')
for x in closest_5:
	correlationValue = round(x[0])
	tempId = x[1]
	file.write(f'User ID:{tempId} {tab}Correlation Value: {correlationValue}{newline}')

file.write(f'{newline}Five other users with lowest correlation: {newline}')
for y in furthest_5:
	correlationValue = round(y[0])
	tempId = y[1]
	file.write(f'User ID:{tempId} {tab}Correlation Value: {correlationValue}{newline}')


recommendedMovies = recommendations.getRecommendations(pref, '368')

file.write(f'{newline}Computed Top 5 Movies to be Watched: {newline}')


for x in range(0,5):
	rating = recommendedMovies[x][0]
	name = recommendedMovies[x][1]
	file.write(f'Name of Movie: {name}{tab} Calculated Rating: {rating}{newline}')
 
file.write(f'{newline}Computed Bottom 5 Movies to be Watched: {newline}')
recommendedMovies.reverse()
for y in range(0,5):
	rating = recommendedMovies[y][0]
	name = recommendedMovies[y][1]
	file.write(f'Name of Movie: {name}{tab} Calculated Rating: {rating}{newline}')

file.write(f'{newline}{newline}Favorite Movie: {tab} Jurassic Park (1993){newline}')
file.write(f'Least Favorite Movie: {tab} Children of the Corn: The Gathering (1996){newline}{newline}')


similarMovies = recommendations.calculateSimilarItems(pref)
notSimilarMovies = recommendations.calculateLeastSimilarItems(pref)
file.write(f'Top Recommended Movies to be Watched for Jurassic Park: {newline}')
# print(similarMovies['Jurassic Park (1993)'])
for x in similarMovies['Jurassic Park (1993)']:
	name = x[1]
	rating = x[0]
	file.write(f'Name of Movie: {name}{tab} Calculated Correlation: {rating}{newline}')

file.write(f'{newline}Bottom Recommended Movies to be Watched for Jurassic Park{newline}')


for x in notSimilarMovies['Jurassic Park (1993)']:
	name = x[1]
	rating = x[0]
	file.write(f'Name of Movie: {name}{tab} Calculated Correlation: {rating}{newline}')

file.write(f'{newline}Top Recommended Movies to be Watched for Children of the Corn: {newline}')

for x in similarMovies['Children of the Corn: The Gathering (1996)']:
	name = x[1]
	rating = x[0]
	file.write(f'Name of Movie: {name}{tab} Calculated Correlation: {rating}{newline}')

file.write(f'{newline}Bottom Recommended Movies to be Watched for Children of the Corn{newline}')

for x in notSimilarMovies['Children of the Corn: The Gathering (1996)']:
	name = x[1]
	rating = x[0]
	file.write(f'Name of Movie: {name}{tab} Calculated Correlation: {rating}{newline}')