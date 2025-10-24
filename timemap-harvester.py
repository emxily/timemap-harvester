#Libraries
import os                                                                                                       #Library for interacting with the OS
import hashlib                                                                                                  #Library for hashing
import subprocess                                                                                               #Library for running external commands
import json                                                                                                     #Library for parsing JSON (to count mementos)
import time                                                                                                     #Library for sleeping between requests
import sys                                                                                                      #Library for accessing command-line arguments


#Run the command: py.exe timemap-harvester.py <link_list_file>


# #Start of main
if __name__ == "__main__":

#Variable Declarations
    URIList = set()                                                                                             #Set that contains all URIs that will be downloaded
    KeyMap = {}                                                                                                 #Dictionary that holds the legend to pair hash to URI
    OutDirectory = "TimeMaps"                                                                                   #Directory that holds the downloaded timemap files
    Format = "JSON"                                                                                             #Output format for MemGator (-f)
    Contact = input("Enter your email: ").strip()                                                               #Prompt user to enter contact email for MemGator (-c)
    Archives = "https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json"                   #URL to archives.json from ODU CS432 public repository
    Memgator = "memgator-windows-amd64.exe"                                                                     #Name of MemGator executable
    KeyMapFile = "KeyMap.txt"                                                                                   #File that stores hash -> URI mappings

#Generate required directory
    os.makedirs(OutDirectory, exist_ok=True)                                                                    #Generate the output directory if it does not exist

#Handle command-line argument
    if len(sys.argv) < 2:                                                                                       #Check if user provided a filename as a command-line argument
        print("Usage: py timemap-harvester.py <link_list_file>")                                                #If not, print correct usage format
        sys.exit(1)                                                                                             #Exit program since no file was provided

    LinkFile = sys.argv[1].strip().strip('\'"')                                                                 #Assign the first command-line argument to 'LinkFile' and remove any surrounding quotes or extra spaces

#Handle relative paths
    if not os.path.isabs(LinkFile):                                                                             #If the provided file path is not an absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))                                                 #Get the directory path where this Python script is located
        LinkFile = os.path.join(script_dir, LinkFile)                                                           #Combine the script directory with the given relative path to create a full path

    LinkFile = os.path.normpath(LinkFile)                                                                       #Normalize the file path to clean up any redundant slashes or dots (e.g., ./ or ../)

#Check if the file exists before continuing
    if not os.path.isfile(LinkFile):                                                                            #If the file path does not point to an existing file
        print(f"Error: file not found: {LinkFile}")                                                             #Print an error message showing the invalid file path
        sys.exit(1)                                                                                             #Exit the program since the file cannot be found or opened

#Grab the links from the input file
    with open(LinkFile, "r", encoding="utf-8") as GrabbedLinksFile:                                             #Open the file that contains the links
        for URI in GrabbedLinksFile:                                                                            #Loop through each line of the file
            URIList.add(URI.strip())                                                                            #Strip whitespace/newlines and add URi to the set
    print("Links Acquired!\n")                                                                                  #Print confirmation when done  
    print("Starting MemGator requests. . .\n")                                                                  #Print that the fetching process has started

#Read Keymap to reuse MD5 hashes if available 
    if os.path.exists(KeyMapFile):                                                                              #Check if KeyMap.txt already exists
        with open(KeyMapFile, "r", encoding="utf-8") as KeyFile:                                                #Open KeyMap.txt
            for line in KeyFile:                                                                                #Loop through each line of the keymap
                if "->" in line and not line.lower().startswith("hash to uri"):                                 #Skip header, only process valid lines
                    parts = line.strip().split("->")                                                            #Split on ->
                    if len(parts) == 2:                                                                         #If valid format
                        hashValue = parts[0].strip()                                                            #Get hash part
                        uri = parts[1].strip()                                                                  #Get URI part
                        KeyMap[uri] = hashValue                                                                 #Store URI:hash in dictionary
    else:
        with open(KeyMapFile, "w", encoding="utf-8") as NewKeyFile:                                             #If file doesn't exist, create with header
            NewKeyFile.write("Hash to URI\n")                                                                   #Write header line

#Open KeyMap.txt for appending any new entries
    KeyMapHandle = open(KeyMapFile, "a", encoding="utf-8")                                                      #Open file in append mode to add new hashes as needed

#Initialize counters and prepare filename, hash, and output path for each URI before fetching TimeMaps
    counter = 1                                                                                                 #Counter for printing progress
    total = len(URIList)                                                                                        #Total number of URIs
    zeroCount = 0                                                                                               #Count of URIs with 0 mementos
    zeroURIs = []                                                                                               #List of URIs with 0 mementos
    mementoCounts = {}                                                                                          #Dictionary to track how many links had N mementos

    for URI in URIList:                                                                                         #Loop through each URI in the set
        if URI in KeyMap:                                                                                       #If URI already in KeyMap
            hashedURI = KeyMap[URI]                                                                             #Use existing hash
        else:                                                                                                   #Otherwise create new hash
            hashedURI = hashlib.md5(URI.encode("utf-8")).hexdigest()                                            #Generate md5 hash for URI
            KeyMap[URI] = hashedURI                                                                             #Add mapping to dictionary
            KeyMapHandle.write(f"{hashedURI} -> {URI}\n")                                                       #Append new mapping to KeyMap.txt
            KeyMapHandle.flush()                                                                                #Flush buffer to save immediately
            print(f"Added new entry to KeyMap: {hashedURI} -> {URI}")                                           #Print confirmation message

        filename = f"{hashedURI}.json"                                                                          #Filename for saved timemap
        OutputPath = os.path.join(OutDirectory, filename)                                                       #Full file path inside output directory

#Build MemGator command
        command = [                                                                                             #MemGator command list with args from Memgator documentation
             Memgator,
            "-c", Contact,
            "-a", Archives,
            "-f", Format,
            URI
        ]

#Run MemGator process
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)                       #Run MemGator and capture output

        mCount = 0                                                                                              #Initialize memento count for this URI
        if process.returncode == 0 and process.stdout:                                                          #If MemGator succeeded and produced output
            with open(OutputPath, "wb") as OutputFile:                                                          #Open output file in binary write mode
                OutputFile.write(process.stdout)                                                                #Write TimeMap JSON bytes to file
            print(f"Saved TimeMap as {filename}")                                                               #Notify user of success

            try:                                                                                                #Try to parse returned JSON for counting mementos
                data = json.loads(process.stdout.decode("utf-8", errors="replace"))                             #Decode and parse JSON
                mList = data.get("mementos", {}).get("list", [])                                                #Access list of mementos (if present)
                mCount = len(mList)                                                                             #Count how many mementos found
            except Exception:                                                                                   #Handle JSON parsing issues
                print("Warning: Could not parse JSON to verify memento count.")                                 #Warn user about parse issue
        else:                                                                                                   #If MemGator failed or no output returned
            with open(OutputPath, "w", encoding="utf-8") as OutputFile:                                         #Open text file for placeholder/error
                if process.returncode == 0:                                                                     #MemGator returned no data
                    OutputFile.write("0 mementos (empty)\n")                                                    #Write placeholder for empty timemap
                else:                                                                                           #MemGator encountered an error
                    OutputFile.write(f"error (returncode={process.returncode})\n")                              #Record the return code for debugging

#Update summary counts
        if mCount == 0:                                                                                         #If there were no mementos
            zeroCount += 1                                                                                      #Increment zero counter
            zeroURIs.append(URI)                                                                                #Add this URI to zero-memento list
        mementoCounts[mCount] = mementoCounts.get(mCount, 0) + 1                                                #Track how many URIs had this memento count

        print("\tSleeping for 10 seconds...\n")                                                                 #Print that the program will pause 
        time.sleep(10)                                                                                          #Pause for 10 seconds
        counter += 1                                                                                            #Increment counter for progress tracking

#Close KeyMap file after processing all URIs
    KeyMapHandle.close()                                                                                        #Close KeyMap.txt file to save any remaining data

#Summary of Data
    print("\nAll TimeMaps retrieved or attempted!")                                                             #Print completion message
    print(f"Results saved as '.json' files in '{OutDirectory}' directory.\n")                                   #Show output directory
    print("Summary of processed URIs:")                                                                          #Header for processed URIs summary
    print(f"{total} URIs processed")                                                                     #Display total URIs processed
    print(f"{zeroCount} URIs with 0 TimeMaps")                                                                #Display total URIs with zero mementos

#Output counts for each memento count
    print("\nSummary of memento counts:")                                                                       #Header for memento summary
    for mCount in sorted(mementoCounts.keys()):                                                                 #Loop through counts in ascending order
        plural = "mementos" if mCount != 1 else "memento"                                                       #Use correct singular/plural
        print(f"{mementoCounts[mCount]} links had {mCount} {plural}")                                           #Print summary line for each count

#Output list of URIs with 0 mementos
    if zeroCount > 0:                                                                                           #If any URIs had no mementos
        print("\nURIs with 0 mementos:")                                                                        #Header for zero-memento list
        for u in zeroURIs:                                                                                      #Loop through list
            print("  -", u)                                                                                     #Print each URI on a new line