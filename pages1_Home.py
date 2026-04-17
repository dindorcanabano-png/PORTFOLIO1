import streamlit as st

st.set_page_config(page_title="Home | Dindo", page_icon="🏠", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=JetBrains+Mono&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #0a0a0f 100%);
    }

    h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
    p, span { font-family: 'DM Sans', sans-serif; }

    /* --- DASHBOARD GLITCH ANIMATION --- */
    .dashboard-title {
        font-family: 'Syne', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        text-transform: uppercase;
        position: relative;
        background: linear-gradient(90deg, #fff, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glitch 3s infinite;
    }

    @keyframes glitch {
        0%, 100% { transform: skew(0); }
        20% { transform: skew(-2deg); filter: hue-rotate(90deg); }
        21% { transform: skew(5deg); }
        25% { transform: skew(0); }
    }

    /* --- ANIMATED D LOGO (MINI VERSION) --- */
    .logo-glow {
        font-family: 'Syne', sans-serif;
        font-size: 5rem;
        font-weight: 800;
        color: #e8e6f0;
        text-shadow: 0 0 15px #7c3aed;
        animation: pulse 2s infinite alternate;
        display: inline-block;
        margin-right: 20px;
    }

    @keyframes pulse {
        from { transform: scale(1); text-shadow: 0 0 10px #7c3aed; }
        to { transform: scale(1.1); text-shadow: 0 0 30px #a78bfa, 0 0 50px #7c3aed; }
    }

    /* Custom Metric Card */
    .metric-card {
        background: rgba(19, 19, 31, 0.8);
        border: 1px solid #7c3aed33;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .metric-card:hover {
        border-color: #7c3aed;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(124, 58, 237, 0.2);
    }

    .terminal-code {
        font-family: 'JetBrains Mono', monospace;
        color: #7c3aed;
        font-size: 0.8rem;
        letter-spacing: 2px;
    }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='terminal-code'>[ ACCESSING_CORE_SYSTEM ]</p>", unsafe_allow_html=True)

col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.markdown('<div class="logo-glow">D</div>', unsafe_allow_html=True)

with col_title:
    st.markdown("""
        <h1 style="
        font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800;
        background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        margin-bottom:0.25rem;
        ">DASHBOARD</h1>
        <hr style="border-color:#1e1e2e; margin-bottom:2rem;">
""", unsafe_allow_html=True)

st.write("Welcome to the core management interface. Here is a summary of my current technical status and focus areas.")

st.divider()

col1, col2, col3, col4 = st.columns(4)

stats = [
    ("PROJECTS", "3+", "⚡"),
    ("EXPERIENCE", "2 YRS", "🏆"),
    ("CLIENTS", "01+", "🤝"),
    ("SYSTEM_UP", "99.9%", "⚙️")
]

for col, (label, val, icon) in zip([col1, col2, col3, col4], stats):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 5px;">{icon}</div>
                <div style="font-size: 2rem; font-weight: 800; color: #fff;">{val}</div>
                <div style="color: #7c3aed; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;">{label}</div>
            </div>
        """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
