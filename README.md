# Computer Vision RPS

# MILESTONE 2
Currently two files have been uploaded onto github, keras_model.h5 and labels.txt. The first file contains machine learning outputs from Teachable Machine (TM) by Google, a web-based tool that facilitates creating machine learning tools in an accessible manner. Using TM, four different classes of data were created: Rock, Paper, Scissors and Nothing. Rock, Paper and Scissors all correspond to symbols of the old childhood gesture game. Class Nothing corresponds to no gesture. Each of the classes have been given a series of inputs, approx. 3,000 image samples per class. These inputs were then put through a 'training' process to allow future recognition of these inputs based on this data sample. The model certainly has its (severe) limitations in that it is largely based on one face and use of a right hand. Much larger data sample would be required to create a model with higher accuracy, however, data collected here is considered sufficient for the purpose of this project.

# MILESTONE 3
A series of steps were executed to set up virtual environment for the rock-paper-scissors game. 
(1) conda was installed first
(2) new environment was created with command: conda create -n cv-rps (where the name of the environment stands for computer vision rock paper scissors)
(3) the environment was then activated / entered using command: conda activate cv-rps. Note that the environment can be deactivated at any time with use of conda deactivate
(4) the following command was then used to install the necessary requirements: pip install opencv-python tensorflow ipykernel 

# MILESTONE 4
Milestone 4 focused on creating a manual version of the rock-paper-scissors game. The code includes four functions.
get_computer_choice(): uses python's random library to select a random item from the predefined list of choices of 'Rock', 'Paper' or 'Scissors' and assigns it to a variable computer_choice. The function returns computer_choice.
get_user_choice(): uses bult-in python function input() to ask user for their choice and assigns it to a variable user_choice. The function returns user_choice. Please note that at present this code is inherently flawed as it will not deal with invalid user input or issue of lower / upper / title case, for instance.
get_winner(): this function takes two parameters, computer_choice and user_choice and with simple if elif and else statements defines whether the user won, the computer won or whether it is a tie.
play(): play simply calls all three functions to run the game itself!


![Alt text](../../01.png)