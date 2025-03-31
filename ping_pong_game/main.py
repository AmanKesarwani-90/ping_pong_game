import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Importing all images
try:
    imgBackground = cv2.imread("Resources/Background.png")
    imgGameOver = cv2.imread("Resources/gameOver.png")
    imgBall = cv2.imread("Resources/Ball.png", cv2.IMREAD_UNCHANGED)
    imgBat1 = cv2.imread("Resources/bat1.png", cv2.IMREAD_UNCHANGED)
    imgBat2 = cv2.imread("Resources/bat2.png", cv2.IMREAD_UNCHANGED)
    if imgBackground is None or imgGameOver is None or imgBall is None or imgBat1 is None or imgBat2 is None:
        raise FileNotFoundError("One or more image files were not found.")
except FileNotFoundError as e:
    print(e)
    exit(1)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
ballPos = [100, 100]
speedX = 15
speedY = 15
gameOver = False
score = [0, 0]
paused = False

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break

    img = cv2.flip(img, 1)
    imgRaw = img.copy()

    if not paused:
        # Find the hand and its landmarks
        hands, img = detector.findHands(img, flipType=False)  # with draw

        # Overlaying the background image
        img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

        # Check for hands
        if hands:
            for hand in hands:
                x, y, w, h = hand['bbox']
                h1, w1, _ = imgBat1.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)

                if hand['type'] == "Left":
                    img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                    if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] += 30
                        score[0] += 1

                if hand['type'] == "Right":
                    img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                    if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] -= 30
                        score[1] += 1

        # Game Over
        if ballPos[0] < 40 or ballPos[0] > 1200:
            gameOver = True

        if gameOver:
            img = imgGameOver
            total_score = score[0] + score[1]
            winner = "Player 1" if score[0] > score[1] else "Player 2"
            winner_text = f"Winner: {winner}"

            cv2.putText(img, str(total_score).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX, 2.5, (200, 0, 200), 5)
            cv2.putText(img, f"P1: {score[0]}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
            cv2.putText(img, f"P2: {score[1]}", (1050, 50), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
            cv2.putText(img, winner_text, (500, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)

        # If game not over move the ball
        else:
            # Increase ball speed every time both scores are multiples of 5
            if (score[0] % 5 == 0 and score[1] % 5 == 0 and score[0] > 0 and score[1] > 0):
                speedX += 3 if speedX > 0 else -3
                speedY += 3 if speedY > 0 else -3
                score[0] += 1  # To avoid continuous speed increase in the same loop
                score[1] += 1

            # Move the Ball
            if ballPos[1] >= 500 or ballPos[1] <= 10:
                speedY = -speedY

            ballPos[0] += speedX
            ballPos[1] += speedY

            # Draw the ball
            img = cvzone.overlayPNG(img, imgBall, ballPos)

            cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

        img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        ballPos = [100, 100]
        speedX = 15
        speedY = 15
        gameOver = False
        score = [0, 0]
        imgGameOver = cv2.imread("Resources/gameOver.png")
    elif key == ord('p'):
        paused = not paused

    # Check if the window is closed
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
