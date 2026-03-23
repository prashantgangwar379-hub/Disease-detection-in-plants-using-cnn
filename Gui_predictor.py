import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import os



train_dir = r"ENTER YOUR PATH HERE\dataset\color"
CLASS_NAMES = sorted(os.listdir(train_dir))

# disease knowledge user database
RECOMMENDATIONS = {
    "Apple___Black_rot": "Remove infected leaves and apply a copper-based fungicide. Avoid overhead watering.ensure proper water logging and the proper amount of watering in plants.",
    "Apple___Apple_scab": "Use resistant varieties and remove fallen leaves. Apply sulfur or captan fungicide.try removing the infected part and keep it seperate fromm the healthy part",
    "Potato___Early_blight": "Rotate crops yearly and apply a preventive fungicide like chlorothalonil.keep a close watch on the amount of pesticides being used in the soil and on the plant",
    "Tomato___Late_blight": "Remove infected plants immediately and use a fungicide containing mancozeb or copper.",
    "Tomato___Leaf_Mold": "Improve air circulation and avoid wetting leaves. Use fungicide sprays as needed.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Increase humidity and use neem oil or insecticidal soap.",
    "Orange___Haunglongbing_(Citrus_greening)": "No known cure. Remove infected trees and control psyllid insects.",
    "Pepper,_bell___Bacterial_spot": "Use disease-free seeds and apply copper sprays preventively.",
    "Grape___Black_rot": "Prune vines to improve airflow and apply fungicides at the start of the season.",
}


# ⚙️ Load model once

MODEL_PATH = r"ENTER YOUR PATH HERE\plant_disease_prediction_model.h5"
print(" Loading model kindly wait ")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model fetched sucessfully")



#  loading and helping call functions

def load_and_prepare_image(img_path, target_size=(224, 224)):
    img = tf.keras.utils.load_img(img_path, target_size=target_size)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


def predict_disease(img_path):
    img_array = load_and_prepare_image(img_path)
    predictions = model.predict(img_array)[0]
    top_indices = predictions.argsort()[-3:][::-1]
    top_classes = [(CLASS_NAMES[i], predictions[i] * 100) for i in top_indices]
    predicted_class, confidence = top_classes[0]
    recommendation = RECOMMENDATIONS.get(
        predicted_class,
        "General care: ensure good watering, remove infected leaves, and maintain airflow.remove the fallen leaves if they seemsnto be infected."
    )
    return predicted_class, confidence, top_classes, recommendation



#  Tkinter GUI

class LeafDiseaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Plant Leaf Disease Detector")
        self.root.geometry("700x600")
        self.root.configure(bg="#FBF4F4")

        self.image_label = Label(root, bg="#1b1b1b")
        self.image_label.pack(pady=10)

        self.result_label = Label(root, text="", font=("Arial", 14), fg="white", bg="#1b1b1b")
        self.result_label.pack(pady=10)

        self.recommendation_label = Label(root, text="", wraplength=600, justify="left",
                                          font=("Arial", 11), fg="#a6ff96", bg="#1b1b1b")
        self.recommendation_label.pack(pady=10)

        Button(root, text="Choose your image file", command=self.load_image,
               font=("Arial", 12, "bold"), bg="#080E09", fg="white", width=20).pack(pady=10)
        Button(root, text="❌ Exit", command=root.quit,
               font=("Arial", 12, "bold"), bg="#cc2323", fg="white", width=20).pack(pady=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if not file_path:
            return

        # Display image
        img = Image.open(file_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

        #prediction
        try:
            predicted_class, confidence, top_classes, recommendation = predict_disease(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Prediction cant n=be fetched: {e}")
            return

        # Format results
        result_text = f"Predicted: {predicted_class}\n Model accuracy: {confidence:.2f}%\n\nTop 3 Predicted matches:\n"
        for i, (cls, conf) in enumerate(top_classes, 1):
            result_text += f"  {i}. {cls} - {conf:.2f}%\n"

        self.result_label.config(text=result_text)
        self.recommendation_label.config(text=f" Recommendation:\n{recommendation}")
#  Run the app

if __name__ == "__main__":
    root = tk.Tk()
    app = LeafDiseaseApp(root)
    root.mainloop()
