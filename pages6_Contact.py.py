import streamlit as st
import re

st.set_page_config(page_title="Contact | Dindo", page_icon="D", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0f; color: #e8e6f0;
}
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0f0f1a, #13131f);
    border-right: 1px solid #1e1e2e;
}
h1, h2, h3 { font-family: 'Syne', sans-serif; letter-spacing: -0.02em; }
hr { border-color: #1e1e2e; }
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background-color: #13131f !important;
    border: 1px solid #2a2a3e !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white; border: none; border-radius: 10px;
    padding: 0.6rem 2rem; font-family: 'Syne', sans-serif;
    font-weight: 700; font-size:1rem; width:100%;
    box-shadow: 0 4px 20px rgba(124,58,237,0.4);
}
label { color: #9090a8 !important; font-size: 0.85rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family:'Syne',sans-serif; font-size:0.82rem; font-weight:600;
    letter-spacing:0.18em; color:#7c3aed; text-transform:uppercase;
    padding-top:1.5rem; margin-bottom:0.5rem;
">Reach Out</p>
<h1 style="
    font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">Contact Me</h1>
<hr style="border-color:#1e1e2e; margin-bottom:2rem;">
""", unsafe_allow_html=True)

col_form, col_info = st.columns([1.4, 1], gap="large")

with col_form:
    st.markdown("""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:18px;
        padding:2rem;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#e8e6f0; font-size:1.1rem; margin-bottom:0.35rem;">
            Send a Message
        </p>
        <p style="color:#6b6b8a; font-size:0.85rem; margin-bottom:1.5rem;">
            Fill in the form below and I'll get back to you as soon as possible.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name", placeholder="Your full name")
        with c2:
            email = st.text_input("Email Address", placeholder="you@example.com")

        subject = st.selectbox("Subject", [
            "General Inquiry",
            "Project Collaboration",
            "Other",
        ])

        message = st.text_area(
            "Message",
            placeholder="Tell me more about your inquiry...",
            height=160,
        )

        submitted = st.form_submit_button("Send Message")

        if submitted:
            errors = []
            if not name.strip():
                errors.append("Full name is required.")
            if not email.strip():
                errors.append("Email address is required.")
            elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
                errors.append("Please enter a valid email address.")
            if not message.strip() or len(message.strip()) < 10:
                errors.append("Message must be at least 10 characters.")

            if errors:
                for err in errors:
                    st.error(err)
            else:
                st.success(
                    f"Thank you, **{name}**! Your message has been sent. "
                    "I'll respond within 24-48 hours."
                )
                st.balloons()

with col_info:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #13131f, #1a1a2e);
        border:1px solid #2a2a3e; border-radius:16px; padding:1.75rem;
        margin-bottom:1.25rem;
    ">
        <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem;">
            <div style="
                width:10px; height:10px; border-radius:50%; background:#22c55e;
                box-shadow:0 0 10px #22c55e;
            "></div>
            <p style="font-family:'Syne',sans-serif; font-weight:700;
                      color:#22c55e; margin:0; font-size:0.95rem;">
                Currently Available
            </p>
        </div>
        <p style="color:#b0afc8; font-size:0.85rem; line-height:1.7; margin:0;">
            I am a student open to freelance projects and part-time collaborations. I am responsive and usually reply within a short time.
            within <strong style="color:#e8e6f0;">24 hours</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-family:'Syne',sans-serif; font-weight:700;
              color:#a78bfa; font-size:0.95rem; margin-bottom:1rem;">
        Connect With Me
    </p>
    """, unsafe_allow_html=True)

    socials = [
        ("GitHub", "github.com/Dindo", "View repositories and source code", "#e8e6f0"),
        ("LinkedIn", "linkedin.com/in/Dindo", "Professional profile", "#60a5fa"),
        ("Facebook", "facebook.com/Dindo", "Personal social page", "#818cf8"),
        ("Email", "Dindo@email.com", "Direct email contact", "#34d399"),
    ]

    for platform, handle, desc, color in socials:
        st.markdown(f"""
        <div style="
            background:#13131f; border:1px solid #2a2a3e; border-radius:12px;
            padding:0.9rem 1.1rem; margin-bottom:0.65rem;
            display:flex; align-items:center; gap:0.85rem;
        ">
            <div style="
                width:38px; height:38px; border-radius:9px; flex-shrink:0;
                background:{color}18; border:1px solid {color}33;
                display:flex; align-items:center; justify-content:center;
            ">
                <span style="font-family:'Syne',sans-serif; font-weight:800;
                             color:{color}; font-size:0.9rem;">
                    {platform[0]}
                </span>
            </div>
            <div style="flex:1; min-width:0;">
                <p style="font-weight:600; color:#e8e6f0; margin:0; font-size:0.88rem;">
                    {platform}
                </p>
                <p style="color:#6b6b8a; font-size:0.77rem; margin:0;
                          overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                    {handle}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:14px;
        padding:1.25rem; margin-top:0.5rem; text-align:center;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:800;
                  color:#a78bfa; font-size:1.5rem; margin:0;">24h</p>
        <p style="color:#6b6b8a; font-size:0.8rem; margin:0.25rem 0 0;">
            Average response time
        </p>
    </div>
    """, unsafe_allow_html=True)
