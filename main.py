import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
# create a video capture object; the argument can index of the device. Typically there is only one device connected so you can pass either 0 or -1
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
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
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()