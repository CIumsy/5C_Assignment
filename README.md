# Brain MRI Metastasis Segmentation

This repository demonstrates the application of computer vision techniques for **brain MRI metastasis segmentation** using deep learning models. We implement and compare two advanced architectures—**Nested U-Net (U-Net++)** and **Attention U-Net**—for accurately segmenting metastases in MRI scans.

The repository includes:
- Data preprocessing (CLAHE, normalization, and augmentation)
- Model implementation for U-Net++ and Attention U-Net
- Model training and evaluation
- Web application for real-time metastasis segmentation
- A FASTAPI backend to serve the model
- A Streamlit UI to visualize the segmentation results.

## Table of Contents
- [Objective](#objective)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Model Training](#model-training)
  - [Serving the Model with FASTAPI](#serving-the-model-with-fastapi)
  - [Streamlit Frontend](#streamlit-frontend)
- [Results](#results)
- [Challenges](#challenges)
- [Future Work](#future-work)

---

## Objective

The goal of this project is to segment brain metastasis from MRI scans. We implemented **Nested U-Net (U-Net++)** and **Attention U-Net** architectures and compared their performance in terms of the **DICE score**, a metric used to evaluate the accuracy of the segmentation. Additionally, we developed a web application that allows users to upload MRI scans and view the segmentation results.

---

## Dataset

- **Link**: [Download Dataset](https://dicom5c.blob.core.windows.net/public/Data.zip)
- **Structure**:
  - The dataset consists of **brain MRI images** and their corresponding **metastasis segmentation masks**. Only images with matching masks were used for training.
  
### Data Preprocessing

The dataset undergoes:
- **CLAHE (Contrast Limited Adaptive Histogram Equalization)** for enhanced metastasis visibility.
- **Normalization** of pixel values.
- **Data Augmentation** (flips, rotations, elastic transformations) for improved generalization.

The dataset is split into **80% training** and **20% testing**.

---

## Requirements

To install the required packages, run:

```bash
pip install -r requirements.txt
```

Required libraries include:
- Python 3.8+
- TensorFlow/PyTorch
- OpenCV
- Albumentations
- Segmentation Models PyTorch
- FastAPI
- Uvicorn
- Streamlit
- Requests

---

## Usage

### Model Training

1. **File**: `train_models.ipynb`
   
   This notebook contains the code for:
   - Loading and preprocessing the MRI dataset.
   - Training both **Nested U-Net** and **Attention U-Net** models.
   - Evaluating the models using the **DICE score**.

   **Note**: You need to adjust the file paths in the notebook to match your dataset location.

   **Steps**:
   - Download the dataset and place it in the appropriate folder.
   - Open the `train_models.ipynb` file.
   - Modify the dataset path and output model path as necessary.
   - Run the notebook to train and evaluate the models.

   After training, save the best-performing model to be used in the web application.

   ```python
   # Example of saving the best model
   torch.save(best_model.state_dict(), "path_to_save_model.pth")
   ```

### Serving the Model with FASTAPI

2. **File**: `app.py` (FASTAPI Backend)

   This file sets up a **FASTAPI** server to serve the trained metastasis segmentation model.

   **Steps**:
   - Before running, ensure you have saved the model file in the correct path and modify the model loading path in `app.py`:
     ```python
     model = torch.load('path_to_saved_model.pth')
     ```
   - Start the FastAPI server using:
     ```bash
     uvicorn app:app --reload
     ```
   - The server will be accessible at `http://127.0.0.1:8000`.

   - **Endpoints**:
     - `POST /predict`: Accepts an uploaded MRI image and returns the metastasis segmentation result.

### Streamlit Frontend

3. **File**: `stream_lit.py` (Streamlit UI)

   This file sets up a **Streamlit** interface where users can upload an MRI image and view the segmentation result generated by the model.

   **Steps**:
   - Make sure the FastAPI server is running.
   - Modify the model endpoint URL in `stream_lit.py` if necessary (ensure it matches your FastAPI server URL):
     ```python
     response = requests.post("http://127.0.0.1:8000/predict", files=files)
     ```
   - Run the Streamlit app using:
     ```bash
     streamlit run stream_lit.py
     ```

   The UI allows users to upload an image, which is then sent to the FastAPI server for prediction. The result is displayed in the Streamlit app.

---

## Results

### DICE Score Evaluation:

- **Nested U-Net (U-Net++)**: 
  - Achieved a DICE score of approximately **0.85** on the test set.

- **Attention U-Net**:
  - Achieved a DICE score of approximately **0.87** on the test set.

### Example UI:

- The Streamlit UI enables users to upload MRI images and view real-time metastasis segmentation results using the trained models.

---

## Challenges

The main challenges encountered during this project were:
1. **Small Lesions**: Metastases can be very small, making it hard to detect.
2. **Data Augmentation**: Extensive augmentation was necessary to account for variations in brain scans.
3. **Model Complexity**: Attention mechanisms and nested structures increase both the computation cost and training time.

---

## Future Work

To further improve the system, we can:
- Use **3D Convolutional Networks** (3D U-Net) for more accurate metastasis segmentation from volumetric MRI data.
- Apply **transfer learning** using models pre-trained on medical imaging tasks.
- Implement **post-processing** techniques like **CRF (Conditional Random Fields)** to improve boundary accuracy.

---

## Notes

- Ensure that the **model path** is correctly specified in the FastAPI backend (`app.py`) and Streamlit frontend (`stream_lit.py`).
- The current model expects **grayscale MRI images** with specific preprocessing (CLAHE and normalization).

---
