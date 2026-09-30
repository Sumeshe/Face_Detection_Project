import cv2 as cv

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)
def read():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        frame = cv.flip(frame, 1)  
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30)
        )
        face_count = len(faces)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 2)
        
        if face_count > 0:
            cv.putText(
                frame,
                f"Faces detected: {face_count}",
                (10, 30),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255 , 0),
                2
            )
        else:
            cv.putText(
                frame,
                f"No Faces detected",
                (10, 30),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0 , 255),
                2
            )
        cv.imshow("Video Feed", frame)

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    read()




