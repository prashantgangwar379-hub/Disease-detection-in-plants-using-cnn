# Disease-detection-in-plants-using-cnn


##  Description
This project detects diseases in plants using **Python**, **Convolutional Neural Networks (CNN)**, and supporting machine learning libraries. It provides a GUI interface to test the model with sample plant images and predict their health status.

---

##  Prerequisites
Keep all files in a single folder for convenience. You will need:

1. `gui_predictor.py` – The main GUI code file.  
2. Labeled plant images – Either download from Kaggle or use the provided Google Drive link.  
3. Pre-trained model (`.h5` format) – Download the already trained CNN model from Google Drive.  
4. Test images – At least 3 sample images for testing the GUI.

---

##  Setup & Usage

1. Create a new folder and place all required files inside it.  
2. Open `gui_predictor.py` and **edit the dataset path** to point to the "colour" folder of your downloaded dataset on your local machine.  
3. Edit the **path of the pre-trained model** in `gui_predictor.py`.  
4. Run `gui_predictor.py`. A GUI will appear.  
5. In the GUI, select a test image and run the prediction.  
6. The model will predict the disease or health status of the plant.

---

##  Folder Structure (Recommended)
Plant-Disease-Detection/
│
├── gui_predictor.py
├── trained_model.h5
├── dataset/
│ └── colour/
│ ├── class_1/
│ ├── class_2/
│ └── ...
└── test_images/
├── test1.jpg
├── test2.jpg
└── test3.jpg

---

##  Downloads
- **Pre-trained model:** [https://drive.google.com/file/d/1NbDXYKmyYQT1BRLER9ZcFQfQiJBx0QwU/view?usp=drive_link]  
- **Training dataset:** [https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset]  

---

##  Requirements
Make sure these Python libraries are installed:
- TensorFlow / Keras
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter (for GUI)

Install via pip if missing:
```bash
pip install tensorflow opencv-python numpy pillow