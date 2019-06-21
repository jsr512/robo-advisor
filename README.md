# robo-advisor
Robo Advisor Project for NYU

## Set up and Installation
Fork the robo-advior repo from https://github.com/jsr512/robo-advisor then clone or download locally 

Create a local repository with the name robo-advisor then navigate to this using the command line
    ''
    cd ~/Desktop/robo-advisor
    ''
Create a file named requirements.txt and place the following contents inside
    ''
    requests
    python-dotenv
    ''
Create and activate a new virtual enviornment
    ''
    conda create -n stocks-env Python=3.7
    conda activate stocks-env
    ''
From within the virtual environment install packages outlines in requirements.txt
    ''
    pip install -r requirements.txt
    ''
Register for API key from Alpha Vantage service and place the specific API key in a file named .env

Add .env to the .gitignore file

eperately create a data directory with another .gitignore file excluding all files within using "*"

## Running the Program
Run the program from the command line
    ''
    python robo_advisor.py
    ''
Follow the prompts to enter a stock symbol and enjoy the investing recommendation and data!
