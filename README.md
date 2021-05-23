# About The Project
https://www.youtube.com/watch?v=fo2fgHogxLk An explanation for the website.
![Trigger Warning](https://user-images.githubusercontent.com/82678405/119267960-c3e9ec80-bbbe-11eb-92d8-e562946df09d.png)

We found many trigger warning websites that would have users say what triggers were included on movies, so we though why not reach a different group of people by doing this on youtube instead.

# Here's why:
This project will help users on the internet who struggle with triggers found in online video sharing websites.  This will allow them to check if other users have also said there are triggers in the youtube video.  In order to improve funcitonality, in the future, we would like to create it into a chrome extension that allows them to add triggers while on the youtube website.

# Built With
Streamlit & Firebase

# Getting Started
You need to create a streamlit account.  Then you need to install streamlit with pip, and then you can access the documentations and add things into your code.  When you want to see your website, you run in the terminal (streamlit run {yourfile}.py) which will allow you to see your code on the website.  Using this, you can then create a website.  The other aspect is firebase, where we needed to create a database that can be accessed by the code in order to store information given by the user, so it can be accessed by other users as well.

# Prerequisites
This is an example of how to list things you need to use the software and how to install them.

Any python IDE with pip.

This installs all of the modules:
pip install streamlit
pip install streamlit_player
pip install firebase
pip install firebase-admin

This accesses all the modules:
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
from streamlit_player import st_player

# Roadmap
There are lots of fine fixes we need including:
- Making sure the users can only submit once (based on IP).
- Making the design better.
- Turning it into a chrome extension accesible on the youtube website itself.

# Contact
Krisztian Drimba - kriszemails@gmail.com
Beatrice Bradau - beatricebradau@gmail.com
Kathrine Mondshain - kathrine.mondshain@gmail.com

# Project Link: https://github.com/KriszD/Trigger-Warning

# Acknowledgements
Streamlit Documentation https://docs.streamlit.io/en/stable/getting_started.html
Firebase Documentation https://firebase.google.com/docs?authuser=0
