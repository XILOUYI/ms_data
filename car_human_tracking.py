import cv2
#our image
#img_file = 'car1.jpg'
#video = cv2.VideoCapture('tesla.mp4')
video = cv2.VideoCapture('human1.mp4')
#our pre-trainsed car classifier and human classfifier
car_file = 'car_detector.xml'
human_file = 'human.xml'
#creat car and human classifier
car_tracker = cv2.CascadeClassifier(car_file)
human_tracker = cv2.CascadeClassifier(human_file)


while True:
    (read_successful, frame) = video.read()
    if read_successful:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(gray_frame)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0,255), 2)
    humans = human_tracker.detectMultiScale(gray_frame)
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0,0), 2)
    cv2.imshow('car_detector', frame)
    cv2.waitKey(1)
    if key == 81 or key == 113:
        break
video.release()
print('Code completed')
