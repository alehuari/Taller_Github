fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if line.startswith('From:',0,5):
       continue
    if line.startswith('From',0,4):
       words=line.split()[1]
       print(words)
       count += 1
print("There were", count, "lines in the file with From as the first word")