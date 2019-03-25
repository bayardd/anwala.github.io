import networkx as nx
import matplotlib.pyplot as plt
import itertools

# Function for original Karate Club graph
def plotKarateClub(G):
	
	plt.figure(figsize=(8,8))
	plt.axis('off')
	colorCode = []

	for i in G:
		print(i)
		print((G.node[i]["club"]))

		if(G.node[i]["club"] == "Officer"):
			colorCode.append("red")

		else:
			colorCode.append("cyan")

	nx.draw_networkx(G, node_color=colorCode)


	plt.show()




def edgeToRemove():
	G=nx.karate_club_graph()

	# Key holds edge and value holds edge betweenness
	dict1 = nx.edge_betweenness_centrality(G)
	listTuples = dict1.items()
	print(type(listTuples))
	listTuples.sort(key = lambda x:x[1], reverse = true)
	return listTuples[0][0]


def plotKarateGirvanNewman(G):
	c = nx.connected_component_subgraphs(G)
	print(type(c))
	components = sum(1 for x in c)

	print('Connected Components', components)


	while(components != 2):
		G.remove_edge(*edgeToRemove(G))
		c = nx.connected_component_subgraphs(G)
		components = len(c)
		print("num of comp.", components)


def girvan_newman ():

	G=nx.karate_club_graph()
	formattedGraph = nx.karate_club_graph()
	formattedGraph.clear()

	plt.figure(figsize=(8,8))
	plt.axis('off')

	edges = G.edges()

	for x in range(0,34):
		formattedGraph.add_node(x)
	


	for edge in edges:

		a = edge[0]
		b = edge[1]
		# print(a)
		# print(b)
		formattedGraph.add_edge(a,b,color ="black")

	colors = [formattedGraph[u][v]['color'] for u,v in formattedGraph.edges()]

	# nx.draw_networkx(formattedGraph, edge_color=colors)
	# plt.show()

	# print(G.edges())
	# print(formattedGraph.edges())
	# print(formattedGraph.number_of_edges())

	if len(G.nodes()) == 1:
		return [G.nodes()]

	def find_best_edge(G0):
		"""
		Networkx implementation of edge_betweenness
		returns a dictionary. Make this into a list,
		sort it and return the edge with highest betweenness.
		"""

		eb = nx.edge_betweenness_centrality(G0)
		
		sortedDict = (sorted(eb.items(), key=lambda key: key[1], reverse=True))

		
		return sortedDict[0][0]

	components = nx.connected_component_subgraphs(G)
	x = sum(1 for x in components)
	while x < 5:
		x = sum(1 for x in components)
		colorCode = []
		plt.figure(figsize=(8,8))
		plt.axis('off')

		# edge = (find_best_edge(G))

		# counter = 0

		# for x in range(0, 78):
		# 	counter = counter+1
		# print(counter)



		# edge1 = (edge[0])
		# edge2 = (edge[1])

		for test in G:
			
			if(G.node[test]["club"] == "Officer"):
				colorCode.append("red")


			else:
				colorCode.append("cyan")

		toFormat = (find_best_edge(formattedGraph))
		print(toFormat)


		

		# Remove Original Node
		formattedGraph.remove_edge(*find_best_edge(formattedGraph))

		# Add formatted Node
		formattedGraph.add_edge(*toFormat, color="blue")
		# Draw Graph
		colors = [formattedGraph[u][v]['color'] for u,v in formattedGraph.edges()]
		nx.draw_networkx(formattedGraph, node_color = colorCode, edge_color = colors)

		# Plot Graph
		# plt.show()
		# print("test")
		# Remove Node
		formattedGraph.remove_edge(*find_best_edge(formattedGraph))
		
		components = nx.connected_component_subgraphs(formattedGraph)

	plt.show()

	result = [c.nodes() for c in components]
	
	for c in components: 
		result.extend(girvan_newman(c))

	return result

girvan_newman();

