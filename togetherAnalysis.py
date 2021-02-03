import pyspark
import re
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
text_file = pyspark.SparkContext().textFile('ak.txt')
text_file = text_file.filter(lambda line : line != '' and 'PART' not in line and 'Chapter' not in line)
text_file = text_file.map(lambda line : line.lower())
#text_file = text_file.flatMap(lambda line : line.split(" "))
text_file.saveAsTextFile('tA-prepped')

def keysfor(line) :
    answer = []
    words = []
    wordspre = sorted(line.replace('—', ' ').split(' '))
    for i in range(0, len(wordspre)) :
        if wordspre[i] != '' and wordspre[i] not in stops :
            words.append(ps.stem(re.sub(r'[^\w\s_]', '', wordspre[i])))
    for w1 in words :
       for w2 in words :
           if w1 < w2 :
               answer.append((w1, w2))
    return answer;

mapped = text_file.flatMap(keysfor)
mapped = mapped.map(lambda list : (list, 1))
mapped.saveAsTextFile('tA-mapped')

reduced = mapped.reduceByKey(lambda a, b : a + b)
reduced = reduced.sortBy(lambda pair : pair[1], ascending=False)
reduced.saveAsTextFile('tA-reduced')


