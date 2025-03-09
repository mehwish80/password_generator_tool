import streamlit as st
import random
import string
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase letters (A-Z)")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include lowercase letters (a-z)")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include numbers (0-9)")
        
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};:,.<>?]", password):
        score += 1
    else:
        feedback.append("❌ Include special characters (!@#$%^&*)")

    if score >= 5:
        st.success("🔒 Strong Password!")
    elif score >= 3:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password")

    if feedback:
        with st.expander("💡 Password Improvement Tips"):
            for tip in feedback:
                st.write(tip)

st.set_page_config(
    page_title="Password Generator & Checker",
    page_icon="🔒",
    layout="centered"
)

# Simplified CSS with only essential styles
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    .main {
        font-family: 'Poppins', sans-serif;
        padding: 1.5rem;
        max-width: 900px;
        margin: 0 auto;
    }

    .title-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .main-title {
        color: white;
        font-size: 1.8rem !important;
        font-weight: 600;
        margin: 0;
        padding: 0;
    }

    .password-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        font-size: 0.9rem !important;
        width: 100%;
    }

    .generated-password {
        background: #f8fafc;
        padding: 0.8rem;
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        font-family: monospace;
        font-size: 1rem;
        text-align: center;
        margin: 0.8rem 0;
    }

    /* Make all text elements consistent size */
    .stRadio label, .stCheckbox label, .stSlider div[data-baseweb="typography"],
    .stSuccess, .stWarning, .stError, .streamlit-expanderHeader {
        font-size: 0.9rem !important;
    }

    /* Custom Input Field Styling */
    .stTextInput input {
        background: #f8fafc !important;
        border: 2px solid #667eea !important;
        border-radius: 8px !important;
        padding: 0.8rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.1) !important;
    }

    .stTextInput input:focus {
        border-color: #764ba2 !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2) !important;
        transform: translateY(-1px);
    }

    .stTextInput input::placeholder {
        color: #a0aec0 !important;
    }

    .stTextInput label {
        color: #4a5568 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }

    /* Footer Styling */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.1);
    }

    .footer-text {
        color: white;
        font-size: 0.9rem;
        margin: 0;
        padding: 0;
        opacity: 0.9;
    }

    .footer-text span {
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    .footer-heart {
        color: #ff4b6c;
        font-size: 1.1rem;
        animation: heartbeat 1.5s ease infinite;
    }

    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">🔒 Password Generator Tool</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="password-container">', unsafe_allow_html=True)

# Rest of your existing Python code remains the same
option = st.radio(
    "Choose your password method:",
    ["🎲 Generate Password", "✍️ Enter Password"]
)

if option == "🎲 Generate Password":
    col1, col2 = st.columns([3, 1])
    with col1:
        length = st.slider("Password Length", 8, 32, 16)
    
    col1, col2 = st.columns(2)
    with col1:
        use_digits = st.checkbox("Include Numbers", value=True)
    with col2:
        use_special = st.checkbox("Include Symbols", value=True)

    if st.button("Generate Password 🎲"):
        chars = string.ascii_letters
        if use_digits:
            chars += string.digits
        if use_special:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        password = ''.join(random.choice(chars) for _ in range(length))
        
        st.markdown(f"""
            <div class="generated-password">
                {password}
            </div>
        """, unsafe_allow_html=True)
        
        check_password_strength(password)

else:
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength 🔍"):
        if password:
            check_password_strength(password)
        else:
            st.warning("Please enter a password")

st.markdown('</div>', unsafe_allow_html=True)

# Add footer
st.markdown("""
    <div class="footer">
        <p class="footer-text">
            Developed with <span class="footer-heart">❤️</span> by <span>Mehwish Shakir</span> | web Developer
        </p>
    </div>
""", unsafe_allow_html=True)
