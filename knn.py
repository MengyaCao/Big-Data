from math import sqrt
"""
THIS FUNCTION IS GIVEN TO YOU
Returns the euclidean distance between the two arrays.
(See tutorial).
"""
def dist(list1, list2) :
    sum = 0
    for i in range(0, len(list1)) :
        sum = sum + (list1[i] - list2[i]) * (list1[i] - list2[i])
    return sqrt(sum)
"""
YOU WRITE THIS FUNCTION.
Gets the distances between test and each of the training arrays in training.
The meaning of distances(a1, a2) is the list returned by the function.
The list returned is the list of distances (Euclidean) between each list in a1 (a1 is a list of lists) and the array a2.
Here's an example:
if a1 is [[1], [2], [3], [4]]
and a2 is [-1]
then distances(a1, a2) is [2, 3, 4, 5]. (Euclidean distance in one dimension is just difference).
"""
def b(training, test) :


"""
THIS FUNCTION IS GIVEN TO YOU
returns the index of topki which is the position of the largest number in distances.
This function is a shortcut which finds which index of distances and training (see knn function below) is the index of the array of training that is furthest from answer (see knn function below) out of all the indexes stored in the topki array.
"""
def maximum(topki, distances) :
    maxi = -1
    for i in range(0, len(topki)) :
        if maxi < 0 or distances[topki[maxi]] < distances[topki[i]] :
            maxi = i
    return maxi

"""
THIS FUNCTION IS GIVEN TO YOU
This function examines a single index (newinsert) and puts that index
This function chooses the k observations closest to test out of up to k+1 observations
somewhere on the topki list, if either (1) that index refers to a distance in the distances lists that is smaller than the distance in distances refered to by any index already in topki or (2) the topki list has fewer than k things in it.

This function always returns the index stored in the topki list which refers to the largest distance in distances of all indexes in the topki list.
"""
def topkinsert(topki, maxi, distances, newinsert, k) :
    if len(topki) == 0 :
        topki.append(newinsert)
        return 0
    if len(topki) < k :
        topki.append(newinsert)
        return maximum(topki, distances)
    elif distances[newinsert] < distances[topki[maxi]] :
        topki[maxi] = newinsert
        return maximum(topki, distances)
    else :
        return maxi

"""
YOU WRITE THIS FUNCTION
Classifies the test data according to the training data using
the k-nearest neighbors classification scheme.  k is the number of
nearest neighbors to use.
"""
def knn(training, answer, test, k) :
	#(1) first make an array of all the distances between
	#an array in training and test (use the distances function you
	#wrote above).
	distarray=distances(taining, test)
    #(2) Make topki an empty list with nothing in it
	#this will be a list that stores the indexes of k-nearest points
	#in the training set to test.
	topki = []
    #(3) make a name maxi which means -1 
	#maxi is used in topkinsert to make sure that after the loop (step (4)) 
	#terminates, topki will be defined correctly.
	maxi = -1
	#(4) make a loop that has limits from the first index in the training
	#array to the and terminates with the last index of the training
	#array.  
	for i in range(0,len(training):
		maxi=topkinsert(topki, maxi, distarray, i, k):
		
	
		#(4a) change the meaning of maxi to be whatever the function 
		#topkinsert returns.  topkinsert should have the arguments:
		#(topki, maxi, the distances array from step (1), the loop variable 
		#       which is an index of training, k)
	#(5) make a variable count and set it equal to zero.
	count=0
	#(6) make a loop that starts at the first number stored in topki
	#and terminates with the last number stored in topki.
	for item in topki:
		if maxi==1:
		count+=1
	if count>k/2:
		return 1
	elif:
		return 0
	
		#(6a) if the answers array classifies the loop variable
		#as a 1 then make count mean one more than it used to mean.
		#(the name that's part of the loop control structure:
		#for ______ in ..... (it's the blank)) .
	#(7) after the loop terminates, if count is more k/2,
	#return 1
	#(8) return 0.

training = [[1, 3], [5, 2], [4, 7], [-3, 6], [-2, 4], [5, -7], [2, -2], [-1, -1], [1, 1]]
test = [-3, -3]
answers = [1, 1, 1, 0, 0, 0, 0, 0, 0]

print(knn(training, answers, test, 1))
