# Nmap-XML-to-Markdown

This repo helps generate markdown for reporting nmap scans open ports and services. 
Just pass in your nmap xml files and it will generate a use able markdown


Step 1: Scan a target using nmap.

```
nmap -sC -sV -oA nmap 172.27.0.222
``` 

Step 2: Clone the repo and use the script to convert the xml file.

```
pip install -r requirements.txt
python3 xmlTomd.py nmap.xml
```

> It also works with -iL and list of hosts passed to nmap 
