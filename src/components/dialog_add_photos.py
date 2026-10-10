import streamlit as st  
from src.database.db import enroll_student_to_subject    
from src.database.config import supabase
import time


@st.dialog("Capture or upload photos")   
def add_photos_dialog(): 

  st.write('Add classroom photos to scan for attendence') 

  if 'photo_tab' not in st.session_state:  
    st.session_state.photo_tab = 'camera' 

  t1, t2 = st.columns(2) 

  with t1: 
    type_camera="primary" if st.session_state.photo_tab == 'camera' else 'tertiary' 
    if st.button('Camera', type=type_camera, width='stretch'): 
      st.session_state.photo_tab = 'camera' 

  with t2: 
    type_upload="primary" if st.session_state.photo_tab == 'upload' else 'tertiary' 
    if st.button('Upload photos', type=type_upload, width='stretch'): 
      st.session_state.photo_tab = 'upload' 


