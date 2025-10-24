# timemap-harvester

Automated retrieval and analysis of web archive TimeMaps using MemGator, JSON parsing, and MD5 hashing for URI management.

<br />

# Project Overview

long detailed explanation

## Original Assignment Requirements

* 
* 
* 


## Added Improvments

* 
* 
* 


<br />

# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Windows/Linux/MacOS system with Python installed
* You have installed the required libraries with: 

        code line


## Installing

* To install this program, clone or download this repository:

        git clone
* Then, navigate into the project directory:

        cd


## Executing program

* To run the program from the terminal:

        py.exe 



### <u>Example Output</u>
```py.exe timemap-harvester.py testlinks.txt```
```
Enter your email: [REDACTED]

Links Acquired!

Starting MemGator requests. . .

Added new entry to KeyMap: 09a457c326e21a1e8c4346241d8a5175 -> https://github.blog/author/davelosert/
Saved TimeMap as 09a457c326e21a1e8c4346241d8a5175.json
        Sleeping for 10 seconds...

Added new entry to KeyMap: 970831fb58b9cd98ffc38901a8e7dd62 -> https://github.blog/open-source/social-impact/
Saved TimeMap as 970831fb58b9cd98ffc38901a8e7dd62.json
        Sleeping for 10 seconds...

Added new entry to KeyMap: 1ccf5df09b90c822a0358f1c183073db -> https://github.blog/news-insights/research/the-state-of-open-source-and-ai/
Saved TimeMap as 1ccf5df09b90c822a0358f1c183073db.json
        Sleeping for 10 seconds...


All TimeMaps retrieved or attempted!
Results saved as '.json' files in 'TimeMaps' directory.

Summary of processed URIs
Total URIs processed: 3
Total with 0 TimeMaps: 0

Summary of memento counts:
1 links had 18 mementos
1 links had 88 mementos
1 links had 182 mementos
```


<br />


# Authors

**Author:** Emily Nowak

*Based on ...**Homework 3 - Web Archiving, part 1** by **Prof. Nasreen Arif** for CS:432 Web Science, at Old Dominion University*


<br />


# Future Updates

* This program is currently written as a single main script; I plan to refactor it into custom functions for better readability, reusability, and testing in a future version.

* More in-depth summaries including which links had 1 memento, which links had 2 mementos, and so on.


<br />


# Version History

* 0.1
    * Initial Release

*This program was tested and developed on Windows 10+ using Python 3.13.9*


<br />


# Acknowledgments

### Original Assignment
[HW3 Part 1 - Web Archiving - Question 1 Original Instructions](https://github.com/emxily/html-uri-crawler/blob/c5d2bd820bc3f4799209856755acb4494c6cdba4/original-assignment-intructions.md)

### References
* Markdown Syntax: <https://www.markdownguide.org/basic-syntax/#headings>
* HTML Syntax: <https://www.w3schools.com/tags>
* Creating a clickable download link: <https://stackoverflow.com/questions/64411967/how-do-i-create-a-download-link-in-github-markdown>
* Python Dictionary Documentation: <https://www.w3schools.com/python/python_dictionaries.asp>
* Python Hashlib Documentation: <https://docs.python.org/3/library/hashlib.html> 
* Python Subprocess Management Documentation: <https://docs.python.org/3/library/subprocess.html>
* MemGator Documentation <https://github.com/oduwsdl/MemGator/blob/master/README.md>
* Python JSON Library Documentation <https://docs.python.org/3/library/json.html>
