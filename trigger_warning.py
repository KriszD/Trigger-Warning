import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
import numpy as np
import pandas as pd
from pyyoutube import Api
from streamlit_player import st_player
from typing import Optional
from pydantic import BaseModel

st.title('Trigger Warning Database')

if not firebase_admin._apps:
    cred = credentials.Certificate('triggers-314603-396887c5358b.json')
    default_app = firebase_admin.initialize_app(cred)

ansab = anshom = ansinc = ansvio = ansrac = anssel = ansmis = anseat = ansins = ansbod = ansnud = ansmed = ansmil = anssub = ansfla = str(0)
yesab = yeshom = yesinc = yesvio = yesrac = yessel = yesmis = yeseat = yesins = yesbod = yesnud = yesmed = yesmil = yessub = yesfla = str(0)
noab = nohom = noinc = novio = norac = nosel = nomis = noeat = noins = nobod = nonud = nomed = nomil = nosub = nofla = str(0)
key = 0

# yestest = 0
# notest = 0

link = st.text_input('Enter link of the video to review:')
print(link)
id = link.replace("https://www.youtube.com/watch?v=", "")
print('id', id)


if len(link) != 0:
    db = firestore.client()
    try:
        trigger = db.collection(u'triggers').document(id).get().to_dict()
        nohom = trigger['nohom'] #copy this for all of them
        yeshom = trigger['yeshom']
        noab = trigger['noab']
        yesab = trigger['yesab']
        novio = trigger['novio']
        yesvio = trigger['yesvio']
        noinc = trigger['noinc']
        yesinc = trigger['yesinc']
        nosel = trigger['nosel']
        yessel = trigger['yessel']
        nomis = trigger['nomis']
        yesmis = trigger['yesmis']
        noeat = trigger['noeat']
        yeseat = trigger['yeseat']
        noins = trigger['noins']
        yesins = trigger['yesins']
        nobod = trigger['nobod']
        yesbod = trigger['yesbod']
        nonud = trigger['nonud']
        yesnud = trigger['yesnud']
        nomed = trigger['nomed']
        yesmed = trigger['yesmed']
        nomil = trigger['nomil']
        yesmil = trigger['yesmil']
        nosub = trigger['nosub']
        yessub = trigger['yessub']
        nofla = trigger['nofla']
        yesfla = trigger['yesfla']
    except:
        print('firsttimevid')
    if link[0:32] == "https://www.youtube.com/watch?v=":
        st.sidebar.header('Triggers')

        # my_expander = st.sidebar.beta_expander("test", expanded=False)
        # with my_expander:
        #     anstest = st.selectbox('Select', ['no','yes'], key=1)
        #     if anstest == 'yes':
        #         yestest = int(yestest)
        #         yestest += 1
        #         print(yestest)
        #     elif anstest == 'no':
        #         notest = int(notest)
        #         notest += 1
        #         print(notest)

        st.sidebar.markdown('***')
        result = st.sidebar.button('Submit')
#        st.write("State of button:", result)
        my_expander = st.sidebar.beta_expander("Abuse", expanded=False)
        with my_expander:
            ansab = st.selectbox('Select', ["No" + " (" + str(noab) + ")","Yes" + " (" + str(yesab) + ")"], key = 1)
            print(yesab)
            if result:
                if ansab == ("Yes" + " (" + str(yesab) + ")"):
                    yesab = int(yesab)
                    yesab += 1
                    print(yesab)
                elif ansab == ("No" + " (" + str(noab) + ")"):
                    noab = int(noab)
                    noab += 1
                    print(noab)

        my_expander = st.sidebar.beta_expander("Homophobia/Transphobia", expanded=False)
        with my_expander:
            anshom = st.selectbox('Select', ["No" + " (" + str(nohom) + ")","Yes" + " (" + str(yeshom) + ")"], key = 2)
            if result:
                if anshom == ("Yes" + " (" + str(yeshom) + ")"):
                    yeshom = int(yeshom)
                    yeshom += 1
                    print(yeshom)
                if anshom == ("No" + " (" + str(nohom) + ")"):
                    nohom = int(nohom) #add int conversions to everything, fix all if statements
                    nohom += 1
                    print(nohom)

        my_expander = st.sidebar.beta_expander("Violence (Knives/Guns/Blood/etc.", expanded=False)
        with my_expander:
            ansvio = st.selectbox('Select', ["No" + " (" + str(novio) + ")","Yes" + " (" + str(yesvio) + ")"], key = 3)
            if result:
                if ansvio == ("Yes" + " (" + str(yesvio) + ")"):
                    yesvio = int(yesvio)
                    yesvio += 1
                if ansvio == ("No" + " (" + str(novio) + ")"):
                    novio = int(novio)
                    novio += 1

        my_expander = st.sidebar.beta_expander("Incest/Mentions of Incest", expanded=False)
        with my_expander:
            ansinc = st.selectbox('Select', ["No" + " (" + str(noinc) + ")","Yes" + " (" + str(yesinc) + ")"], key = 4)
            if result:
                if ansinc == ("Yes" + " (" + str(yesinc) + ")"):
                    yesinc = int(yesinc)
                    yesinc += 1
                    print(yesinc)
                if ansinc == ("No" + " (" + str(noinc) + ")"):
                    noinc = int(noinc)
                    noinc += 1


        my_expander = st.sidebar.beta_expander("Racism/Mentions of Racism", expanded=False)
        with my_expander:
            ansrac = st.selectbox('Select', ["No" + " (" + str(norac) + ")","Yes" + " (" + str(yesrac) + ")"], key = 5)
            if result:
                if ansrac == ("Yes" + " (" + str(yesrac) + ")"):
                    yesrac = int(yesrac)
                    yesrac += 1
                if ansrac == ("No" + " (" + str(norac) + ")"):
                    norac = int(norac)
                    norac += 1

        my_expander = st.sidebar.beta_expander("Depictons/Mentions of Self-Harm/Suicide", expanded=False)
        with my_expander:
            anssel = st.selectbox('Select', ["No" + " (" + str(nosel) + ")","Yes" + " (" + str(yessel) + ")"], key = 6)
            if result:
                if anssel == ("Yes" + " (" + str(yesrac) + ")"):
                    yessel = int(yessel)
                    yessel += 1
                if anssel == ("No" + " (" + str(nosel) + ")"):
                    nosel = int(nosel)
                    nosel += 1

        my_expander = st.sidebar.beta_expander("Mentions of Miscarriage/Stillbirth", expanded=False)
        with my_expander:
            ansmis = st.selectbox('Select', ["No" + " (" + str(nosel) + ")","Yes" + " (" + str(yessel) + ")"], key = 7)
            if result:
                if ansmis == ("Yes" + " (" + str(yesmis) + ")"):
                    yesmis = int(yesmis)
                    yesmis += 1
                if ansmis == ("No" + " (" + str(nomis) + ")"):
                    nomis = int(nomis)
                    nomis += 1

        my_expander = st.sidebar.beta_expander("Depictions of Eating Disorders", expanded=False)
        with my_expander:
            anseat = st.selectbox('Select', ["No" + " (" + str(noeat) + ")","Yes" + " (" + str(yeseat) + ")"], key = 8)
            if result:
                if anseat == ("Yes" + " (" + str(yeseat) + ")"):
                    yeseat = int(yeseat)
                    yeseat += 1
                if anseat == ("No" + " (" + str(noeat) + ")"):
                    noeat = int(noeat)
                    noeat += 1

        my_expander = st.sidebar.beta_expander("Insects", expanded=False)
        with my_expander:
            ansins = st.selectbox('Select', ["No" + " (" + str(noins) + ")","Yes" + " (" + str(yesins) + ")"], key = 9)
            if result:
                if ansins == ("Yes" + " (" + str(yesins) + ")"):
                    yesins = int(yesins)
                    yesins += 1
                if ansins == ("No" + " (" + str(noins) + ")"):
                    noins = int(noins)
                    noins += 1

        my_expander = st.sidebar.beta_expander("Bodily Fluids (Vomit/Feces/Urine) (Excludes Blood)", expanded=False)
        with my_expander:
            ansbod = st.selectbox('Select', ["No" + " (" + str(nobod) + ")","Yes" + " (" + str(yesbod) + ")"], key = 10)
            if result:
                if ansbod == ("Yes" + " (" + str(yesbod) + ")"):
                    yesbod = int(yesbod)
                    yesbod += 1
                if ansbod == ("No" + " (" + str(nobod) + ")"):
                    nobod = int(nobod)
                    nobod += 1

        my_expander = st.sidebar.beta_expander("Nudity", expanded=False)
        with my_expander:
            ansnud = st.selectbox('Select', ["No" + " (" + str(nobod) + ")","Yes" + " (" + str(yesbod) + ")"], key = 11)
            if result:
                if ansnud == ("Yes" + " (" + str(yesnud) + ")"):
                    yesnud = int(yesnud)
                    yesnud += 1
                if ansnud == ("No" + " (" + str(nonud) + ")"):
                    nonud = int(nonud)
                    nonud += 1

        my_expander = st.sidebar.beta_expander("Depictions of Medical Issues", expanded=False)
        with my_expander:
            ansmed = st.selectbox('Select', ["No" + " (" + str(nomed) + ")","Yes" + " (" + str(yesmed) + ")"], key = 12)
            if result:
                if ansmed == ("Yes" + " (" + str(yesmed) + ")"):
                    yesmed = int(yesmed)
                    yesmed += 1
                if ansmed == ("No" + " (" + str(nomed) + ")"):
                    nomed = int(nomed)
                    nomed += 1

        my_expander = st.sidebar.beta_expander("Depictions of Military Combat", expanded=False)
        with my_expander:
            ansmil = st.selectbox('Select', ["No" + " (" + str(nomil) + ")","Yes" + " (" + str(yesmil) + ")"], key = 13)
            if result:
                if ansmil == ("Yes" + " (" + str(yesmil) + ")"):
                    yesmil = int(yesmil)
                    yesmil += 1
                if ansmil == ("No" + " (" + str(nomil) + ")"):
                    nomil = int(nomil)
                    nomil += 1

        my_expander = st.sidebar.beta_expander("Depictions of Substance Misuse", expanded=False)
        with my_expander:
            anssub = st.selectbox('Select', ["No" + " (" + str(nosub) + ")","Yes" + " (" + str(yessub) + ")"], key = 14)
            if result:
                if anssub == ("Yes" + " (" + str(yessub) + ")"):
                    yessub = int(yessub)
                    yessub += 1
                if anssub == ("No" + " (" + str(nosub) + ")"):
                    nosub = int(nosub)
                    nosub += 1

        my_expander = st.sidebar.beta_expander("Flashing Lights/Eyestrain", expanded=False)
        with my_expander:
            ansfla = st.selectbox('Select', ["No" + " (" + str(nofla) + ")","Yes" + " (" + str(yesfla) + ")"], key = 15)
            if result:
                if ansfla == ("Yes" + " (" + str(yesfla) + ")"):
                    yesfla = int(yesfla)
                    yesfla += 1
                if ansfla == ("No" + " (" + str(nofla) + ")"):
                    nofla = int(nofla)
                    nofla += 1
        users_ref = db.collection(u'triggers').document(id)
        doc_ref = db.collection(u'triggers').document(id)
        doc_ref.set({
            u'yeshom': yeshom,
            u'nohom': nohom, #add yes/no for all triggers
            u'yesab': yesab,
            u'noab': noab,
            u'yesvio': yesvio,
            u'novio': novio,
            u'yesinc': yesinc,
            u'noinc': noinc,
            u'yessel': yessel,
            u'nosel': nosel,
            u'yesrac': yesrac,
            u'norac': norac,
            u'yesmis': yesmis,
            u'nomis': nomis,
            u'yeseat': yeseat,
            u'noeat': noeat,
            u'yesins': yesins,
            u'noins': noins,
            u'yesbod': yesbod,
            u'nobod': nobod,
            u'yesnud': yesnud,
            u'nonud': nonud,
            u'yesmed': yesmed,
            u'nomed': nomed,
            u'yesmil': yesmil,
            u'nomil': nomil,
            u'yessub': yessub,
            u'nosub': nosub,
            u'yesfla': yesfla,
            u'nofla': nofla,
        })

    else:
        st.text('Invalid Link')

if link[0:32] == "https://www.youtube.com/watch?v=":
    st_player(link)
