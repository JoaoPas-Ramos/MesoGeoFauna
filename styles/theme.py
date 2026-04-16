PRIMARY_BLUE = "#0a192f"
SIDEBAR_BG = "#112240"
CARD_BG = "#172a45"
CARD_DARK = "rgba(10, 25, 47, 0.92)"
SECONDARY_TURQUOISE = "#00f2ff"
TEXT_WHITE = "#e6f1ff"
MUTED_TEXT = "rgba(230, 241, 255, 0.75)"
BORDER_COLOR = "rgba(0, 242, 255, 0.16)"


def carregar_css():
    return f"""
    <style>
    .stApp {{
        background-color: {PRIMARY_BLUE};
        color: {TEXT_WHITE};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {SIDEBAR_BG};
        border-right: 1px solid {BORDER_COLOR};
    }}

    section[data-testid="stSidebar"] .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    .main .block-container {{
        max-width: 100%;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT_WHITE};
    }}

    .app-title {{
        font-size: 2.15rem;
        font-weight: 700;
        color: {TEXT_WHITE};
        margin-bottom: 0.25rem;
        line-height: 1.1;
    }}

    .app-subtitle {{
        color: {SECONDARY_TURQUOISE};
        font-size: 1rem;
        margin-bottom: 1.4rem;
    }}

    .sidebar-brand {{
        margin-bottom: 0.6rem;
    }}

    .sidebar-brand h1 {{
        font-size: 1.9rem;
        margin: 0;
        line-height: 1.1;
    }}

    .sidebar-brand span {{
        color: {SECONDARY_TURQUOISE};
    }}

    .sidebar-text {{
        color: {MUTED_TEXT};
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }}

    .sidebar-section-title {{
        color: {SECONDARY_TURQUOISE};
        font-size: 0.95rem;
        font-weight: 600;
        margin-top: 0.8rem;
        margin-bottom: 0.6rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }}

    .info-card {{
        background: {CARD_DARK};
        border: 1px solid {SECONDARY_TURQUOISE};
        border-radius: 12px;
        overflow: hidden;
        margin-top: 1rem;
    }}

    .info-card-header {{
        background: linear-gradient(90deg, rgba(0,242,255,0.15), rgba(0,242,255,0.04));
        padding: 0.8rem 1rem;
        border-bottom: 1px solid rgba(0,242,255,0.18);
    }}

    .info-card-header h3 {{
        margin: 0;
        font-size: 1rem;
        color: {SECONDARY_TURQUOISE};
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}

    .info-card-body {{
        padding: 1rem;
    }}

    .info-card-body p {{
        margin: 0.35rem 0;
        font-size: 0.93rem;
        color: {TEXT_WHITE};
    }}

    .info-card-body strong {{
        color: {SECONDARY_TURQUOISE};
    }}

    .map-panel {{
        background-color: {CARD_BG};
        border: 1px solid {BORDER_COLOR};
        border-radius: 18px;
        padding: 1rem;
        margin-top: 0.4rem;
        margin-bottom: 1rem;
    }}

    .map-title {{
        color: {TEXT_WHITE};
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }}

    .map-subtitle {{
        color: {MUTED_TEXT};
        font-size: 0.92rem;
        margin-bottom: 0.9rem;
    }}

    .panel {{
        background-color: {CARD_BG};
        border: 1px solid {BORDER_COLOR};
        border-radius: 16px;
        padding: 1.1rem 1.2rem;
        margin-bottom: 1rem;
    }}

    .panel-title {{
        color: {SECONDARY_TURQUOISE};
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.9rem;
    }}

    .bottom-strip {{
        background-color: {SIDEBAR_BG};
        border: 1px solid {BORDER_COLOR};
        border-radius: 16px;
        padding: 1rem 1.2rem;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }}

    .bottom-strip-title {{
        color: {SECONDARY_TURQUOISE};
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }}

    .bottom-strip-text {{
        color: {TEXT_WHITE};
        font-size: 0.95rem;
        margin-bottom: 0.8rem;
    }}

    .timeline-badge {{
        display: inline-block;
        padding: 0.45rem 0.8rem;
        border: 1px solid rgba(0,242,255,0.25);
        border-radius: 999px;
        color: {SECONDARY_TURQUOISE};
        font-size: 0.88rem;
        margin-right: 0.5rem;
        margin-bottom: 0.35rem;
        background: rgba(0,242,255,0.05);
    }}

    div[data-testid="metric-container"] {{
        background-color: {CARD_BG};
        border: 1px solid {BORDER_COLOR};
        border-radius: 14px;
        padding: 1rem;
    }}

    div[data-testid="metric-container"] label {{
        color: {SECONDARY_TURQUOISE} !important;
    }}

    div[data-testid="metric-container"] [data-testid="stMetricValue"] {{
        color: {TEXT_WHITE};
    }}

    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div {{
        background-color: {PRIMARY_BLUE};
        color: {TEXT_WHITE};
        border: 1px solid rgba(255,255,255,0.08);
    }}

    .stRadio > div {{
        gap: 0.35rem;
    }}

    .stDataFrame {{
        border-radius: 12px;
        overflow: hidden;
    }}

    .stAlert {{
        border-radius: 12px;
    }}
    </style>
    """
