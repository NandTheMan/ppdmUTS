import streamlit as st
from ipynb.fs.full.nuMNB import testLy

st.set_page_config(page_title="Song Emotions Detection", layout="centered")


st.markdown("<h1 style='text-align: center; color: #FFFF00; white-space: nowrap;'> 🎵Song Emotions Detection App🎵 </h1>", unsafe_allow_html=True)

with st.container():
    st.markdown(" <h2 style='color: #FAD02C;'>  Masukkan lirik lagu di bawah ini: </h2>", unsafe_allow_html=True)
    temp = st.text_area("Lirik Lagu", placeholder="Contoh: Ku ingin kau tahu betapa aku merindukanmu...", height=150)

    if st.button("🔍 Detect Emosi Lagu"):
        if temp.strip() == "":
            st.warning("⚠️ Mohon masukkan lirik terlebih dahulu.")
        else:

            result, probablities, sorted = testLy(temp)
            if result == "bahagia":
                emoji = "😊"
            elif result == "sedih":
                emoji = "😢"
            elif result == "marah":
                emoji = "😠"
            elif result == "takut":
                emoji = "😨"
            
            st.success(f"🎧 Lagu kamu terdeteksi memiliki emosi: **{result}** {emoji}")
            st.success("Prediction From Most Confident to Least:")
            
            for i in range(len(sorted)):
                st.success(f"{i+1}.{sorted[3-i]}: {probablities[sorted[3-i]]}")

st.markdown("---")
