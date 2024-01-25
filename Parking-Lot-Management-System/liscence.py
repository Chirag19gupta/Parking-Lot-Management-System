import cv2
import numpy as np
import pytesseract
import os

# Configure the path of Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function for trackbar control
def empty(a):
    pass

# Create settings window for trackbars
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 640, 240)
cv2.createTrackbar("Threshold1", "Settings", 23, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 20, 255, empty)

# Image preprocessing for edge detection
def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    thresh1 = cv2.getTrackbarPos("Threshold1", "Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgCanny = cv2.Canny(imgBlur, thresh1, thresh2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDil, kernel, iterations=1)
    return imgThres

# Function to recognize license plate using OCR
def recognize_license_plate(img):
    custom_config = r'--oem 3 --psm 7'
    text = pytesseract.image_to_string(img, config=custom_config)
    return text.strip()

# Function to save the image
def save_image(img, text):
    if not os.path.exists('Saved_Plates'):
        os.makedirs('Saved_Plates')
    filepath = f"Saved_Plates/{text.replace(' ', '_')}.png"
    cv2.imwrite(filepath, img)
    print(f"Image saved as {filepath}")

# Start video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture a frame.")
        break

    imgPre = preProcessing(img)
    contours, _ = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:  # Adjust this value as needed for license plate size
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped_plate = img[y:y+h, x:x+w]
            plate_text = recognize_license_plate(cropped_plate)
            cv2.putText(img, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the image
    cv2.imshow("Image", img)

    # Capture and save the image if 'Enter' key is pressed
    if cv2.waitKey(1) & 0xFF == 13:  # 13 is the Enter Key
        if cropped_plate is not None and plate_text:
            save_image(cropped_plate, plate_text)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
