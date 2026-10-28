from datetime import date, datetime

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Khylla Laine Menardo | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)


NAME = "Khylla Laine C. Menardo"
SECTION = "G01"
PROGRAM = "BS Information Technology"
YEAR_LEVEL = "3rd Year"
SCHOOL = "Cebu Institute of Technology – University"
LOCATION = "Mandaue City, Cebu"
EMAIL = "khyllalaine.menardo@cit.edu"
GITHUB = "https://github.com/khyllalainemenardo"
LINKEDIN = "https://linkedin.com/in/khyllalainemenardo"
PHOTO_PATH = "photo.jpg"

TAGLINE = "Third year BSIT student at Cebu Institute of Technology – University."

SHORT_BIO = (
    "I go by Khylla. I study BS Information Technology at Cebu Institute of Technology – "
    "University, currently in my third year. Most of my time goes to learning how things "
    "work and trying out whatever area of IT catches my interest."
)


AUTOBIOGRAPHY = {
    "🏡 Background": (
        "I'm 24 and from Mandaue City, Cebu. I grew up in a busy city, and it made me curious "
        "about how things run behind the scenes. That curiosity is a big part of why I ended up "
        "in IT. I came into the field a little later than some of my classmates, after studying "
        "business in senior high, and I think that path gave me a different way of looking at "
        "technology: not just how it works, but who it's for. These days my routine is fairly "
        "simple. Most of my time goes to schoolwork and side projects. When I'm not studying, "
        "I'm usually playing video games or sitting with my cats, who have opinions about how "
        "long I stay at my desk."
    ),
    "🎓 Education": (
        "I went to De La Salle Andres Soriano Memorial College for junior high, where I built a "
        "strong foundation in core subjects and first got curious about computers through school "
        "activities and projects. I stayed there for senior high under the ABM strand, studying "
        "accounting, business, and management, which later led me to explore how technology "
        "supports the way organizations work. Since 2023 I've been taking BS Information "
        "Technology at CIT-U, studying web development, database design, and systems "
        "integration, and building projects for each along the way."
    ),
    "💡 Interests": (
        "Music is always on in the background, usually a Spotify playlist that fits whatever "
        "I'm doing, whether that's coding, commuting, or winding down at night. I read whenever "
        "I can, on my phone or from a printed book; I like ebooks for convenience, but nothing "
        "beats turning real pages. When I need a break from screens, I go on nature trips. "
        "Being outdoors resets my head better than anything else. I also love anime, with an "
        "unreasonable soft spot for Frieren, films (including the ones that put me to sleep), "
        "and video games, usually with a cat nearby."
    ),
    "🎯 Goals": (
        "I want to see more of the world than the city I grew up in. After graduating, my goal "
        "is to work abroad, ideally in Switzerland, where I'd like to grow as an IT professional "
        "and learn how teams work in a different culture. Along the way I want to explore other "
        "countries too. In the long run, I want to become a philanthropist. Whatever I build "
        "in my career, I want it to come back to people who need it, whether that's supporting "
        "students who can't afford school, helping my community in Cebu, or funding causes "
        "that give others the chances I was given."
    ),
}


MILESTONES = [
    (2014, "Junior High School", "Started at De La Salle Andres Soriano Memorial College and first got curious about computers."),
    (2021, "Senior High School, ABM Strand", "Studied accounting, business, and management at DLS-ASMC."),
    (2023, "Started BS Information Technology", "Enrolled at Cebu Institute of Technology – University."),
    (2024, "First game project", "Built Lost Echoes, a turn-based story game, with my group for Object-Oriented Programming 1."),
    (2025, "TideBound", "Worked with my group on TideBound, a naval strategy game in Java Swing."),
    (2026, "First React projects", "Set up Vite for the first time and rebuilt my About Me page in React for CSIT340."),
]


SKILLS = [

    ("HTML & CSS",             "Web",         85, 3.0),
    ("JavaScript",             "Web",         70, 2.5),
    ("React",                  "Web",         65, 1.0),
    ("Tailwind CSS",           "Web",         70, 1.0),
    ("Java",                   "Programming", 75, 3.0),
    ("Python",                 "Programming", 55, 1.5),
    ("Database design / SQL",  "Data",        65, 2.0),
    ("Systems integration",    "Systems",     50, 1.0),
    ("Git & GitHub",           "Tools",       70, 2.5),
]

SOFT_SKILLS = ["Teamwork", "Communication", "Problem solving", "Curiosity and self-learning", "Business thinking"]


PROJECTS = [
    {
        "title": "TideBound",
        "year": 2025,
        "role": "Developer — character abilities and UI",
        "tools": ["Java", "Swing", "OOP", "MVC"],
        "summary": (
            "A turn-based naval strategy game that takes classic Battleship and adds "
            "character-driven gameplay. Players pick one of eight commanders, each with special "
            "abilities like healing, stealth, shields or spreading a virus across the enemy board, "
            "then place a five-ship fleet on a 10×10 grid and battle it out."
        ),
        "outcome": (
            "A playable desktop game with a Campaign mode against AI opponents of increasing "
            "difficulty and a hot-seat Local Multiplayer mode, plus animations, ocean backgrounds, "
            "sound effects and music. The code is organized with the MVC pattern into separate "
            "packages for the models, game logic, AI and GUI."
        ),
        "link": "https://github.com/JiiiJiii26/Dagat2Game",
        "type": "Group",
    },
    {
        "title": "Lost Echoes",
        "year": 2024,
        "role": "Programmer (group of five)",
        "tools": ["Java", "OOP", "Console"],
        "summary": (
            "A turn-based story game that runs in the console, made for CSIT 227 (Object-Oriented "
            "Programming 1)."
        ),
        "outcome": (
            "A complete, playable Java game where we put classes, objects and other OOP "
            "concepts to work in a real project, and my first experience building a game as a team."
        ),
        "link": "https://github.com/khyllalainemenardo/LostEcoes",
        "type": "Group",
    },
    {
        "title": "About Me in React",
        "year": 2026,
        "role": "Solo developer",
        "tools": ["React", "Tailwind CSS"],
        "summary": "My first React lab for CSIT340, rebuilt from a plain HTML page.",
        "outcome": "Turned a static page into reusable React components styled with Tailwind.",
        "link": "https://github.com/khyllalainemenardo/CSIT340-Lab1-Menardo",
        "type": "Academic",
    },
    {
        "title": "CSIT340 React Project",
        "year": 2026,
        "role": "Solo developer",
        "tools": ["React", "JavaScript"],
        "summary": "My starter React project.",
        "outcome": "Where I first set up Vite and learned how components fit together.",
        "link": "https://github.com/khyllalainemenardo/CSIT340_reactproj",
        "type": "Academic",
    },
    {
        "title": "Order Inventory",
        "year": 2026,
        "role": "Solo developer",
        "tools": ["Java"],
        "summary": "A Java application for keeping track of orders and the stock they draw from.",
        "outcome": "Built the whole app on my own, which gave me practice structuring a Java program around real records like orders and inventory.",
        "link": "https://github.com/khyllalainemenardo/order-inventory",
        "type": "Academic",
    },
    {
        "title": "SIA Project",
        "year": 2026,
        "role": "Solo developer",
        "tools": ["JavaScript", "Systems integration"],
        "summary": "A project for Systems Integration and Architecture that connects separate services into one system.",
        "outcome": "Showed me how separate parts of a system talk to each other, and how to make them work as one.",
        "link": "https://github.com/khyllalainemenardo/SIA_Project",
        "type": "Academic",
    },
]


st.markdown(
    """
    <style>
      .hero-name {font-size: 2.6rem; font-weight: 800; line-height: 1.1; margin: 0;}
      .hero-tag  {font-size: 1.1rem; opacity: .75; margin-top: .3rem;}
      .pill {display:inline-block; padding:.15rem .6rem; margin:.15rem .2rem .15rem 0;
             border-radius:999px; font-size:.8rem; background: rgba(214,51,132,.12);
             color:#d63384; border:1px solid rgba(214,51,132,.25);}
      .tl-year {font-weight:800; color:#d63384; font-size:1.1rem;}
      .footer {text-align:center; opacity:.6; font-size:.85rem; padding-top:1rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


def pills(items):
    return "".join(f'<span class="pill">{i}</span>' for i in items)


if "messages" not in st.session_state:
    st.session_state.messages = []
if "likes" not in st.session_state:
    st.session_state.likes = 0
if "visits" not in st.session_state:
    st.session_state.visits = 1


skills_df = pd.DataFrame(SKILLS, columns=["Skill", "Category", "Level", "Years"])
projects_df = pd.DataFrame(
    [
        {
            "Title": p["title"],
            "Year": p["year"],
            "Type": p["type"],
            "Role": p["role"],
            "Tools": ", ".join(p["tools"]),
        }
        for p in PROJECTS
    ]
)
all_tools = sorted({t for p in PROJECTS for t in p["tools"]})


with st.sidebar:
    st.markdown(f"### 🌸 {NAME}")
    st.caption(f"Section **{SECTION}** · {PROGRAM}, {YEAR_LEVEL}")
    st.divider()

    st.markdown("**Quick facts**")
    st.write(f"📍 {LOCATION}")
    st.write(f"🏫 {SCHOOL}")
    st.write(f"✉️ {EMAIL}")

    st.divider()
    st.markdown("**Display options**")
    show_timeline = st.checkbox("Show milestone timeline", value=True)
    chart_style = st.radio("Skills chart style", ["Bar", "Area", "Line"], horizontal=True)
    accent_greeting = st.selectbox(
        "Greeting language",
        ["English", "Cebuano", "Filipino"],
        help="Changes the greeting at the top of the page.",
    )

    st.divider()
    st.link_button("🐙 GitHub profile", GITHUB, width="stretch")
    if LINKEDIN:
        st.link_button("💼 LinkedIn", LINKEDIN, width="stretch")

    if st.button("💖 Leave a like", width="stretch"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!", icon="💖")
    st.caption(f"Likes this session: **{st.session_state.likes}**")


greeting = {
    "English": "Hello, I'm",
    "Cebuano": "Maayong adlaw, ako si",
    "Filipino": "Kumusta, ako si",
}[accent_greeting]

st.title(f"🌸 {NAME}")
st.caption(f"{PROGRAM} · {YEAR_LEVEL} · Section {SECTION}")

hero_photo, hero_text = st.columns([1, 2.4], gap="large")

with hero_photo:
    try:
        st.image(PHOTO_PATH, width="stretch", caption=NAME)
    except Exception:

        h, w = 320, 320
        y, x = np.mgrid[0:h, 0:w]
        grad = np.zeros((h, w, 3), dtype=np.uint8)
        grad[..., 0] = (214 - 60 * y / h).astype(np.uint8)
        grad[..., 1] = (120 + 60 * x / w).astype(np.uint8)
        grad[..., 2] = (180 + 50 * (x + y) / (w + h)).astype(np.uint8)
        st.image(grad, width="stretch",
                 caption="📷 Photo stand-in — add photo.jpg to replace")

with hero_text:
    st.markdown(f'<p class="hero-tag">{greeting}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-name">{NAME}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-tag">{TAGLINE}</p>', unsafe_allow_html=True)
    st.write("")
    st.write(SHORT_BIO)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects", len(PROJECTS))
    m2.metric("Skills tracked", len(skills_df))
    m3.metric("Top skill level", f"{int(skills_df['Level'].max())}%")
    m4.metric("Messages received", len(st.session_state.messages),
              delta=f"+{st.session_state.likes} likes" if st.session_state.likes else None)

st.divider()


tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["📖 Autobiography", "🛠️ Skills", "🗂️ Projects", "✉️ Contact"]
)


with tab_story:
    st.header("My Story")

    left, right = st.columns(2, gap="large")
    parts = list(AUTOBIOGRAPHY.items())
    for i, (heading, text) in enumerate(parts):
        with (left if i % 2 == 0 else right):
            with st.container(border=True):
                st.subheader(heading)
                st.write(text)

    if show_timeline:
        st.subheader("🗓️ Milestones")
        year_min, year_max = min(m[0] for m in MILESTONES), max(m[0] for m in MILESTONES)
        yr_range = st.slider(
            "Show milestones between",
            min_value=year_min, max_value=year_max,
            value=(year_min, year_max),
        )
        shown = [m for m in MILESTONES if yr_range[0] <= m[0] <= yr_range[1]]
        if not shown:
            st.info("No milestones in that range.")
        for year, title, desc in shown:
            c_year, c_body = st.columns([1, 6])
            c_year.markdown(f'<div class="tl-year">{year}</div>', unsafe_allow_html=True)
            c_body.markdown(f"**{title}** — {desc}")

    with st.expander("✨ A few things people might not know about me"):
        st.markdown(
            "- My cats have opinions about how long I stay at my desk.\n"
            "- I have an unreasonable soft spot for *Frieren*.\n"
            "- Some films put me to sleep, and I still count them as films I like.\n"
            "- One day I want to live and work in Switzerland.\n"
            "- I still prefer the smell of a printed book over an ebook, even if I read both.\n"
            "- I came into IT from the ABM strand, so I think about how tech fits the way organizations work."
        )


with tab_skills:
    st.header("Skills")
    st.write(
        "I'm studying web development, database design, and systems integration, and building projects for each along the way. Lately most of that has been React."
    )

    f1, f2 = st.columns([2, 1])
    with f1:
        cats = st.multiselect(
            "Filter by category",
            options=sorted(skills_df["Category"].unique()),
            default=sorted(skills_df["Category"].unique()),
        )
    with f2:
        min_level = st.slider("Minimum level", 0, 100, 0, step=5)

    filtered = skills_df[
        skills_df["Category"].isin(cats) & (skills_df["Level"] >= min_level)
    ].sort_values("Level", ascending=False)

    chart_col, table_col = st.columns([1, 1], gap="large")
    with chart_col:
        st.subheader("Proficiency (self-rated, 0–100)")
        if skills_df["Level"].sum() == 0:
            st.info("✏️ Fill in your own skill levels in the SKILLS list at the top of app.py to see the chart.")
        elif filtered.empty:
            st.warning("No skills match those filters.")
        else:
            chart_data = filtered.set_index("Skill")[["Level"]]
            if chart_style == "Bar":
                st.bar_chart(chart_data, color="#d63384", horizontal=True)
            elif chart_style == "Area":
                st.area_chart(chart_data, color="#d63384")
            else:
                st.line_chart(chart_data, color="#d63384")

    with table_col:
        st.subheader("Skill table")
        st.dataframe(
            filtered,
            hide_index=True,
            width="stretch",
            column_config={
                "Level": st.column_config.ProgressColumn(
                    "Level", min_value=0, max_value=100, format="%d%%"
                ),
                "Years": st.column_config.NumberColumn("Years", format="%.1f"),
            },
        )

    st.subheader("Soft skills")
    st.markdown(pills(SOFT_SKILLS), unsafe_allow_html=True)

    st.download_button(
        "⬇️ Download my skills (CSV)",
        data=skills_df.to_csv(index=False).encode("utf-8"),
        file_name=f"{NAME.replace(' ', '_')}_skills.csv",
        mime="text/csv",
    )


with tab_projects:
    st.header("Projects")

    p1, p2 = st.columns([2, 1])
    with p1:
        tool_filter = st.multiselect("Show projects that use", all_tools)
    with p2:
        sort_by = st.selectbox("Sort by", ["Newest first", "Oldest first", "Title"])

    proj = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if sort_by == "Newest first":
        proj.sort(key=lambda p: p["year"], reverse=True)
    elif sort_by == "Oldest first":
        proj.sort(key=lambda p: p["year"])
    else:
        proj.sort(key=lambda p: p["title"])

    show_details = st.checkbox("Show full details on each card", value=True)

    if not proj:
        st.info("No projects use those tools.")

    cols = st.columns(3, gap="medium")
    for i, p in enumerate(proj):
        with cols[i % 3]:
            with st.container(border=True):
                st.subheader(p["title"])
                st.caption(f"{p['type']} · {p['year']}")
                st.markdown(f"**Role:** {p['role']}")
                st.markdown(pills(p["tools"]), unsafe_allow_html=True)
                if show_details:
                    st.write(p["summary"])
                    st.markdown(f"**Outcome:** {p['outcome']}")
                if p["link"]:
                    st.link_button("Open project ↗", p["link"], width="stretch")

    st.subheader("At a glance")
    g1, g2 = st.columns([3, 2], gap="large")
    with g1:
        st.table(projects_df)
    with g2:
        tool_counts = (
            pd.Series([t for p in PROJECTS for t in p["tools"]])
            .value_counts()
            .rename_axis("Tool")
            .to_frame("Projects")
        )
        st.caption("How often each tool appears in my projects")
        st.bar_chart(tool_counts, color="#6f42c1")


with tab_contact:
    st.header("Get in touch")
    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name *")
            email = st.text_input("Your email")
            topic = st.selectbox(
                "What's this about?",
                ["Feedback on this site", "Project collaboration", "Just saying hi", "Other"],
            )
            rating = st.select_slider(
                "How would you rate this portfolio?",
                options=["😐", "🙂", "😊", "😄", "🤩"],
                value="😊",
            )
            message = st.text_area("Message *", height=130)
            subscribe = st.checkbox("I'd like a reply")
            submitted = st.form_submit_button("Send message", type="primary")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please fill in your name and a message.")
            else:
                st.session_state.messages.append(
                    {
                        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Name": name.strip(),
                        "Email": email.strip(),
                        "Topic": topic,
                        "Rating": rating,
                        "Message": message.strip(),
                        "Wants reply": subscribe,
                    }
                )
                st.success(
                    f"Thank you, {name.strip()}! Your message about "
                    f"“{topic.lower()}” was received. Rating: {rating}"
                    + (" — I'll get back to you soon." if subscribe else "")
                )
                st.balloons()

    with info_col:
        with st.container(border=True):
            st.subheader("Contact details")
            st.write(f"✉️ {EMAIL}")
            st.write(f"🐙 [{GITHUB.split('/')[-1]}]({GITHUB})")
            st.write(f"📍 {LOCATION}")

        st.subheader("Messages this session")
        if st.session_state.messages:
            log = pd.DataFrame(st.session_state.messages)
            st.dataframe(log[["Time", "Name", "Topic", "Rating"]],
                         hide_index=True, width="stretch")
            st.download_button(
                "⬇️ Download messages (CSV)",
                data=log.to_csv(index=False).encode("utf-8"),
                file_name="messages.csv",
                mime="text/csv",
            )
            if st.button("Clear messages"):
                st.session_state.messages = []
                st.rerun()
        else:
            st.caption("No messages yet — be the first!")


st.divider()
st.markdown(
    f'<div class="footer">{NAME} · Section {SECTION} · {PROGRAM}, {YEAR_LEVEL}<br>'
    f"Built with Streamlit · {date.today().year}</div>",
    unsafe_allow_html=True,
)
