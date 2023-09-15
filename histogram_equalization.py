import cv2
import numpy as np
import pydicom
from tkinter import filedialog
from tkinter import Tk

def dicom_enhancement():
    # Open a file dialog to select the image
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print("File path:", file_path)
    
    # Load the DICOM image using pydicom
    ds = pydicom.dcmread(file_path)
    img = ds.pixel_array
    
    # Convert the image to a format that can be displayed by OpenCV
    img = img.astype(np.float32)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    img = img.astype(np.uint8)
    
    # Enhance the image using histogram equalization
    enhanced_img = cv2.equalizeHist(img)
    
    # Display the original and enhanced images
    cv2.imshow('Original Image', img)
    cv2.imshow('Enhanced Image', enhanced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    dicom_enhancement()
