import streamlit as st
import cv2
import numpy as np
from datetime import datetime
st.title("Real-Time Webcam Processing with OpenCV")
# --- Initialize webcam ---
frame_window = st.image([])
cap = cv2.VideoCapture(0)  # 0 is usually the default webcam
   # --- Filter controls ---
st.sidebar.header(" Filter Controls")
gray = st.sidebar.checkbox("Convert to Grayscale")
canny = st.sidebar.checkbox("Apply Canny Edge Detection")
canny_threshold1 = st.sidebar.slider("Canny Threshold1", 0, 255, 100)
canny_threshold2 = st.sidebar.slider("Canny Threshold2", 0, 255, 200)

snapshot_btn = st.sidebar.button("Take Snapshot")
# --- Process webcam ---
snapshot_taken = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to read from webcam.")
        break
    # Apply filters
    processed = frame
    if gray:
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    if canny:
        processed = cv2.Canny(processed, canny_threshold1, canny_threshold2)

    # Convert to RGB for Streamlit display
    if len(processed.shape) == 2:
        processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)
    else:
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
    frame_window.image(processed)
    # Snapshot
    if snapshot_btn and not snapshot_taken:
        filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, cv2.cvtColor(processed, cv2.COLOR_RGB2BGR))
        st.sidebar.success(f"Snapshot saved: {filename}")
        snapshot_taken = True
        break  # Stop after snapshot to avoid multiple captures
cap.release()
