import time
import threading
import queue
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx

# Import functions from our separated modules
from commands import (
    get_greeting,
    listen_in_background,
    recognize_audio,
    process_command,
    speak_text
)
from styles import CUSTOM_CSS

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Friday AI",
    page_icon="◉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================
# SESSION STATE & GLOBALS
# ============================================================
if "status" not in st.session_state:
    st.session_state.status = "sleeping"
if "last_query" not in st.session_state:
    st.session_state.last_query = ""
if "last_response" not in st.session_state:
    st.session_state.last_response = ""
if "trigger_listen" not in st.session_state:
    st.session_state.trigger_listen = False

# Queue to pass messages from background threads to the main Streamlit thread
if "message_queue" not in st.session_state:
    st.session_state.message_queue = queue.Queue()

# ============================================================
# UI RENDERING
# ============================================================
status_info = {
    "sleeping": {"label": "Sleeping", "description": "Friday is waiting"},
    "activated": {"label": "Activated", "description": "Friday is ready"},
    "listening": {"label": "Listening", "description": "I'm listening..."},
    "processing": {"label": "Processing", "description": "Understanding..."},
    "speaking": {"label": "Speaking", "description": "Friday is speaking..."}
}

current_status = st.session_state.status
info = status_info.get(current_status, status_info["sleeping"])

st.markdown('<div class="friday-title">FRIDAY</div>', unsafe_allow_html=True)
st.markdown('<div class="friday-subtitle">Your personal voice assistant</div>', unsafe_allow_html=True)

# Render Orb
st.markdown(f'<div class="orb-container"><div class="orb {current_status}"></div></div>', unsafe_allow_html=True)

# Render Status Text
st.markdown(f'<div class="status">{info["label"]}</div><div class="status-small">{info["description"]}</div>', unsafe_allow_html=True)

# Render Conversation
if st.session_state.last_query or st.session_state.last_response:
    query_text = st.session_state.last_query
    response_text = st.session_state.last_response
    st.markdown(f"""
        <div class="conversation">
            <div class="user-text"><b>You:</b> {query_text}</div>
            <div class="friday-text"><b>Friday:</b> {response_text}</div>
        </div>
        """, unsafe_allow_html=True)

# Render Controls
st.write("")
col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    if st.button("◉  ACTIVATE FRIDAY", use_container_width=True):
        st.session_state.status = "activated"
        greeting = get_greeting() + " I am Friday. How may I help you?"
        st.session_state.last_response = greeting
        st.session_state.last_query = ""
        st.session_state.message_queue.put({"type": "speak", "value": greeting})
        st.rerun()

st.write("")
col1, col2 = st.columns(2)
with col1:
    if st.button("🎙  LISTEN", use_container_width=True):
        st.session_state.status = "listening"
        st.session_state.trigger_listen = True
        st.rerun()

with col2:
    if st.button("⏻  SLEEP", use_container_width=True):
        st.session_state.status = "sleeping"
        st.session_state.last_response = "Going to sleep."
        st.session_state.message_queue.put({"type": "speak", "value": "Going to sleep."})
        st.rerun()

# ============================================================
# LOGIC EXECUTION LOOP
# ============================================================

# Handle listening trigger
if st.session_state.trigger_listen:
    st.session_state.trigger_listen = False # Reset immediately
    
    # Start listening thread
    listen_thread = threading.Thread(
        target=listen_in_background, 
        args=(st.session_state.message_queue,)
    )
    add_script_run_ctx(listen_thread) # Give thread Streamlit context
    listen_thread.start()

# Process messages from the queue
try:
    while not st.session_state.message_queue.empty():
        msg = st.session_state.message_queue.get_nowait()
        
        if msg["type"] == "status":
            st.session_state.status = msg["value"]
            st.rerun()
            
        elif msg["type"] == "audio_ready":
            st.session_state.status = "processing"
            audio = msg["value"]
            
            # Recognize
            query = recognize_audio(audio)
            st.session_state.last_query = query
            
            # Process Command
            response_text, action = process_command(query)
            st.session_state.last_response = response_text
            
            # Queue the speech response
            st.session_state.message_queue.put({"type": "speak_and_act", "value": response_text, "action": action})
            st.rerun()
            
        elif msg["type"] == "error":
            st.session_state.status = "activated"
            st.session_state.last_response = msg["value"]
            st.rerun()
            
        elif msg["type"] == "speak":
            speak_text(msg["value"])
            if st.session_state.status != "sleeping":
                st.session_state.status = "activated"
            
        elif msg["type"] == "speak_and_act":
             speak_text(msg["value"])
             action = msg.get("action")
             if action:
                 action()
             if st.session_state.status != "sleeping":
                st.session_state.status = "activated"
             st.rerun() 
             
except queue.Empty:
    pass

# Auto-rerun to poll the queue if we are actively listening or processing
if st.session_state.status in ["listening", "processing"]:
    time.sleep(0.5)
    st.rerun()

# to run this file _>python -m streamlit run main.py       