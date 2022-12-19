import cv2
from keras.models import load_model
import numpy as np
import time
import random
model = load_model('keras_model.h5')

labels = open('labels.txt', 'r').read().split('\n')
labels = [entry[2:] for entry in labels]
labels.pop()

class RockPaperScissors:
    def __init__(self):
        pass

    def get_computer_choice(self):
        choices = ['Rock', 'Paper', 'Scissors']
        self.computer_choice = random.choice(choices)
        return self.computer_choice

    def get_prediction(self):
        # create a video capture object; the argument can be the index of the device. Typically there is only one device connected so you can pass either 0 or -1
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.start = time.time()
        while True: 
            # capture frame by frame
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            flipped_image = cv2.flip(normalized_image, 1)
            data[0] = flipped_image
            # verbose = 0 supresses printing out to the terminal
            self.prediction = model.predict(data, verbose = 0)
            # display image in a window, the arguments stand for 'frame': a string representing the name of the window in which image is to be displayed; frame: the image that is to be displayed
            cv2.imshow('frame', frame) 
                
            self.prediction = labels[np.argmax(self.prediction)]
            
            if time.time() > self.start + 5:
                break

            # Press q to close the window                 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                                
        print(f'You chose {self.prediction}.')
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return self.prediction

    def get_winner(self, computer_choice, user_choice):
        if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
            print('You lost')
            return 0
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print('You won!')
            return 1
        elif user_choice == 'Nothing':
            print('No guess')
        else:
            print('It is a tie!')



def play():
    game = RockPaperScissors()
    computer_wins = 0
    user_wins = 0
    while True:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        result = game.get_winner(computer_choice, user_choice)
        
        if result == 0:
            computer_wins += 1
        elif result == 1:
            user_wins += 1
        if computer_wins >= 3 or user_wins >= 3:
            break

play()



# def get_winner(computer_choice, user_choice):
#     match(computer_choice, user_choice):
#         case (('Rock', 'Scissors') | ('Paper', 'Rock') | ('Scissors', 'Paper')):
#             print('You lost')
#             return 0
#         case (('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock')):
#             print('You won!')
#             return 1
#         case (c, u) if c == u:
#             print('It is a tie!')
#         case (_, 'Nothing'):
#             print('No guess')
#         case x:
#             print(x)
#             print('Invalid')
