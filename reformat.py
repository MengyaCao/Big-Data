f = open('ak.txt')
string = ''
for line in f :
    string = string + line.strip() + ' '
f.close()
string = string.replace('.', '\n')
f = open('ak.txt', 'w')
f.write(string)
f.close()
