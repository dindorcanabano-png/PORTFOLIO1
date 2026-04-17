import streamlit as st

st.set_page_config(page_title="About | Dindo", page_icon="D", layout="wide")

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
h1, h2, h3 { font-family: 'Syne', sans-serif; letter-spacing:-0.02em; }
hr { border-color: #1e1e2e; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family:'Syne',sans-serif; font-size:0.82rem; font-weight:600;
    letter-spacing:0.18em; color:#7c3aed; text-transform:uppercase;
    padding-top: 1.5rem; margin-bottom:0.5rem;
">Get To Know Me</p>
<h1 style="
    font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">About Me</h1>
<hr style="border-color:#1e1e2e; margin-bottom:2rem;">
""", unsafe_allow_html=True)

col_bio, col_info = st.columns([1.5, 1], gap="large")

with col_bio:
    st.markdown("""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:16px;
        padding:1.75rem 2rem; margin-bottom:1.25rem;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#a78bfa; font-size:1rem; margin-bottom:0.75rem;">
            Who I Am
        </p>
        <p style="color:#b0afc8; line-height:1.8; font-size:0.95rem; margin:0;">
            I'm Dindo, a driven Computer Science student with a deep passion for
            building functional, beautiful, and impactful software. I thrive at the
            intersection of <strong style="color:#e8e6f0;">design and program </strong>
        </p>
        <p style="color:#b0afc8; line-height:1.8; font-size:0.95rem; margin-top:1rem 0 0;">
            Whether it's crafting a web app from scratch, designing a seamless interface,
            or solving a complex logic problem, I bring curiosity and commitment to
            everything I create.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-family:'Syne',sans-serif; font-weight:700;
              color:#e8e6f0; font-size:1rem; margin:1.5rem 0 1rem;">
        Education Timeline
    </p>
    """, unsafe_allow_html=True)

    timeline_items = [
    ("2024", "Hackathon Participant",
     "Part of a hackathon team that participated in an official event as a programmer, contributing to visuals and presentation materials."),

    ("2025", "Hackathon Team Member",
     "Continued participation in hackathon events, working with a team, as a defender."),

    ("Present", "Student Programmer / Editor",
     "Currently studying as programmer while also handling editing and graphic design tasks.")
]

    for year, title, desc in timeline_items:
        st.markdown(f"""
        <div style="
            display:flex; gap:1rem; margin-bottom:1rem; align-items:flex-start;
        ">
            <div style="text-align:right; min-width:64px;">
                <span style="font-family:'Syne',sans-serif; font-size:0.75rem;
                             font-weight:700; color:#7c3aed;">{year}</span>
            </div>
            <div style="
                width:10px; height:10px; border-radius:50%; margin-top:4px;
                background:#7c3aed; flex-shrink:0;
                box-shadow:0 0 10px rgba(124,58,237,0.5);
            "></div>
            <div style="
                background:#13131f; border:1px solid #2a2a3e; border-radius:10px;
                padding:0.9rem 1.1rem; flex:1;
            ">
                <p style="font-family:'Syne',sans-serif; font-weight:700;
                          color:#e8e6f0; margin:0 0 0.3rem; font-size:0.9rem;">
                    {title}
                </p>
                <p style="color:#6b6b8a; font-size:0.82rem; line-height:1.6; margin:0;">
                    {desc}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #13131f, #1a1a2e);
        border:1px solid #2a2a3e; border-radius:16px; padding:1.75rem;
        margin-bottom:1.25rem;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#a78bfa; margin-bottom:1.2rem; font-size:1rem;">
            Quick Info
        </p>
    """, unsafe_allow_html=True)

    info_items = [
        ("Role", "Student Developer"),
        ("Degree", "CS Computer Science"),
        ("Focus", "Full-Stack Development"),
        ("Location", "Philippines"),
        ("Status", "Open to Opportunities"),
    ]
    for label, value in info_items:
        st.markdown(f"""
        <div style="
            display:flex; justify-content:space-between; align-items:center;
            padding:0.65rem 0; border-bottom:1px solid #1e1e2e;
        ">
            <span style="color:#6b6b8a; font-size:0.82rem;">{label}</span>
            <span style="color:#e8e6f0; font-size:0.85rem; font-weight:500;
                         text-align:right; max-width:60%;">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:16px;
        padding:1.75rem; margin-top:0.25rem;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#a78bfa; margin-bottom:1.2rem; font-size:1rem;">
            Career Goals
        </p>
    """, unsafe_allow_html=True)

    goals = [
        "Become a Full-Stack Developer",
        "Become a pro Editor",
        "Become a network analysis",
        "Grow a professional network in tech",
    ]
    for g in goals:
        st.markdown(f"""
        <div style="
            display:flex; align-items:center; gap:0.75rem;
            padding:0.5rem 0; border-bottom:1px solid #1a1a2a;
        ">
            <div style="
                width:6px; height:6px; border-radius:50%;
                background:#7c3aed; flex-shrink:0;
            "></div>
            <span style="color:#b0afc8; font-size:0.85rem;">{g}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<p style="font-family:'Syne',sans-serif; font-weight:700;
          color:#e8e6f0; font-size:1rem; margin-bottom:1rem;">
    Fun Facts About Me
</p>
""", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
facts = [
    (f1, "Night Owl", "Most of my best code gets written after midnight when the world is quiet."),
    (f2, "Problem Solver", "I enjoy debugging as much as building — every bug is a puzzle to crack."),
    (f3, "Lifelong Learner", "I spend at least 30 minutes daily exploring new tech concepts and tutorials."),
]
for col, title, text in facts:
    with col:
        st.markdown(f"""
        <div style="
            background:#13131f; border:1px solid #2a2a3e; border-radius:14px;
            padding:1.25rem; height:100%;
        ">
            <p style="font-family:'Syne',sans-serif; font-weight:700;
                      color:#a78bfa; margin-bottom:0.5rem; font-size:0.9rem;">
                {title}
            </p>
            <p style="color:#6b6b8a; font-size:0.83rem; line-height:1.6; margin:0;">
                {text}
            </p>
        </div>
        """, unsafe_allow_html=True)
