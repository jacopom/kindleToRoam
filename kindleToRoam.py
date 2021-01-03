import json
from itertools import groupby    

lines = []
with open('My Clippings.txt', mode='r', encoding='utf-8-sig') as f:
    lines = f.readlines()


titles, authors, highlights = [],[],[]

for line in range(0, (len(lines)), 5):
    titles.append(
    lines[line].split('(',1)[0][:-1]
    )
    authors.append(
    lines[line].rsplit('(',1)[1][:-2]
    )

for line in range(3, (len(lines)), 5):
    highlights.append(
    lines[line]
    )

result = zip(titles, authors, highlights)
listResult = (list(result))

groups = []

data = sorted(listResult, key=lambda x: x[0])
for k, g in groupby(data, lambda x: x[0]):
    groups.append(list(g))

def createMd(book):
    f = open(f"{(groups[book][0][0])}.md", "w")
    authorBlock = f"- **Author:** [[{(groups[book][0][1])}]] \n- **Reading Status:**  \n- **Date Finished:**  \n- **Why:**  \n- **Tags:**#book  \n- **Notes:**  \n"
    f.write(authorBlock)
    
    for n in range(len(groups[book])):    
        f.write(f"     - {(groups[book][n][2])} \n")
    
    f.close()


for book in range(len(groups)):
    createMd(book)