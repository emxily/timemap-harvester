# timemap-harvester

Automated retrieval and analysis of web archive TimeMaps using MemGator, JSON parsing, and MD5 hashing for URI management.

<br />

# Project Overview

This program is an improved version of the CS432: Web Science – Homework 3, Part 1: Web Archiving implementation originally created by Prof. Nasreen Arif at Old Dominion University. It was enhanced to provide full automation, persistent URI management, and detailed summary reporting while maintaining the educational goals of the original assignment. It automates the process of downloading TimeMaps for a collection of web pages using the MemGator aggregation tool. The script begins by reading a list of URLs from a file and generating an output directory named TimeMaps to store the retrieved data. Each URI is associated with a unique MD5 hash, which serves as the filename for its corresponding TimeMap and is recorded in a file called KeyMap.txt to ensure consistent naming. For each URI, the program constructs and executes a MemGator command using Python’s subprocess library, specifying the user’s email for identification and the ODU-provided archives.json file to determine which public web archives to query. The output from MemGator, returned in JSON format, is saved to a local file and parsed using Python’s json library to count the number of available mementos for each resource. If a URI has no mementos or encounters an error, a placeholder file is created to record that result. Between each request, the program waits ten seconds to avoid overloading the archives. After all URIs have been processed, the script prints a detailed summary to the console, listing any pages with zero mementos and reporting how many links had each specific memento count.

## Original Assignment Requirements

* Use MemGator with -c flag
* Use MemGator with -a flag to use the given archive file.
* Use MD5 hash to generate unique file names.
* Sleep 10 to 20 seconds between each request.
* Report URIs with 0 mementos.

## Added Improvments

* Now takes the file containing the links as a command-line argument.
* KeyMap.txt logs the hash-key pairs.
* Automatic error handling.
* Detailed summary output

<br />

# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Windows/Linux/MacOS system with Python installed.

* This program requires the MemGator command-line tool to retrieve TimeMaps:
    * A Windows 64-bit MemGator executable (memgator-windows-amd64.exe) is already included in this repository and referenced directly by the script.

    * For other operating systems (macOS, Linux, etc.), download the appropriate release from the official [MemGator repository](https://github.com/oduwsdl/MemGator/releases).

    * After downloading, update the Memgator variable near the top of the script to point to your version’s filename.

* A .txt document containing the URIs you want the TimeMaps for with one URI per line. 

## Installing

* To install this program, clone or download this repository:

        git clone https://github.com/emxily/timemap-harvester.git

* Then, navigate into the project directory:

        cd timemap-harvester


## Executing program

* To run the program from the terminal:

        py.exe timemap-harvester.py <link_list_file>


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

Summary of processed URIs:
3 URIs processed
0 URIs with 0 TimeMaps

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

### MemGator
Sawood Alam and Michael L. Nelson. [MemGator - A Portable Concurrent Memento Aggregator: Cross-Platform CLI and Server Binaries in Go](https://github.com/oduwsdl/MemGator). In Proceedings of the 16th ACM/IEEE-CS Joint Conference on Digital Libraries, JCDL 2016, pp. 243-244, Newark, New Jersey, USA, June 2016.

### References
* Markdown Syntax: <https://www.markdownguide.org/basic-syntax/#headings>
* HTML Syntax: <https://www.w3schools.com/tags>
* Creating a clickable download link: <https://stackoverflow.com/questions/64411967/how-do-i-create-a-download-link-in-github-markdown>
* Python Dictionary Documentation: <https://www.w3schools.com/python/python_dictionaries.asp>
* Python Hashlib Documentation: <https://docs.python.org/3/library/hashlib.html> 
* Python Subprocess Management Documentation: <https://docs.python.org/3/library/subprocess.html>
* MemGator Documentation <https://github.com/oduwsdl/MemGator/blob/master/README.md>
* Python JSON Library Documentation <https://docs.python.org/3/library/json.html>
