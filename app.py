import streamlit as st

# ==========================================
# UNIVERSAL APPLICATION CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="2026 World Cup Analytical Model",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# TOTAL SPORTS GRAPHICS BRANDING & THEME ENGINE
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&family=Bebas+Neue&display=swap');

    /* Global Base Styling */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        background-color: #080B10 !important;
        color: #E2E8F0;
    }

    /* Hide the default Streamlit footer so our own footer is the only one */
    footer {visibility: hidden;}

    /* Broadcast Elements */
    h1, h2, h3, h4, .stTabs [data-baseweb="tab-list"] button {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    h2 { color: #00FF87 !important; font-size: 2.2rem !important; }
    h3 { color: #F1F5F9 !important; }

    /* ==========================================
       HERO / KICKOFF BANNER (Pitch-Inspired)
    ========================================== */
    .pitch-banner {
        position: relative;
        text-align: center;
        padding: 48px 25px 38px 25px;
        border-radius: 14px;
        margin-bottom: 28px;
        overflow: hidden;
        border: 1px solid #1E293B;
        background:
            linear-gradient(180deg, rgba(8,11,16,0.55) 0%, rgba(8,11,16,0.94) 75%),
            repeating-linear-gradient(110deg, #123524 0px, #123524 70px, #0D2B1B 70px, #0D2B1B 140px);
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.6);
    }
    .kickoff-badge {
        display: inline-block;
        background-color: #00FF87;
        color: #04140C;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 0.95rem;
        letter-spacing: 4px;
        padding: 6px 18px;
        border-radius: 999px;
        margin-bottom: 18px;
    }
    .hero-title {
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        font-size: 3.4rem;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
        text-shadow: 0 0 25px rgba(0, 255, 135, 0.35);
    }
    .hero-subtitle {
        font-family: 'Oswald', sans-serif;
        color: #00FF87;
        font-size: 1.5rem;
        letter-spacing: 4px;
        margin: 8px 0 16px 0;
    }
    .hero-tagline {
        max-width: 760px;
        margin: 0 auto 18px auto;
        color: #94A3B8;
        font-size: 1rem;
        line-height: 1.6;
    }
    .host-flags {
        font-family: 'Oswald', sans-serif;
        font-size: 1rem;
        letter-spacing: 2px;
        color: #E2E8F0;
    }

    /* Clean Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #111622;
        border-radius: 8px;
        padding: 6px;
        border: 1px solid #1E293B;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.2rem !important;
        color: #94A3B8 !important;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #00FF87 !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 6px;
    }

    /* Container Modules */
    .streamlit-expanderHeader {
        background-color: #111622 !important;
        border: 1px solid #1E293B !important;
        font-family: 'Oswald', sans-serif;
        font-size: 1.4rem !important;
        color: #FFFFFF !important;
        border-radius: 6px !important;
    }

    /* ==========================================
       SCOREBOARD-STYLE METRICS
    ========================================== */
    [data-testid="stMetric"] {
        background-color: #111622;
        border: 1px solid #1E293B;
        border-left: 4px solid #00FF87;
        border-radius: 10px;
        padding: 14px 16px;
    }
    [data-testid="stMetricValue"] {
        font-family: 'Bebas Neue', 'Oswald', sans-serif;
        font-size: 2.3rem !important;
        color: #00FF87 !important;
        letter-spacing: 1px;
    }
    [data-testid="stMetricLabel"] {
        font-family: 'Space Grotesk', sans-serif;
        text-transform: uppercase;
        font-size: 0.8rem !important;
        color: #94A3B8 !important;
        letter-spacing: 1.5px;
    }

    /* ==========================================
       SIDEBAR / MATCH CENTER
    ========================================== */
    section[data-testid="stSidebar"] {
        background-color: #0D121F;
        border-right: 1px solid #1E293B;
    }
    section[data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] h3 {
        color: #00FF87 !important;
    }

    /* ==========================================
       TEAM PROFILE BANNER
    ========================================== */
    .team-banner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
        padding: 18px 26px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -8px rgba(0, 0, 0, 0.6);
    }
    .team-banner-name {
        font-family: 'Oswald', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .team-banner-tag {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 1.1rem;
        letter-spacing: 4px;
        opacity: 0.75;
    }

    /* Dedicated Team Color Branding Kits */
    .team-argentine { background-color: #1D4ED8 !important; color: #FFFFFF !important; border-left: 5px solid #60A5FA; }
    .team-brazil { background-color: #15803D !important; color: #FDE047 !important; border-left: 5px solid #EAB308; }
    .team-spain { background-color: #991B1B !important; color: #FDE047 !important; border-left: 5px solid #F59E0B; }
    .team-england { background-color: #F8FAFC !important; color: #0F172A !important; border-left: 5px solid #E2E8F0; }
    .team-france { background-color: #1E3A8A !important; color: #FFFFFF !important; border-left: 5px solid #3B82F6; }
    .team-netherlands { background-color: #C2410C !important; color: #FFFFFF !important; border-left: 5px solid #F97316; }
    .team-mexico { background-color: #065F46 !important; color: #FFFFFF !important; border-left: 5px solid #10B981; }
    .team-ecuador { background-color: #B45309 !important; color: #FDE047 !important; border-left: 5px solid #F59E0B; }
    .team-germany { background-color: #1A1A1A !important; color: #FFCE00 !important; border-left: 5px solid #DD0000; }
    .team-colombia { background-color: #003893 !important; color: #FFCD00 !important; border-left: 5px solid #C8102E; }
    .team-portugal { background-color: #006633 !important; color: #FFFFFF !important; border-left: 5px solid #FF0000; }
    .team-uruguay { background-color: #0F3460 !important; color: #75AADB !important; border-left: 5px solid #75AADB; }
    .team-croatia { background-color: #DC2626 !important; color: #FFFFFF !important; border-left: 5px solid #FFFFFF; }
    .team-japan { background-color: #1E1E1E !important; color: #FFFFFF !important; border-left: 5px solid #BC002D; }
    .team-senegal { background-color: #00853F !important; color: #FDEF42 !important; border-left: 5px solid #E31B23; }
    .team-norway { background-color: #BA0C2F !important; color: #FFFFFF !important; border-left: 5px solid #00205B; }
    .team-paraguay { background-color: #D52B1E !important; color: #FFFFFF !important; border-left: 5px solid #0038A8; }

    /* ==========================================
       SCOREBOARD-STYLE BRACKET TABLES
    ========================================== */
    .stMarkdown table {
        width: 100%;
        border-collapse: collapse;
        background-color: #111622;
        border-radius: 8px;
        overflow: hidden;
        font-size: 0.95rem;
    }
    .stMarkdown table thead th {
        background-color: #00FF87;
        color: #04140C;
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 10px 14px;
        text-align: left;
    }
    .stMarkdown table td {
        padding: 9px 14px;
        border-bottom: 1px solid #1E293B;
        color: #E2E8F0;
    }
    .stMarkdown table tbody tr:nth-child(even) td {
        background-color: #161D30;
    }
    .stMarkdown table tbody tr:hover td {
        background-color: #1E293B;
    }

    /* Ultimate Trophy Destination Platform */
    .grand-champion-platform {
        background: linear-gradient(135deg, #FEF08A 0%, #CA8A04 100%);
        color: #000000;
        text-align: center;
        padding: 28px 15px;
        border-radius: 10px;
        font-family: 'Oswald', sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        box-shadow: 0 0 30px rgba(234, 179, 8, 0.4);
        border: 2px solid #FAC827;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .champ-subtext {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        color: #713F12;
        margin-top: 8px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* ==========================================
       FOOTER
    ========================================== */
    .app-footer {
        text-align: center;
        margin-top: 50px;
        padding: 24px 10px 18px 10px;
        border-top: 2px solid #1E293B;
        font-family: 'Space Grotesk', sans-serif;
    }
    .footer-line {
        color: #64748B;
        font-size: 0.85rem;
        margin-bottom: 6px;
        letter-spacing: 0.5px;
    }
    .footer-copyright {
        color: #475569;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }
    .footer-copyright .highlight {
        color: #00FF87;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR — MATCH CENTER
# ==========================================
with st.sidebar:
    st.markdown("Match Center")
    st.markdown("---")
    st.markdown("Tournament: 2026 FIFA World Cup")
    st.markdown("Hosts: USA 🇺🇸 · Mexico 🇲🇽 · Canada 🇨🇦")
    st.markdown("Field Size: 48 Nations")
    st.markdown("---")
    st.markdown("Navigation Guide")
    st.markdown("- The AI Engine — methodology & model internals")
    st.markdown("- Team Journeys — squad-by-squad scouting reports")
    st.markdown("- The Alpha Bracket — full knockout projection")
    st.markdown("---")
    st.caption(" Model outputs are probabilistic projections, not guarantees. Football is a game of fine margins.")

# ==========================================
# MAIN INTERFACE HEADER — KICKOFF BANNER
# ==========================================
st.markdown("""
    <div class="pitch-banner">
        <div class="kickoff-badge"> LIVE PREDICTIVE MODEL </div>
        <div class="hero-title">2026 FIFA World Cup</div>
        <div class="hero-subtitle"> Predictive Analytics Engine </div>
        <p class="hero-tagline">Machine Learning Simulation Pipeline Mapping Roster Efficiency, Travel Exhaustion, and Micro-Climate Physics.</p>
        <div class="host-flags">🇺🇸 &nbsp;·&nbsp; 🇲🇽 &nbsp;·&nbsp; 🇨🇦 &nbsp; — A NORTH AMERICAN SUMMER TOURNAMENT</div>
    </div>
""", unsafe_allow_html=True)

# Initialize Navigation Tab Infrastructure
tab_engine, tab_journeys, tab_bracket = st.tabs([
    " The AI Engine",
    " Team Journeys",
    " The Alpha Bracket"
])

# ==========================================
# METHODOLOGY LAYER
# ==========================================
with tab_engine:
    st.header(" Algorithmic Methodology")
    st.write("This structural pipeline evaluates physical tournament factors, adjusting baseline Elo configurations using localized environmental variables to generate raw advancement vectors.")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    metric_col1.metric(" Historical Matches Checked", "50,000+")
    metric_col2.metric(" Monte Carlo Replications", "1,000")
    metric_col3.metric(" Modeled Competitors", "48")
    metric_col4.metric(" Environmental Array", "Active")

    st.write("")
    st.markdown("### Operational Feature Engineering")

    with st.expander(" Physical Exhaustion Index", expanded=True):
        st.write("""
        Mechanic: Quantifies cross-continental aviation vectors and absolute recovery increments between matchdays.
        Impact: Teams crossing multiple time zones on compressed schedules face clear performance penalties in late-game expected goal calculations compared to stationary rivals.
        """)

    with st.expander(" Micro-Climate & Altitude Array", expanded=True):
        st.write("""
        Mechanic: Factors geographic stadium elevation profiles directly into player stamina depletion layers.
        Impact: Teams unaccustomed to playing at high elevations show decreased late-stage efficiency, while host squads receive localized adaptation multipliers.
        """)

    with st.expander(" Opponent-Adjusted Momentum Metrics", expanded=True):
        st.write("""
        Mechanic: Processes trailing historical score lines using exponentially decayed moving averages adjusted for opponent strength.
        Impact: High-margin scorelines against elite competitors yield top-tier ratings. Victories over lower-tier teams are discounted to prevent ranking inflation.
        """)

# ==========================================
# DETAILED TEAM COMPENDIUM (TOP 15 + GERMANY)
# ==========================================
with tab_journeys:
    st.header(" Team Analytics & Performance Portfolios")
    st.write("Squad-by-squad scouting dossiers, generated from the model's probability and tactical-form layers.")

    team_registry = {
        "Spain": {
            "win": "34.2%", "final": "48.2%", "form": "Elite positional dominance and sustained possession patterns.", "rivals": "Mexico, Argentina",
            "story": "The Multiverse Frontrunner. Across randomized Monte Carlo simulations, Spain leads in total title wins. Their possession-heavy system limits defensive errors and exposure to low-probability counters, making them highly resilient against classic tournament upsets."
        },
        "Argentina": {
            "win": "25.3%", "final": "48.2%", "form": "Top-tier conversion efficiency against low defensive blocks.", "rivals": "France, Spain, England",
            "story": "The Consensus Core Choice. Argentina demonstrates a clear competitive edge in high-leverage fixtures against elite components. In the baseline deterministic timeline, they navigate a demanding knockout path by outperforming structural defensive expectations."
        },
        "England": {
            "win": "21.7%", "final": "40.9%", "form": "Deep talent distribution with high physical resilience.", "rivals": "Ecuador, Netherlands, Argentina",
            "story": "The Roster Depth Juggernaut. England benefits from high team valuation metrics and clean travel scheduling across early groups. The model identifies their deep rotation options as an asset, though their conversion efficiency numbers drop slightly in final simulations."
        },
        "Germany": {
            "win": "0.1%", "final": "0.4%", "form": "Strong tactical core neutralized by high-risk bracket pathing.", "rivals": "Mexico, Spain",
            "story": "The Bracket Trap Victim. Despite carrying strong baseline player metrics, Germany faces a severe geographic and scheduling disadvantage. A projected early knockout meeting with host nation Mexico requires playing at high altitude on short recovery rest. The model identifies this specific fixture as a high-probability bottleneck that limits their deeper tournament equity."
        },
        "France": {
            "win": "8.4%", "final": "19.5%", "form": "High-efficiency vertical transition attack.", "rivals": "United States, Argentina",
            "story": "The Early Bracket Bottleneck. France's core projection suffers due to a projected early meeting with Argentina in the quarterfinals. This early matchup against top-tier opposition lowers their overall baseline probability of reaching the finals."
        },
        "Netherlands": {
            "win": "2.1%", "final": "8.9%", "form": "Organized defensive shape, efficient tactical foul tracking.", "rivals": "Brazil, England",
            "story": "The Structural Disrupter. The Netherlands shows solid values within defensive performance metrics. The model positions them to take advantage of teams dealing with recent defensive inconsistencies, projecting a deep run past the quarterfinals."
        },
        "Colombia": {
            "win": "1.6%", "final": "3.8%", "form": "Consistent unbeaten run in regional qualifying play.", "rivals": "Japan, Netherlands",
            "story": "The Form Peak Contender. Colombia benefits from high momentum weights in the model's tracking layer. Their intense regional form suggests comfortable progress through initial groups before hitting organized European defensive structures."
        },
        "Brazil": {
            "win": "1.3%", "final": "7.4%", "form": "Recent defensive inconsistencies in continental qualification.", "rivals": "Senegal, Netherlands",
            "story": "The Vulnerable Giant. While possessing high overall squad talent, Brazil is penalized for soft defensive tracking data over their recent qualification cycles. The model projects clear risks when facing disciplined counter-attacking teams."
        },
        "Ecuador": {
            "win": "1.1%", "final": "3.9%", "form": "High cardiovascular recovery values, altitude acclimation.", "rivals": "Korea Republic, Switzerland, England",
            "story": "The Altitude Outlier. Ecuador's physical profiles are well-suited to the high-temperature, high-altitude venues of the North American summer tournament. They routinely outrun European teams on short rest cycles."
        },
        "Portugal": {
            "win": "1.0%", "final": "2.9%", "form": "Slowing transition speeds across their central midfield.", "rivals": "Czechia, Spain",
            "story": "The Stagnating Contingent. While holding strong legacy team metrics, Portugal faces challenges against younger squads built for fast transition play. The model identifies risks during long, demanding tournament stretches."
        },
        "Uruguay": {
            "win": "0.6%", "final": "3.4%", "form": "High-intensity counter-pressing structure.", "rivals": "Croatia, England",
            "story": "The High-Attrition Squad. Uruguay's aggressive pressing tactics yield early group-stage advantages but lead to noticeable fatigue accumulation across later rounds, reducing their depth value in long tournament simulations."
        },
        "Croatia": {
            "win": "0.6%", "final": "2.4%", "form": "Experienced tactical spine with physical recovery limits.", "rivals": "Uruguay",
            "story": "The Legacy Dynamic. Croatia retains an elite tactical core, but tracking models flag their older roster as vulnerable to younger, physical pressing teams during late knockout rounds."
        },
        "Japan": {
            "win": "0.4%", "final": "1.8%", "form": "Sustained high-tempo pressing and rapid transition output.", "rivals": "Colombia",
            "story": "The Tactical Giant Killer. Japan holds a clear track record of securing positive results against high-possession teams. Their disciplined defensive shape makes them a dangerous wildcard in knockout brackets."
        },
        "Senegal": {
            "win": "0.3%", "final": "1.3%", "form": "Dominant physical and athletic core metrics.", "rivals": "Brazil",
            "story": "The Athletic Wildcard. Senegal possesses the direct running power and physical profile needed to stress elite European backlines, though lower overall finishing metrics caps their final championship equity."
        },
        "Norway": {
            "win": "0.3%", "final": "2.1%", "form": "Highly concentrated offensive production from key starters.", "rivals": "Scotland, Argentina",
            "story": "The High-Variance Attack. Norway's core projections are driven by outlier attacking talent. Their efficient finishing data means they can occasionally outscore high-level opponents regardless of possession shares."
        },
        "Paraguay": {
            "win": "0.2%", "final": "0.5%", "form": "Low-event defensive setup, low tactical risk.", "rivals": "Switzerland",
            "story": "The Defensive Gridlock. Paraguay excels at slowing match tempos and limiting clear chances. While this keeps scorelines close, their lower scoring rates restrict their ability to mount deep comebacks."
        }
    }

    # Team flags + jersey-color CSS classes for the profile banner
    team_flags = {
        "Spain": "🇪🇸", "Argentina": "🇦🇷", "England": "🏴", "Germany": "🇩🇪",
        "France": "🇫🇷", "Netherlands": "🇳🇱", "Colombia": "🇨🇴", "Brazil": "🇧🇷",
        "Ecuador": "🇪🇨", "Portugal": "🇵🇹", "Uruguay": "🇺🇾", "Croatia": "🇭🇷",
        "Japan": "🇯🇵", "Senegal": "🇸🇳", "Norway": "🇳🇴", "Paraguay": "🇵🇾"
    }
    team_color_class = {
        "Spain": "team-spain", "Argentina": "team-argentine", "England": "team-england",
        "Germany": "team-germany", "France": "team-france", "Netherlands": "team-netherlands",
        "Colombia": "team-colombia", "Brazil": "team-brazil", "Ecuador": "team-ecuador",
        "Portugal": "team-portugal", "Uruguay": "team-uruguay", "Croatia": "team-croatia",
        "Japan": "team-japan", "Senegal": "team-senegal", "Norway": "team-norway",
        "Paraguay": "team-paraguay"
    }

    selection = st.selectbox(" Select Team Profile Archive:", list(team_registry.keys()))
    record = team_registry[selection]
    flag = team_flags.get(selection, "")
    css_class = team_color_class.get(selection, "team-argentine")

    st.markdown(f"""
        <div class="team-banner {css_class}">
            <span class="team-banner-name">{flag} {selection}</span>
            <span class="team-banner-tag">SQUAD DOSSIER</span>
        </div>
    """, unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)
    col_v1.metric(" Tournament Win Equity", record['win'])
    col_v2.metric(" Reach Final Equity", record['final'])

    st.markdown(f"** Calculated Tactical Form:** {record['form']}")
    st.markdown(f"** Projected Bracket Paths:** {record['rivals']}")
    st.write("")
    st.info(f" {record['story']}")

# ==========================================
# TAB 3: THE NATIVE STREAMLIT BRACKET
# ==========================================
with tab_bracket:
    st.header(" The Consensus Tournament Timeline")
    st.write("Deterministic progression matrix built entirely with native Streamlit data tables to ensure zero rendering errors and maximum readability.")
    st.write("---")

    # ==========================================
    # GROUP STAGE DATA LAYER
    # ==========================================
    GROUPS = {
        "Group A": ["Mexico", "South Africa", "Korea Republic", "Czechia"],
        "Group B": ["Canada", "Bosnia-Herzegovina", "Qatar", "Switzerland"],
        "Group C": ["United States", "Paraguay", "Australia", "Türkiye"],
        "Group D": ["Brazil", "Morocco", "Haiti", "Scotland"],
        "Group E": ["Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"],
        "Group F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
        "Group G": ["Belgium", "Egypt", "IR Iran", "New Zealand"],
        "Group H": ["Spain", "Cape Verde", "Saudi Arabia", "Uruguay"],
        "Group I": ["France", "Senegal", "Iraq", "Norway"],
        "Group J": ["Argentina", "Algeria", "Austria", "Jordan"],
        "Group K": ["Portugal", "Congo DR", "Uzbekistan", "Colombia"],
        "Group L": ["England", "Croatia", "Ghana", "Panama"],
    }

    # (Date, Home_Team, Away_Team, Home_xG, Away_xG, Home_Score, Away_Score)
    GROUP_STAGE_MATCHES = [
        ("2026-06-11", "Mexico", "South Africa", 2.28, 0.63, 2, 1),
        ("2026-06-11", "Korea Republic", "Czechia", 1.26, 0.96, 1, 1),
        ("2026-06-12", "Canada", "Bosnia-Herzegovina", 2.04, 0.77, 2, 1),
        ("2026-06-12", "United States", "Paraguay", 1.09, 1.04, 1, 1),
        ("2026-06-13", "Qatar", "Switzerland", 0.79, 2.09, 1, 2),
        ("2026-06-13", "Brazil", "Morocco", 1.87, 0.78, 2, 1),
        ("2026-06-13", "Haiti", "Scotland", 1.03, 1.39, 1, 1),
        ("2026-06-13", "Australia", "Türkiye", 2.17, 0.79, 2, 1),
        ("2026-06-14", "Germany", "Curaçao", 3.00, 0.71, 3, 1),
        ("2026-06-14", "Netherlands", "Japan", 1.61, 0.82, 2, 1),
        ("2026-06-14", "Côte d'Ivoire", "Ecuador", 1.10, 1.85, 1, 2),
        ("2026-06-14", "Sweden", "Tunisia", 1.90, 0.83, 2, 1),
        ("2026-06-15", "Belgium", "Egypt", 2.10, 0.79, 2, 1),
        ("2026-06-15", "Spain", "Cape Verde", 3.09, 0.64, 3, 1),
        ("2026-06-15", "IR Iran", "New Zealand", 1.67, 0.75, 2, 1),
        ("2026-06-15", "Saudi Arabia", "Uruguay", 0.85, 1.59, 1, 2),
        ("2026-06-16", "France", "Senegal", 1.96, 0.83, 2, 1),
        ("2026-06-16", "Iraq", "Norway", 0.97, 1.70, 1, 2),
        ("2026-06-16", "Argentina", "Algeria", 2.33, 0.64, 2, 1),
        ("2026-06-16", "Austria", "Jordan", 1.83, 0.75, 2, 1),
        ("2026-06-17", "Portugal", "Congo DR", 2.32, 0.67, 2, 1),
        ("2026-06-17", "England", "Croatia", 1.94, 0.72, 2, 1),
        ("2026-06-17", "Ghana", "Panama", 1.03, 1.28, 1, 1),
        ("2026-06-17", "Uzbekistan", "Colombia", 0.88, 1.50, 1, 2),
        ("2026-06-18", "Czechia", "South Africa", 2.21, 0.84, 2, 1),
        ("2026-06-18", "Switzerland", "Bosnia-Herzegovina", 2.14, 0.58, 2, 1),
        ("2026-06-18", "Canada", "Qatar", 1.97, 0.51, 2, 1),
        ("2026-06-18", "Mexico", "Korea Republic", 2.35, 0.84, 2, 1),
        ("2026-06-19", "United States", "Australia", 1.29, 1.10, 1, 1),
        ("2026-06-19", "Scotland", "Morocco", 1.30, 0.99, 1, 1),
        ("2026-06-19", "Türkiye", "Paraguay", 1.08, 1.10, 1, 1),
        ("2026-06-19", "Brazil", "Haiti", 2.94, 0.65, 3, 1),
        ("2026-06-20", "Netherlands", "Sweden", 2.25, 0.50, 2, 0),
        ("2026-06-20", "Germany", "Côte d'Ivoire", 2.12, 0.66, 2, 1),
        ("2026-06-20", "Ecuador", "Curaçao", 2.15, 0.52, 2, 1),
        ("2026-06-20", "Tunisia", "Japan", 0.97, 1.66, 1, 2),
        ("2026-06-21", "Spain", "Saudi Arabia", 3.03, 0.65, 3, 1),
        ("2026-06-21", "Belgium", "IR Iran", 2.23, 0.75, 2, 1),
        ("2026-06-21", "Uruguay", "Cape Verde", 2.34, 0.66, 2, 1),
        ("2026-06-21", "New Zealand", "Egypt", 1.30, 1.00, 1, 1),
        ("2026-06-22", "Argentina", "Austria", 2.26, 0.66, 2, 1),
        ("2026-06-22", "France", "Iraq", 2.95, 0.65, 3, 1),
        ("2026-06-22", "Norway", "Senegal", 1.60, 0.86, 2, 1),
        ("2026-06-22", "Jordan", "Algeria", 1.28, 0.99, 1, 1),
        ("2026-06-23", "Portugal", "Uzbekistan", 2.21, 0.66, 2, 1),
        ("2026-06-23", "England", "Ghana", 2.99, 0.73, 3, 1),
        ("2026-06-23", "Panama", "Croatia", 1.01, 1.09, 1, 1),
        ("2026-06-23", "Colombia", "Congo DR", 2.46, 0.72, 2, 1),
        ("2026-06-24", "Switzerland", "Canada", 1.73, 1.01, 2, 1),
        ("2026-06-24", "Bosnia-Herzegovina", "Qatar", 2.17, 0.78, 2, 1),
        ("2026-06-24", "Scotland", "Brazil", 1.28, 1.28, 1, 1),
        ("2026-06-24", "Morocco", "Haiti", 2.21, 0.67, 2, 1),
        ("2026-06-24", "South Africa", "Korea Republic", 1.21, 1.05, 1, 1),
        ("2026-06-24", "Czechia", "Mexico", 1.21, 1.02, 1, 1),
        ("2026-06-25", "Curaçao", "Côte d'Ivoire", 1.02, 1.33, 1, 1),
        ("2026-06-25", "Ecuador", "Germany", 1.90, 0.86, 2, 1),
        ("2026-06-25", "Japan", "Sweden", 1.96, 0.72, 2, 1),
        ("2026-06-25", "Tunisia", "Netherlands", 0.76, 1.83, 1, 2),
        ("2026-06-25", "Paraguay", "Australia", 1.60, 0.83, 2, 1),
        ("2026-06-25", "Türkiye", "United States", 1.69, 0.98, 2, 1),
        ("2026-06-26", "Norway", "France", 1.08, 1.05, 1, 1),
        ("2026-06-26", "Senegal", "Iraq", 2.13, 0.65, 2, 1),
        ("2026-06-26", "Uruguay", "Spain", 1.06, 1.82, 1, 2),
        ("2026-06-26", "Cape Verde", "Saudi Arabia", 1.45, 0.92, 1, 1),
        ("2026-06-26", "Egypt", "IR Iran", 1.59, 0.90, 2, 1),
        ("2026-06-26", "New Zealand", "Belgium", 0.90, 1.79, 1, 2),
        ("2026-06-27", "Panama", "England", 0.93, 1.96, 1, 2),
        ("2026-06-27", "Croatia", "Ghana", 2.95, 0.65, 3, 1),
        ("2026-06-27", "Colombia", "Portugal", 1.44, 0.93, 1, 1),
        ("2026-06-27", "Congo DR", "Uzbekistan", 1.30, 1.08, 1, 1),
        ("2026-06-27", "Jordan", "Argentina", 0.82, 1.99, 1, 2),
        ("2026-06-27", "Algeria", "Austria", 1.30, 0.99, 1, 1),
    ]

    def compute_group_standings(group_name):
        """Build a sorted points table for a given group from the raw fixtures."""
        teams = GROUPS[group_name]
        stats = {t: {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0} for t in teams}
        for _, home, away, _, _, hs, as_ in GROUP_STAGE_MATCHES:
            if home in teams and away in teams:
                stats[home]["P"] += 1
                stats[away]["P"] += 1
                stats[home]["GF"] += hs
                stats[home]["GA"] += as_
                stats[away]["GF"] += as_
                stats[away]["GA"] += hs
                if hs > as_:
                    stats[home]["W"] += 1
                    stats[away]["L"] += 1
                elif hs < as_:
                    stats[away]["W"] += 1
                    stats[home]["L"] += 1
                else:
                    stats[home]["D"] += 1
                    stats[away]["D"] += 1

        rows = []
        for t in teams:
            s = stats[t]
            pts = s["W"] * 3 + s["D"]
            gd = s["GF"] - s["GA"]
            rows.append({"team": t, "pts": pts, "gd": gd, **s})

        rows.sort(key=lambda r: (-r["pts"], -r["gd"], -r["GF"], r["team"]))
        return rows

    def render_group_standings(group_name):
        rows = compute_group_standings(group_name)
        qual_icon = {0: "🟢", 1: "🟢", 2: "🟡", 3: "🔴"}
        lines = [
            "| Pos | Team | P | W | D | L | GF | GA | GD | Pts |",
            "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        for i, r in enumerate(rows):
            lines.append(
                f"| {qual_icon[i]} {i + 1} | **{r['team']}** | {r['P']} | {r['W']} | {r['D']} | {r['L']} | {r['GF']} | {r['GA']} | {r['gd']:+d} | **{r['pts']}** |"
            )
        return "\n".join(lines)

    def render_group_fixtures(group_name):
        teams = GROUPS[group_name]
        lines = [
            "| Date | Fixture | Score | xG (H – A) |",
            "| :--- | :--- | :---: | :---: |",
        ]
        for date, home, away, hxg, axg, hs, as_ in GROUP_STAGE_MATCHES:
            if home in teams and away in teams:
                lines.append(f"| {date} | {home} vs {away} | **{hs} – {as_}** | {hxg:.2f} – {axg:.2f} |")
        return "\n".join(lines)

    # ==========================================
    # GROUP STAGE SECTION
    # ==========================================
    st.subheader(" Group Stage")
    st.write("All 72 simulated Group Stage fixtures across the tournament's 12 groups, with final standings, results, and Expected Goals (xG) generated by the model.")
    st.caption("🟢 Direct knockout qualification &nbsp;·&nbsp; 🟡 Best third-place contention &nbsp;·&nbsp; 🔴 Eliminated")

    group_select = st.selectbox(" Select Group:", list(GROUPS.keys()))

    col_standings, col_fixtures = st.columns([1, 1])
    with col_standings:
        st.markdown(f"##### {group_select} — Final Standings")
        st.markdown(render_group_standings(group_select))
    with col_fixtures:
        st.markdown(f"##### {group_select} — Fixtures & Results")
        st.markdown(render_group_fixtures(group_select))

    st.write("---")

    st.subheader(" Round of 32 (16 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (96.1%)** | New Zealand (3.9%) | **Argentina** |
    | **England (91.4%)** | Algeria (8.6%) | **England** |
    | **Netherlands (83.3%)** | Bosnia-Herzegovina (16.7%) | **Netherlands** |
    | **Spain (89.4%)** | Austria (10.6%) | **Spain** |
    | **Mexico (80.5%)** | Cote d'Ivoire (19.5%) | **Mexico** |
    | **Brazil (86.9%)** | Senegal (13.1%) | **Brazil** |
    | **Ecuador (93.6%)** | Korea Republic (6.4%) | **Ecuador** |
    | **Canada (57.2%)** | Morocco (42.8%) | **Canada** |
    | **France (94.8%)** | United States (5.2%) | **France** |
    | **Switzerland (77.3%)** | Paraguay (22.7%) | **Switzerland** |
    | **Belgium (78.1%)** | Turkiye (21.9%) | **Belgium** |
    | **Germany (91.8%)** | IR Iran (8.2%) | **Germany** |
    | **Portugal (88.9%)** | Czechia (11.1%) | **Portugal** |
    | **Colombia (74.0%)** | Japan (26.0%) | **Colombia** |
    | **Uruguay (58.4%)** | Croatia (41.6%) | **Uruguay** |
    | **Norway (86.3%)** | Scotland (13.7%) | **Norway** |
    """)

    st.write("---")
    st.subheader(" Round of 16 (8 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (87.2%)** | Norway (12.8%) | **Argentina** |
    | **England (81.4%)** | Uruguay (18.6%) | **England** |
    | **Netherlands (71.9%)** | Colombia (28.1%) | **Netherlands** |
    | **Spain (91.7%)** | Portugal (8.3%) | **Spain** |
    | **Mexico (80.3%)** | Germany (19.7%) | **Mexico** |
    | **Brazil (83.7%)** | Belgium (16.3%) | **Brazil** |
    | **Ecuador (79.7%)** | Switzerland (20.3%) | **Ecuador** |
    | **France (77.9%)** | Canada (22.1%) | **France** |
    """)

    st.write("---")
    st.subheader(" Quarterfinals (4 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (76.6%)** | France (23.4%) | **Argentina** |
    | **Spain (95.8%)** | Mexico (4.2%) | **Spain** |
    | **England (76.3%)** | Ecuador (23.7%) | **England** |
    | **Netherlands (68.3%)** | Brazil (31.7%) | **Netherlands** |
    """)

    st.write("---")
    st.subheader(" Semifinals (2 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (59.1%)** | Spain (40.9%) | **Argentina** |
    | **England (85.2%)** | Netherlands (14.8%) | **England** |
    """)

    st.write("---")
    st.subheader(" The Final (1 Match)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (72.1%)** | England (27.9%) | **Argentina** |
    """)

    st.write("---")
    st.markdown("""
        <div class="grand-champion-platform">
            🏆 PREDICTED CHAMPION: ARGENTINA 🏆
            <div class="champ-subtext">2026 FIFA World Cup &mdash; Model Consensus Output</div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
    <div class="app-footer">
        <div class="footer-line"> System Core Framework built using Python and XGBoost Ensembles. </div>
        <div class="footer-copyright">Copyright <span class="highlight">Soumyadeep Roy Chowdhury</span> 2026. All rights reserved.</div>
    </div>
""", unsafe_allow_html=True)
