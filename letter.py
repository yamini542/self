import streamlit as st
import time

st.set_page_config(page_title="💌 A Letter Just for You", page_icon="💌")

st.markdown("<h2 style='text-align: center;'>💌 You've Got a Letter 💌</h2>", unsafe_allow_html=True)

# Session state to handle steps
if "step" not in st.session_state:
    st.session_state.step = 0

# Step 0: Show button to open letter
if st.session_state.step == 0:
    if st.button("📩 Open the Letter"):
        st.session_state.step = 1
        st.rerun()

# Step 1: Ask if we should say something
elif st.session_state.step == 1:
    st.markdown("### It's been a long time... should I say something?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("No"):
            st.session_state.step = 3
            st.rerun()

# Step 2: Banagaram message
elif st.session_state.step == 2:
    st.markdown("### Someone told me Banagaram is too expensive... 😢")
    time.sleep(2)
    st.markdown("### I told them: *“My Banagaram is always with me.”* 😌💛")
    time.sleep(4)
    st.session_state.step = 4
    st.rerun()

# Step 3: Alternate pickup line
elif st.session_state.step == 3:
    st.markdown("### Okay... but I’m gonna say it anyway.")
    time.sleep(2)
    st.markdown("### If kisses were stars, I’d give you the sky 🌌")
    time.sleep(4)
    st.session_state.step = 5
    st.rerun()

# Step 4: Thank you and final prompt
elif st.session_state.step == 4:
    st.markdown("---")
    st.markdown("### Thank you for your service 💂‍♂️")
    time.sleep(1)
    st.markdown("### This person is going to charge you some **interest** now... 💸")
    st.markdown("### Are you ready to give that?")
    if st.button("Yes I am 😘"):
        st.success("💖 Payment accepted: 1 hug, 2 kisses, unlimited cuddles.")
