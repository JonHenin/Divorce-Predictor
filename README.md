## DIVORCE PREDICTOR

## Project Description
In this project I built a survey that predicts Divorce likelihood.  The survey sends the responses to a program in a docker container, running in Google Kubernetes.  The model is built using a SVM which is then transformed using a Calibrated Platt Scale such that the results are provided as a percentage of likelihood.  

## Data
The dataset is the Divorce Predictors dataset provided by UCI Machine Learning. 
http://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set

## How to Run
Download project and run take_survey.py
This will lead you through a survey of 54 questions upon which will give you the likelihood of divorce percentage.

## Methods Used
* SVC
* Platt Scaling
* User Survey

## Technologies
* Python
* Docker
* Kubernetes
* Flask

## Python Packages
* pandas
* numpy
* sklearn
* flask
* joblib
* json
* requests
* pathlib