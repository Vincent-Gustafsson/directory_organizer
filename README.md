# About Directory Organizer

This script is all about organizing files. My intent here is to make a organizer script that's easy to understand, yet fills your needs. It's really easy to edit to your needs!

Example:
```py
 # Folder name in code: Folder name in file explorer
    folders = {
	    "images": "vincents_images",
	    "audio": "my_music"
    }
    
    # File extension: Folder name
    actions = {
	    ".png": folders["images"],
	    ".jpg": folders["images"],
	    ".wav": folders["audio"],
	    ".mp3": folders["audio"]
    }
```
In this example I have two folders, one named ``"vincents_images"`` and one named ``"my_music"``. The idea here is that the key in the ``folders`` dictionary is the name that will be referenced in the ``actions`` dictionary and in the rest of the code. The value in the dictionary is the name you want your folder to have on your system (your actual folder name).


# How to install

 - Download the python file from the github repository.
 - use git - ``git clone https://www.github.com/vincent-gustafsson/direcotry_organizer``

# How to run

**Run the python script**

 1. Open the terminal.
 2. Make sure you are in the correct directory.
 3. Type ``python organizer.py´´
