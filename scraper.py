i = 0
file = 0
line = 0
line_number = 0
line_str = 0
ln_str=0
n=0
lines=0
line_to_replace = 0
lineList = []

def findLineWithM3U(file): #return line as string
    with open(file) as f:
        for line in f:
            if 'm3u' in line:
                return re.findall("'(.*?)'", line)


def writeM3UtoFile(file, line_to_replace, ln_str):
    with open(file, 'r+') as f:
        lineList = []
        line = f.readlines()
        line[line_to_replace] = "ln_str"
        #if len(line) > int(line_to_replace):
        #lineList.insert(line_to_replace, ln_str)      #now we build an array of lines.
        #print(len(lineList))
        #print(lineList)
        f.writelines(lineList)
    #with open(file, 'w+') as fw:

        #with open('vietchannels.m3u', 'w') as file: #write to file
        #f.writelines(ln_str)
        #type(lineList)

#read URLs text file
with open('urls.txt') as urlf:
    import urllib
    for line in urlf:
        i+=1
        urllib.request.urlretrieve(line, "%s.txt" % i) #create and save to new file

        n+=2
        line_str = findLineWithM3U("%s.txt" % i) #open file and find str M3U
        if len(line_str) > 0:
            s = line_str[1]

        with open('vietchannels.m3u', 'r+') as f:
            li = f.readlines()
            if len(li) > int(n):
                li[n] = s
                f.writelines(li)
            #print(s)
        #writeM3UtoFile('vietchannels.m3u', n, s )

        #print(n)
        #print(a[1])
        #print(line);
