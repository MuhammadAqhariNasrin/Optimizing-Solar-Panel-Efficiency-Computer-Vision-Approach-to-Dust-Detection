


![Uploading _5ae8541a-c651-4b14-9256-39b8f2f82024.jpg…]()

# Optimizing Solar Panel Efficiency: Computer Vision Approach to Dust Detection

## Overview

This project aims to enhance the efficiency of solar panels using a computer vision approach for dust detection. The implemented solution involves training a model to detect and quantify dust on solar panels and presenting the results through a Streamlit web application.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [The Computer Vision Model](#the-computer-vision-model)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Dust Detection Model:** Trained a computer vision model to identify and quantify dust on solar panels.
  
- **Streamlit Web Application:** Created an [interactive web application](https://solarpanelimageclassifier.streamlit.app/) using Streamlit to visualize and analyze the dust detection results.


## Project Structure

- `data/`: [SolNet: A Convolutional Neural Network for Detecting Dust on Solar Panels](https://drive.google.com/drive/folders/12Q3MBI8SPw0vHsO_kkS5izkxw0F7tXx4) 
  
- `models/`: Includes the trained dust detection model.

- `src/`: Source code for the computer vision model and Streamlit web application.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies: OpenCV, TensorFlow, Streamlit
  
### Data Preprocessing

Image preprocessing is an essential step in preparing the data for model training. In this project, we used the following preprocessing steps:

- Image resizing to 256x256 pixels.
- Batch normalization.
- Batch size of 32.

## The Computer Vision Model

### Model

Utilizing the AlexNet architecture. The model architecture includes:

- AlexNet base model.
- Batch normalization layers.
- Flatten layer.
- Dense layers with dropout for predictions based on the two classes.

### Training

The model was trained for 20 epochs. The achieved accuracy on the validation set is approximately 95%.

### Pre-trained Model

The pre-trained model for chest solar panel image classification is available in the repository as solarpanelimageclassification.h5.

## Acknowledgments

The solar panel image dataset was compiled by:

[@SolNet2022](https://www.mdpi.com/1996-1073/16/1/155)  
**Authors:** Md Saif Hassan Onim, Zubayar Mahatab Md Sakif, Adil Ahnaf, Ahsan Kabir, Abul Kalam Azad, Amanullah Maung Than Oo, Rafina Afreen, Sumaita Tanjim Hridy, Mahtab Hossain, Taskeed Jabid, and Md Sawkat Ali  
**Title:** SolNet: A Convolutional Neural Network for Detecting Dust on Solar Panels  
**Journal:** Energies  
**Volume:** 16  
**Number:** 1  
**Year:** 2023  
**Article Number:** 155  
**DOI:** [10.3390/en16010155](https://doi.org/10.3390/en16010155)

## Contributing

Contributions, issues, and feature requests are welcome!

## Contact

LinkedIn : [Muhammad Aqhari Nasrin](https://www.linkedin.com/in/muhammad-aqhari-nasrin-bin-ramli/)

