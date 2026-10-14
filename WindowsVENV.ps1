# Sets the working directory to the path the script file is in
Set-Location -Path $PSScriptRoot

# Create the python virtual enviornment file
python -m venv venv

# Activate the virtual enviornment
.\venv\Scripts\Activate.ps1

#Install all the requirements
pip install -r .\requirements.txt