# Best Sellers Rank
A script which takes the best sllers rank of a book off of Amazon and pushes it to a google spreadsheet.

## Overview
The intial setup is somewhat confusing and can take up to a half an hour to complete. I have tried to make the setup as simple as possible, including adding specifid directions here. For any questions regarding how the script works, please contact me at michaelpineiro.code@gmail.com

## Dependencies
There are a few different things that we need to install before this script will work. The instructions below give a detail step-by-step explanation of how to install all the neccessary dependencies. All dependencies are open-source.

### Python
Ensure that python 3.6 or greater is installed. This can be done by opening the terminal or command prompt and typing:
```
python3 --version
```
If python 3.6 or greater is not installed, it can be installed [here:](https://www.python.org/downloads/)

During the installation process, make sure to check the box to "add python to PATH."

### This!
You can download this entire project by clicking "download" in the top right corner of the page, and selecting ZIP. Decompress the zip file.

### Other Libraries
All other neccessary bits and pieces of code can be installed with the "requirements.txt" file. Open the terminal/command prompt and move to the directory of the project, then copy:
```
pip3 install -r requirements.txt
```

## Setup Google Spreadsheets for API Access
In order to give the script permission to access a google sheet, a things must be set up first. First, head [here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjEy_Dx76TyAhVJop4KHVxZAYwQFnoECAUQAw&url=https%3A%2F%2Fconsole.developers.google.com%2F&usg=AOvVaw39ieEDI7pzBj4NtuzqS57M) to setup a project. Click "new project" and give it a name.

Then, on the left-hand side, click "credentials." At the top click "create credentials" and create a "service account." Setup the name and hit continue. In the next section, roles, go to "basic" and select owner. This will ensure that there are no unnessesary complications between google and the script.

From there, search "service accounts" at the top and go to the link. This will list all service accounts. Click on the account you just created. At the top, there is a tab that says "keys." Add a key, create a new key, and download as a json. Add the downloaded file to the folder of this project.

