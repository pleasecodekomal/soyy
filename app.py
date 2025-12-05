import streamlit as st
import pandas as pd
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

import streamlit as st

GA_TRACKING_ID = "G-BLKEL70ZJN"

st.markdown(
    f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_TRACKING_ID}');
    </script>
    """,
    unsafe_allow_html=True,
)

# --- CONFIGURATION & SETUP ---
# 1. Load Environment Variables
load_dotenv()

# 2. Page Config
st.set_page_config(page_title="Hello Babbu", page_icon="🌻", layout="centered")

# 3. API Key Logic (Environment vs Sidebar)
api_key = os.getenv("GOOGLE_API_KEY")

with st.sidebar:
    st.header("⚙️ Settings")
    
    if api_key:
        st.success("✅ API Key loaded securely")
    else:
        # Fallback: If no .env file is found, ask user for key
        api_key = st.text_input("Enter Google Gemini API Key", type="password")
        st.caption("Get your key at [Google AI Studio](https://aistudio.google.com/app/apikey)")

    # Configure GenAI if key is available
    if api_key:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- HELPER: GEMINI GENERATION ---
def get_gemini_response(prompt):
    if not api_key:
        return "⚠️ Please check your API Key settings in the sidebar."
    try:
        # Update: Changed 'gemini-pro' to 'gemini-1.5-flash'
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"
    
# --- LOAD DATA ---
@st.cache_data
def load_music():
    return pd.read_csv("music_data.csv")

@st.cache_data
def load_movies():
    return pd.read_csv("movies_data.csv")

@st.cache_data
def load_race():
    return pd.read_csv("race_data.csv")

# Try to load Data
try:
    df_music = load_music()
except FileNotFoundError:
    st.error("⚠️ Error: 'music_data.csv' not found. Please run 'generate_data.py' first!")
    st.stop()

try:
    df_movies = load_movies()
except FileNotFoundError:
    st.error("⚠️ Error: 'movies_data.csv' not found. Please run 'generate_moviedata.py' first!")
    st.stop()

try:
    df_race = load_race()
except FileNotFoundError:
    st.error("⚠️ Error: 'race_data.csv' not found. Please run 'generate_racedata.py' first!")
    st.stop()


# --- CSS STYLING ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 20px;
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Hello Babbu! 👋")
st.markdown("Let's figure out the best plan for your day.")
st.divider()

# --- QUESTION 1: MOOD ---
st.subheader("1. How is your mood today?")
mood = st.select_slider(
    "Slide to select your mood:",
    options=["Very sad", "Sad", "Neutral", "Happy", "Very happy"],
    value="Neutral"
)

st.write("") # Spacer

# --- QUESTION 2: ACTIVITIES ---
st.subheader("2. What would you like to do today?")
activities = st.multiselect(
    "Select one or more activities:",
    ["Listen to music", "Exercise", "Read something new", "Watch something", "Let's talk about race"]
)

# --- QUESTION 3: CONDITIONAL LOGIC ---
# Variables to hold user selections
watch_format = None
watch_genre = "Any"
watch_vibe = mood 
read_genre = None
read_time = None
ex_duration = None
ex_time_of_day = None
ex_intensity = None

# 3a. WATCH LOGIC
if "Watch something" in activities:
    st.info("🎥 You selected 'Watch something'. Let's narrow it down.")
    col1, col2 = st.columns(2)
    with col1:
        watch_format = st.selectbox("Format?", ["Movie", "Series", "Documentary", "Short Film"])
    with col2:
        if watch_format:
            available_genres = sorted(df_movies[df_movies['Type'] == watch_format]['Genre'].unique().tolist())
            watch_genre = st.selectbox("Genre?", ["Any"] + available_genres)
    
    watch_vibe = st.select_slider("Select the vibe you want to watch:", 
                                  options=["Very sad", "Sad", "Neutral", "Happy", "Very happy"], 
                                  value=mood, key="watch_vibe")

# 3b. READ LOGIC (AI INTEGRATED)
if "Read something new" in activities:
    st.info("📚 You selected 'Read something new'. I'll find the perfect text for you.")
    col1, col2 = st.columns(2)
    with col1:
        read_genre = st.selectbox(
            "Topic/Genre?",
            ["Fiction Short Story", "Scientific Theory", "History Article", "Self-Help/Philosophy", "Biography", "Tech/AI", "Poetry"]
        )
    with col2:
        read_time = st.selectbox("Time available?", ["5 mins", "15 mins", "30 mins", "1 hour+"])

# 3c. EXERCISE LOGIC (AI INTEGRATED)
if "Exercise" in activities:
    st.info("💪 You selected 'Exercise'. Let's build a routine.")
    col1, col2, col3 = st.columns(3)
    with col1:
        ex_duration = st.selectbox("Duration?", ["10 mins", "20 mins", "30 mins", "45 mins", "1 hour"])
    with col2:
        ex_time_of_day = st.selectbox("Time of Day?", ["Morning", "Afternoon", "Evening", "Late Night"])
    with col3:
        ex_intensity = st.selectbox("Intensity?", ["Light (Stretching/Yoga)", "Medium (Cardio/Flow)", "High (HIIT/Strength)"])

# 3d. RACE LOGIC
if "Let's talk about race" in activities:
    st.info("🏎️ You selected 'Let's talk about race'. Preparing F1 vibes.")

st.divider()

# --- RESULT GENERATION ---
if st.button("✨ Give me a recommendation"):
    
    if not activities:
        st.warning("You didn't select any activities! Maybe just take a nap? 😴")
        st.stop()

    with st.spinner('Thinking...'):
        time.sleep(0.8) # UI Polish
    
    st.success(f"Result for a **{mood}** Babbu!")
    st.markdown("### 📝 The Plan:")
    
    for activity in activities:
        
        # --- 1. MUSIC (Local Data) ---
        if activity == "Listen to music":
            st.write(f"#### 🎵 Music Playlist ({mood})")
            filtered_df = df_music[df_music['Mood'] == mood]
            if not filtered_df.empty:
                sample = filtered_df.sample(n=min(5, len(filtered_df)))
                for _, row in sample.iterrows():
                    st.markdown(f"- **{row['Title']}** - *{row['Artist']}* ({row['Language']})")
            else:
                st.write("No songs found for this mood.")
            st.divider()

        # --- 2. WATCH (Local Data) ---
        elif activity == "Watch something":
            st.write(f"#### 🎥 Watch Recommendation")
            st.caption(f"Looking for: {watch_vibe} {watch_format} ({watch_genre})")
            
            filtered = df_movies[(df_movies['Type'] == watch_format) & (df_movies['Mood'] == watch_vibe)]
            if watch_genre != "Any":
                filtered = filtered[filtered['Genre'] == watch_genre]
            
            if not filtered.empty:
                sample = filtered.sample(n=min(5, len(filtered)))
                for _, row in sample.iterrows():
                    st.markdown(f"- 🎬 **{row['Title']}** *({row['Genre']})*")
            else:
                st.warning("No exact matches found in database. Try a broader search!")
            st.divider()

        # --- 3. RACE (Local Data) ---
        elif activity == "Let's talk about race":
            st.write(f"#### 🏎️ F1 Vibes")
            filtered = df_race[df_race['Mood'] == mood]
            if not filtered.empty:
                sample = filtered.sample(n=min(5, len(filtered)))
                for _, row in sample.iterrows():
                    st.markdown(f"- {row['Content']}")
            else:
                st.write("No specific F1 moments for this mood.")
            st.divider()

        # --- 4. READING (GEN AI) ---
        elif activity == "Read something new":
            st.write(f"#### 📚 Reading Suggestion")
            if not api_key:
                st.error("Please add GOOGLE_API_KEY to your .env file or the sidebar.")
            else:
                with st.spinner("Asking Gemini for reading ideas..."):
                    # Construct Prompt
                    prompt = (
                        f"I am feeling {mood}. I have exactly {read_time} to read. "
                        f"Recommend 3 specific {read_genre} pieces (books, articles, or specific theories). "
                        f"For each, explain in 1 sentence why it fits my {mood} mood. "
                        f"Do not give generic advice, give specific titles or theories."
                    )
                    ai_response = get_gemini_response(prompt)
                    st.markdown(ai_response)
            st.divider()

        # --- 5. EXERCISE (GEN AI) ---
        elif activity == "Exercise":
            st.write(f"#### 💪 Workout Routine")
            if not api_key:
                st.error("Please add GOOGLE_API_KEY to your .env file or the sidebar.")
            else:
                with st.spinner("Designing your workout..."):
                    # Construct Prompt
                    prompt = (
                        f"I am feeling {mood}. It is currently {ex_time_of_day}. "
                        f"Create a {ex_duration} {ex_intensity} workout routine. "
                        f"List the exercises with rep counts or duration. "
                        f"Keep it safe and fun."
                    )
                    ai_response = get_gemini_response(prompt)
                    st.markdown(ai_response)
            st.divider()
            
