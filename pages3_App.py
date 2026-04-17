import streamlit as st
st.set_page_config(
    page_title="PORTFOLIO | Dindo", 
    page_icon="D", 
    layout="wide"
)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');
    
    /* Background and Global Text */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #0a0a0f 100%);
    }
    
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        color: #e8e6f0;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(160deg, #0f0f1a, #13131f);
        border-right: 1px solid #1e1e2e;
    }

    /* Headings */
    h1, h2, h3 { 
        font-family: 'Syne', sans-serif !important; 
        letter-spacing: -0.02em; 
    }

    /* --- ANIMATED D LOGO --- */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }

    .animated-d {
        font-family: 'Syne', sans-serif;
        font-size: 8rem;
        font-weight: 800;
        color: #e8e6f0;
        text-shadow: 0 0 10px #7c3aed, 0 0 20px #7c3aed, 0 0 40px #7c3aed;
        animation: pulse 2s infinite alternate, glitch 3s infinite;
    }

    @keyframes pulse {
        from { transform: scale(1); opacity: 0.8; text-shadow: 0 0 10px #7c3aed; }
        to { transform: scale(1.05); opacity: 1; text-shadow: 0 0 30px #a78bfa, 0 0 50px #7c3aed; }
    }

    @keyframes glitch {
        0% { transform: translate(0); }
        2% { transform: translate(-2px, 2px); }
        4% { transform: translate(-2px, -2px); }
        6% { transform: translate(0); }
        100% { transform: translate(0); }
    }

    hr { border-color: #1e1e2e; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("<p style='color:#7c3aed; font-weight:600; letter-spacing:0.2em; padding-top:2rem;'>SYSTEM INITIALIZED</p>", unsafe_allow_html=True)
    
    st.markdown("""
<h1 style="
    font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">Welcome to My Page</h1>
<hr style="border-color:#1e1e2e; margin-bottom:2rem;">
""", unsafe_allow_html=True)
    
    st.write("Navigate through the sidebar to explore my technical profile, projects, and career journey.")
    st.divider()
    
    st.info("👈 Use the sidebar to start exploring modules.")

with col_right:
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
            <div class="logo-container">
                <span class="animated-d">D</span>
            </div>
            <p style='text-align:center; font-family:Syne; font-weight:700; color:#a78bfa; letter-spacing:0.1em; text-transform:uppercase;'>
                Dindo R. Cañabano
            </p>
        """, unsafe_allow_html=True)
