# kindleToRoam
Convert highlights stored on your Kindle to markdown files ready to be imported in Roam Research

In order to import them as single book in Roam, I've created a script to split the My Clipping file and aggregate by book name. The result is an .md file with the following formatting. 
- book title as filename
    - **Author:**
    - **Reading Status:**
    - **Date Finished:**
    - **Why:** 
    - **Tags:** #book
    - **Notes:**
        
In order to execute the script:
- clone or download the repo
- plug your kindle and navigate to the 'Documents' folder
- make a copy of 'My Clippings.txt' in the same folder of kindleToRoam.py
- open terminal and navigate to the folder 
- execute the command: 
```python
python3 kindleToRoam.py
```
- import your freshly formatted book entries in Roam Research
 
 
In the near future I would like to convert this script in a webpage and add other customisations in the output format. If interested in collaborating, [my dm's are open](https://twitter.com/jacopomar)😉
