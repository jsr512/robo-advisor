# robo-advisor
Robo Advisor Project for NYU

## Set up and Installation

Fork the robo-advior repo from https://github.com/jsr512/robo-advisor then clone or download locally \n 

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