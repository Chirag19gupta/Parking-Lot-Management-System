
# Parking Lot Management System

This repository contains two Python scripts that work together to manage a parking lot system and recognize vehicle license plates.

## Getting Started

### Prerequisites
- Python 3.x
- OpenCV (cv2)
- NumPy
- Pytesseract
- Tesseract-OCR

### Installation
1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required libraries using pip:
   ```
   pip install opencv-python numpy pytesseract
   ```
3. Install Tesseract-OCR from [this link](https://github.com/tesseract-ocr/tesseract).

### Running the Code
To run the code, execute the following commands in your terminal:
```
python liscence.py
python management.py
```

## Customization
You can customize the following aspects of the code:
- **License Plate Recognition Settings**: In `liscence.py`, you can adjust the image preprocessing settings and the Tesseract OCR configuration.
- **Parking Lot Configuration**: In `management.py`, you can modify the `fee_per_hour` variable in the `ParkingLot` class to change the parking fee.

## Contributing
Feel free to fork this repository and submit pull requests. You can also open an issue for bugs, suggestions, or new feature requests.
