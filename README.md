# Google Cloud Function Course

## Starting Project

To start project new project in google cloud,we can go to [Firebase Console](https://console.firebase.google.com) or create it from [Google Cloud Platform Console](https://console.cloud.google.com)

## Creating Virtual Environment

First we have to install 'python3-venv' with following command:

1. Below command install python3 on system with pip3 latest version

   `brew install python3`

2. Below command install virtual environment on system

   `sudo pip install virtualenv`
   or
   `sudo -H pip install virtualenv`

3. Below command creates virtual environment on system

   `python3 -m venv .venv`

4. Below command to activate virtual environment on system

   `source .venv/bin/activate`

For understanding above procedure Follow this [Youtube Link](https://youtu.be/kz4gbWNO1cw)

## Creating Requirments Txt File Environment

1. create requirments.txt file in root foder
   This file only contains the pacakges which are in current create virtual environment
2. Below command To add new pacakges to our virtual environments

   `pip install -r requirments.txt`

   To upgrade pip inside virtual environment

   `pip install --upgrade pip`

## To save changes of README.md on github:

1. `git add .`

2. `git commit -m "Modified README.md"`

3. `git push or git push --set-upstream origin develop`

## First Cloud Function

You can refer this links to run Function Locally:

1. [Youtube Link 1](https://youtu.be/hnqeYOYDRYY)
2. [Youtube Link 2](https://youtu.be/N1sSUU3XGu4)

Commands to run function locally:-

`functions-framework --target hello_world --debug`

`functions-framework --target hello_world --debug --port=4040`

## Install Google Cloud SDK

To check your current Python version, run python3 -V or python -V. Supported versions are Python 3

[Google Download link](https://cloud.google.com/sdk/docs/install)

Note: To determine your machine hardware name, run uname -m from a command line.

Reference [Youtube Link](https://youtu.be/wc2kuTaHl8Y)

Run the script (from the root of the folder you extracted in the last step) using this command:

`./google-cloud-sdk/install.sh`

To initialize the gcloud CLI, run gcloud init:

`./google-cloud-sdk/bin/gcloud init` or `gcloud init`

## Some Google CLoud SDK Cheats

`gcloud project list`

`gcloud config set project Project Id`

Function Deploy Command(Run this command from folder containing main.py):

`gcloud functions deploy Function_Name --runtime python310 --trigger-http --allow-unauthenticated`

## Add envirnoment variables:-

1. Create .env file in root of folder
2. export SENDGRID_API_KEY=KEY
3. In terminal run command `source .env` to set api key
4. Run command `printenv | grep SENDGRID_API_KEY`

## Deploying cloud functions with environment variables and other dependencies

we have to create a `.env.yaml` file and `requirements.txt` in the same directory of our main.py and run the following command:

`gcloud functions deploy [Funtion_Name] --env-vars-file .env.yaml --runtime python310 --trigger-http --allow-unauthenticated`
