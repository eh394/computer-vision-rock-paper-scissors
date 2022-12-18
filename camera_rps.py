import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')

labels = open('labels.txt', 'r').read().split('\n')
labels = [entry[2:] for entry in labels]
labels.pop()

start = time.time()


def get_prediction():
    # create a video capture object; the argument can index of the device. Typically there is only one device connected so you can pass either 0 or -1
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        if time.time() < start + 5:
            # capture frame by frame
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            flipped_image = cv2.flip(normalized_image, 1)
            data[0] = flipped_image
            prediction = model.predict(data)
            # display image in a window, the arguments stand for 'frame': a string representing the name of the window in which image is to be displayed; frame: the image that is to be displayed
            cv2.imshow('frame', frame)
            # # Press q to close the window

            # if time.time() > start + 5:      
            for i in range(len(labels)):
                if np.argmax(prediction) == i:
                    prediction = labels[i]
                    break
                           
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    print(f' You chose {prediction}.')
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction


get_prediction()




# import random


# def get_computer_choice():
#     choices = ['Rock', 'Paper', 'Scissors']
#     computer_choice = random.choice(choices)
#     return computer_choice

# def get_user_choice():
#     user_choice = input('Please enter Rock, Paper or Scissors: ')
#     return user_choice

# def get_winner(computer_choice, user_choice):
#     if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
#         print('You lost')
#     elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
#         print('You won!')
#     else:
#         print('It is a tie!')

# def play():
#     computer_choice = get_computer_choice()
#     user_choice = get_user_choice()
#     get_winner(computer_choice, user_choice)

# play()


# import random

# choices = ['rock', 'paper', 'scissors']

# def get_computer_choice():
#     computer_choice = random.choice(choices)
#     print(computer_choice)
#     return computer_choice

# def get_user_choice():
#     while True:
#         user_choice = input('Please enter rock, paper or scissors: ')
#         if user_choice.lower() not in choices:
#             print('Invalid entry. Please enter rock, paper, or scissors.')
#         else:
#             user_choice = user_choice.lower()
#             print(user_choice)
#             break    
#     return user_choice

# get_computer_choice()
# get_user_choice()
