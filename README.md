
# Bicep Curl Counter

This project is a real-time bicep curl counter using computer vision techniques. It uses OpenCV and Mediapipe libraries to detect and track the movement of the user's arm during bicep curls, providing feedback on the number of curls performed.

## Features

**Real-time Pose Detection**: Utilizes the Mediapipe library to detect and track the user's arm movement in real-time.

**Angle Calculation** : Calculates the angle between the wrist, elbow, and shoulder to determine the position of the arm during bicep curls.

**Counting Bicep Curls** : Counts the number of completed bicep curls based on the angle of the arm movement. 

**Visual Feedback** : Displays a graphical representation of the bicep curl count and the percentage of completion on the screen.


## Usage Setup:

* Clone the repository:

  ```git clone https://github.com/your-username/bicep-curl-counter.git```

* Install the required dependencies:

    ```pip install opencv-python mediapipe cvzone``` 

* Run the Application:

Execute the **bicep_curl_counter.py** script: 
```python bicep_curl_counter.py``` 

* Perform Bicep Curls:

    * Stand in front of the webcam with your arm extended.
    * Perform bicep curls while keeping your elbow and wrist in    view of the camera.
    * The application will count the number of curls as you perform them.

* Exit the Application:

Press the 's' key to close the camera feed and exit the application.

## Demo

  I will add the Demo Video asap. 

## Contributing

* Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

* Fork the repository.
* Create a new branch (git checkout -b feature/improvement).
* Make your changes.
* Commit your changes (git commit -am 'Add new feature').
* Push to the branch (git push origin feature/improvement).
* Create a new Pull Request.

Contact
For any inquiries or feedback, please contact satyamkumar90009@gmail.com

Thanks!
