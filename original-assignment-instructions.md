# Homework 3 - Web Archiving, part 1

### Q1. Get TimeMaps for Each URI.

Obtain the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs you collected in HW1 using the [MemGator Memento Aggregator](https://github.com/oduwsdl/MemGator).  

*Do **not** use memgator.cs.odu.edu this assignment. You must download and install a local version of MemGator.*

There are two options for running MemGator locally:
* Install a stand-alone version of MemGator on your own machine, see <https://github.com/oduwsdl/MemGator/releases>
  * This was described in [EC-memgator](https://github.com/odu-cs432-websci/public-fall25/blob/main/getting-started/EC-memgator.md)
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and run MemGator as a Docker Container, see notes at <https://github.com/oduwsdl/MemGator/blob/master/README.md>

Here's an example:

`./memgator-darwin-amd64 -c "ODU CS432/532 YOUR_EMAIL_ADDRESS" -a https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json -F 2 -f JSON https://www.cs.odu.edu/~mweigle/ > mweigle-tm.json`

Notes:
* As described in [EC-memgator](https://github.com/odu-cs432-websci/public-fall25/blob/main/getting-started/EC-memgator.md), you **must** include the `-c` and `-a` options to specify your contact information and to use the alternate `archives.json` file.
* When running this for all of your URIs, you might want to use the MD5 hash that you recorded earlier as part of the filename to help keep track of which TimeMaps you have.
* You will want to add a sleep (at least 10-20 seconds) between each call to MemGator because if you make too many requests too quickly, you will get "connection refused" errors (or worse, get blocked by an archive). 

**Important:** Obtaining TimeMaps requires contacting several different web archives for each URI-R.  *This process will take time.*

Look at the MemGator options and figure out how to process the output before running the entire process. 

Note that if there are no mementos for a URI-R, MemGator will return nothing. *Don't be surprised if many of your URI-Rs return 0 mementos.*  Remember the ["How Much of the Web is Archived" slides](https://docs.google.com/presentation/d/132sObERXgzGbxVETIc8QblUyuXB6X7lDbrbhCKmAKzU/edit#slide=id.g80c031ceb5_0_91) -- there are lots of things on the web that are not archived.  If you want to do a sanity check on a few, you can manually use the Wayback Machine and see what you get from the Internet Archive.  (Remember though that MemGator is going to query several web archives, not only the Internet Archive.)

If you uncover TimeMaps that are very large (e.g., for popular sites like <https://www.cnn.com/>) and swamp your filesystem, you have two options:
* Manually remove those URI-Rs from your dataset (but note this in your report), or
* Compress each TimeMap file individually (using pipe to `gzip` in the same command when downloading or after the download is completed). These compressed files can be used for further analysis by decompressing on the fly using commands like `zcat` or `zless` (or using gzip libraries in Python).
. . .

# Full Original Assignment
**Title:** Homework 3 Part 1 - Web Archiving

**Author:** Professor Nasreen Arif

[Public Assignment Instructions](https://github.com/odu-cs432-websci/public-fall25/blob/3164683945415a53dbce28ff19d93d78a069578d/HW3-archive.md)

**This assignment was originally from CS432 Web Science, at Old Dominion University**