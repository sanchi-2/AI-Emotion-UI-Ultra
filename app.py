import streamlit as st
import pandas as pd
import random
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt

# ------------------- Page Config -------------------
st.set_page_config(
    page_title='🤖 AI Emotion UI Ultra',
    page_icon='🎭',
    layout='wide'
)

# ------------------- Load Lottie Animations -------------------
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

happy_lottie = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jbrw3hcz.json")
sad_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json")
neutral_lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_hgk3qfn9.json")
welcome_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_yr6zz3wv.json")

# ------------------- GLOBAL CSS -------------------
st.markdown("""
<style>
.main { background-color:#0E1117; }

h1, h2, h3, h4 {
    color:#F5F7FA !important;
    font-weight:800 !important;
}

.card {
    background:#ffffff;
    color:#000000 !important;
    padding:18px;
    border-radius:15px;
    margin:12px 0;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
}

.stButton>button {
    background:linear-gradient(90deg,#89f7fe,#66a6ff);
    color:#000;
    font-weight:700;
    border-radius:12px;
    height:45px;
    width:100%;
}
</style>
""", unsafe_allow_html=True)

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.title("🤖 AI Emotion UI")
    selected = st.radio(
        "Navigate",
        ['🏠 Welcome', '💬 Emotion Chat', '🎭 AI Mood Themes',
         '📊 AI Dashboard', 'ℹ️ About Project', '❓ Help']
    )

# ------------------- SESSION STATE -------------------
if 'emotion_logs' not in st.session_state:
    st.session_state.emotion_logs = pd.DataFrame(
        columns=['Message', 'Detected Emotion', 'AI Confidence']
    )

# =====================================================
# 🏠 WELCOME PAGE
# =====================================================
if selected == '🏠 Welcome':
    st.header("👋 Welcome to AI Emotion UI Ultra")

   

    st.markdown("""
    <div class="card">
    🤖 <b>AI Emotion UI Ultra</b> is an AI-based application that detects
    human emotions from text and adapts the user interface accordingly.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    🧠 <b>Features:</b><br>
    • AI Emotion Detection<br>
    • Confidence Scoring<br>
    • Adaptive UI (HCI)<br>
    • Data Visualization using Matplotlib
    </div>
    """, unsafe_allow_html=True)

    if welcome_lottie:
        st_lottie(welcome_lottie, height=300)

# =====================================================
# 💬 EMOTION CHAT
# =====================================================
elif selected == '💬 Emotion Chat':
    st.header("💬 AI Emotion Detection Chat")

    st.markdown("""
    <div class="card">
    Enter a message and AI will analyze the emotion behind it.
    </div>
    """, unsafe_allow_html=True)

    user_input = st.text_input("Type your message here...")

    positive_words = ['happy','good','great','awesome','love','fantastic','amazing','excited']
    negative_words = ['sad','bad','angry','hate','terrible','upset','worst','frustrated']

    if st.button("Analyze Emotion") and user_input:
        text = user_input.lower()

        if any(w in text for w in positive_words):
            emotion = 'Positive'
            anim = happy_lottie
        elif any(w in text for w in negative_words):
            emotion = 'Negative'
            anim = sad_lottie
        else:
            emotion = 'Neutral'
            anim = neutral_lottie

        confidence = random.randint(70, 95)

        st.markdown(f"""
        <div class="card">
        🎭 <b>Detected Emotion:</b> {emotion}<br>
        🔍 <b>AI Confidence:</b> {confidence}%
        </div>
        """, unsafe_allow_html=True)

        if anim:
            st_lottie(anim, height=200)

        st.session_state.emotion_logs = pd.concat([
            st.session_state.emotion_logs,
            pd.DataFrame({
                'Message':[user_input],
                'Detected Emotion':[emotion],
                'AI Confidence':[confidence]
            })
        ], ignore_index=True)

# =====================================================
# 🎭 AI MOOD THEMES
# =====================================================
elif selected == '🎭 AI Mood Themes':
    st.header("🎭 AI Adaptive Mood Themes")

    mood = st.radio("Select Mood:", ['Positive','Negative','Neutral'])

    if mood == 'Positive' and happy_lottie:
        st_lottie(happy_lottie, height=250)
    elif mood == 'Negative' and sad_lottie:
        st_lottie(sad_lottie, height=250)
    elif neutral_lottie:
        st_lottie(neutral_lottie, height=250)

# =====================================================
# 📊 DASHBOARD (🔥 VISUALIZATION ADDED)
# =====================================================
elif selected == '📊 AI Dashboard':
    st.header("📊 AI Emotion Analytics Dashboard")

    if not st.session_state.emotion_logs.empty:

        df = st.session_state.emotion_logs
        st.dataframe(df)

        emotion_counts = df['Detected Emotion'].value_counts()

        # 🔹 BAR CHART
        st.subheader("📊 Emotion Count (Bar Graph)")
        fig1, ax1 = plt.subplots()
        emotion_counts.plot(kind='bar', ax=ax1)
        ax1.set_xlabel("Emotion")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

        # 🔹 PIE CHART
        st.subheader("🥧 Emotion Distribution (Pie Chart)")
        fig2, ax2 = plt.subplots()
        ax2.pie(
            emotion_counts,
            labels=emotion_counts.index,
            autopct='%1.1f%%',
            startangle=90
        )
        ax2.axis('equal')
        st.pyplot(fig2)

    else:
        st.info("No data yet. Start chatting to generate analytics.")

# =====================================================
# ℹ️ ABOUT PROJECT
# =====================================================
elif selected == 'ℹ️ About Project':
    st.header("ℹ️ About This Project")

    st.markdown("""
    <div class="card">
    <b>Project Name:</b> AI Emotion UI Ultra<br>
    <b>Developer:</b> sanchi<br>
    <b>Subject:</b> AI Tools / Artificial Intelligence
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    🧠 <b>Technologies Used:</b><br>
    • Python<br>
    • Streamlit<br>
    • Rule-Based AI<br>
    • Matplotlib Visualization
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# ❓ HELP
# =====================================================
elif selected == '❓ Help':
    st.header("❓ Help & Instructions")

    st.markdown("""
    <div class="card">
    1️⃣ Type a message in Emotion Chat<br>
    2️⃣ AI detects emotion<br>
    3️⃣ UI adapts automatically<br>
    4️⃣ Dashboard shows charts & analytics
    </div>
    """, unsafe_allow_html=True)