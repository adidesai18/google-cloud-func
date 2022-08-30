# Google Cloud Function Course

## Starting Project

To start project new project in google cloud,we can go to [Firebase Console](https://console.firebase.google.com) or create it from [Google Cloud Platform Console](https://console.cloud.google.com)

## Creating Virtual Environment

First we have to install 'python3-venv' with following command:

1. Below command install python3 on system with pip3 latest version

   '''brew install python3'''

2. Below command install virtual environment on system

   '''sudo pip install virtualenv'''
   or
   '''sudo -H pip install virtualenv'''

3. Below command creates virtual environment on system

   '''python3 -m venv .venv'''

4. Below command to activate virtual environment on system

   '''source .venv/bin/activate'''

For understanding above procedure Follow this [Youtube Link](https://youtu.be/kz4gbWNO1cw)

## Creating Requirments Txt File Environment

1. create requirments.txt file in root foder
   This file only contains the pacakges which are in current create virtual environment
2. Below command To add new pacakges to our virtual environments

   '''pip install -r requirments.txt'''

   To upgrade pip inside virtual environment

   '''pip install --upgrade pip'''

## To save changes of README.md on github

1. ''' git add '''

2. ''' git commit -m "Modified README.md" '''

3. ''' git push or git push --set-upstream origin develop '''
