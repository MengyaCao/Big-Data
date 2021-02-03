#each observation has the following information:
#[height (inches), weight (pounds), shoe size (US)]
training = [[68, 200, 10], 
 [74, 200, 12], 
 [72, 154, 10.5], 
 [65, 135, 8], 
 [60, 110, 5],
 [65, 100, 9],
 [63, 108, 8],
 [64, 145, 7.5],
 [71, 215, 10.5],
 [70, 145, 7]]  #observations used to train the classifier.
test = [68, 180, 10]  #0 is the correct classification.
answers = [0, 0, 0, 1, 1, 1, 1, 1, 0, 1] #correct classifications for training data
