# Watch Next
## Description
- This is a Python script that reads in a list of movie descriptions from a file, and returns the title of the most similar movie to a given description.

## Requirements
- Python 3.x
- spaCy

## Installation
- Clone this repository: git clone https://github.com/23BraSut/Task2
- Install the project's requirements: pip install -r requirements.txt

## Usage
- Navigate to the project directory.
- Run the script: python watch_next.py 
- "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
- The script will return the title of the most similar movie from the list.
- Includes ability to take user inputs just remove commented code by it.

## Docker
- Install Docker on your machine.
- Navigate to the project directory.
- Build the Docker image: docker build -t watch-next .
- Run the Docker container: docker run -it --rm watch-next "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
- The Docker container will run the script and return the title of the most similar movie from the list.
- You can pull from my docker repo using docker pull 23brasut/movie-similar
- run docker 23brasut/movie-similar
