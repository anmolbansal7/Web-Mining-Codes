#Anmol Bansal 19BCE0630

#Graph Input
# graph = {
#     "a" : ["b", "e", "f"],
#     "b": ["a", "c"],
#     "c": ["b", "d", "f"],
#     "d": ["c", "g"],
#     "e": ["a", "i"],
#     "f": ["a", "c", "g", "j"],
#     "g": ["d", "f", "h", "k"],
#     "h": ["g", "l", "o"],
#     "i": ["e", "j", "m", "n"],
#     "j": ["f", "g", "i", "n", "o"],
#     "k": ["g", "o"],
#     "l": ["h", "p"],
#     "m": ["i"],
#     "n": ["i", "j", "o"],
#     "o": ["j", "k", "h", "n", "p"],
#     "p": ["o", "l"]
#     }

graph = {
    "1" : ["2", "3", "4"],
    "2" : ["4", "5"],
    "3" : ["6"],
    "4" : ["3", "6", "7"],
    "5" : ["4", "7"],
    "6" : [],
    "7" : ["6"]
    }


#Degree Centrality
degreeC = dict()

for i in graph.keys():
    degreeC[i] = (len(graph[i])/(len(graph)-1))

print("\nDegree Centrality: \n")
print(degreeC)


# Shortest Path Function
def find_shortest_path(graph, start, end, path =[]):
		path = path + [start]
		if start == end:
			return path
		shortest = None
		for node in graph[start]:
			if node not in path:
				newpath = find_shortest_path(graph, node, end, path)
				if newpath:
					if not shortest or len(newpath) < len(shortest):
						shortest = newpath
        if shortest == None:
            return [None]
        
		return shortest

#Closeness Centrality
def getCentrality(graph, node):
    temp = list(set(graph.keys()) - {node})
    close = [len(find_shortest_path(graph, node, i)) - 1 for i in temp]
    d = sum(close)
    cc = (len(graph) - 1)/d
    
    return cc

closeC = dict()

for i in graph.keys():
    closeC[i] = (getCentrality(graph, i))

print("\nCloseness Centrality: \n")
print(closeC)


#Betweeness Centrality
betC = dict()
keys = list(graph.keys())
n = len(keys)

for i in keys:
    betC[i] = 0
    
for i in range(1, n):
    for j in range(i+1, n):
        temp = find_shortest_path(graph, keys[i], keys[j])[1:-1]
        for k in temp:
            betC[k] += 1
            
m = len(graph)
d = (m-1)*(m-2)/2
for i in betC.keys():
    betC[i] = betC[i]/d

print("\nBetweeness Centrality: \n")
print(betC)


#Degree Prestige
degreeP = dict()

for i in graph.keys():
    degreeP[i] = (len(graph[i])/(len(graph)-1))

print("\nDegree Prestige: \n")
print(degreeP)

#Proximity Prestige
proxP = dict()

for i in graph.keys():
    count = 0
    for j in graph.values():
        if i in j:
            count += 1
    proxP[i] = count

for i in proxP.keys():
    proxP[i] = proxP[i]/(len(graph) - 1)
   
print("\nProximity Prestige: \n")
print(proxP)