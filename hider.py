import os, itertools, sys
from itertools import combinations

fileToStore = sys.argv[1]
palabra = sys.argv[2]
permission = "400"
characters = []
allPaths = []
total = 0


# Create fake dir
try:
	os.makedirs("fake")
	os.makedirs("folders")
except:
	pass


#Create fake file
fileSize = os.path.getsize(fileToStore)
fileName = os.path.basename(fileToStore)
with open(("fake/"+fileName), "wb") as f:
    f.seek(fileSize-1)
    f.write("\0")


# Char list
for char in palabra:
	characters.append(char)


# Create all directories
for combination in itertools.product( characters, repeat= len(palabra)):
	path = "folders/"
	for char in combination:	
		path = path + char +"/"
	if path not in allPaths:
		try:
			os.makedirs(path)
			total += 1
			allPaths.append(path)
		except:
			pass

# Copy all files
for path in allPaths:
	try:
		if path.replace("/","") == ("folders"+palabra):
				os.system("cp "+fileToStore+" "+path)
		else:
				os.system("cp fake/"+fileName+" "+path)
	except:
		pass
	os.system("chmod "+permission+" "+path+"/"+fileName)

os.system("rm -r fake/")
