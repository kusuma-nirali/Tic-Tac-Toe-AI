
import streamlit as st

from game_logic import create_board, make_move, check_winner, is_draw
from minimax import find_best_move


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Tic-Tac-Toe AI",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================
# DARK PREMIUM THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 5% 5%, #29204a 0%, transparent 32%),
        radial-gradient(circle at 95% 10%, #152c49 0%, transparent 35%),
        #0b1020;
    color: #eef0ff;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1050px;
    padding: 2rem 2rem 3rem;
}

h1, h2, h3 {
    color: #f1efff !important;
    font-family: 'Outfit', sans-serif !important;
}

p, label, span {
    color: inherit;
}

/* HERO */

.hero {
    background: linear-gradient(120deg, #19152c, #202445, #142c3c);
    border: 1px solid #39375e;
    padding: 38px 20px;
    border-radius: 24px;
    text-align: center;
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
    margin-bottom: 30px;
}

.hero-icon {
    font-size: 52px;
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 1px;
    background: linear-gradient(90deg, #c7a5ff, #7eaaff, #65e5d2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #aab4d1;
    font-size: 15px;
    margin-top: 10px;
}

.hero-tag {
    display: inline-block;
    background: #30264c;
    border: 1px solid #67549d;
    color: #d1b8ff;
    border-radius: 30px;
    padding: 9px 17px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 17px;
}

/* SECTION HEADINGS */

.section-heading {
    font-family: 'Outfit', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #e7e5ff;
    margin: 25px 0 15px;
}

/* PLAYER CARDS */

.player-card {
    padding: 22px;
    border-radius: 19px;
    min-height: 115px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.18);
}

.human-card {
    background: linear-gradient(135deg, #302039, #3b233d);
    border: 1px solid #81476f;
}

.ai-card {
    background: linear-gradient(135deg, #192844, #202d4d);
    border: 1px solid #42669d;
}

.player-symbol {
    font-size: 30px;
}

.player-name {
    color: #f4efff;
    font-size: 18px;
    font-weight: 800;
    margin-top: 5px;
}

.player-description {
    color: #b0b4d0;
    font-size: 12px;
    margin-top: 4px;
}

/* SCOREBOARD */

.score-card {
    padding: 22px 12px;
    border-radius: 19px;
    text-align: center;
    background: linear-gradient(145deg, #1a2035, #202840);
    border: 1px solid #343c5b;
    box-shadow: 0 8px 22px rgba(0,0,0,0.2);
    transition: transform 0.2s;
}

.score-card:hover {
    transform: translateY(-3px);
}

.score-label {
    color: #b2bad2;
    font-size: 13px;
    font-weight: 700;
}

.score-number {
    font-family: 'Outfit', sans-serif;
    font-size: 38px;
    font-weight: 800;
    margin-top: 8px;
}

.pink-score { color: #ff91c8; }
.blue-score { color: #8eabff; }
.green-score { color: #64e5c2; }

/* STATUS */

.status-card {
    background: linear-gradient(100deg, #292044, #1c304b);
    border: 1px solid #51467e;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    color: #d5c8ff;
    font-weight: 700;
    margin: 20px 0;
}

/* GAME BOARD */

.game-panel {
    background: #141b2d;
    padding: 22px;
    border: 1px solid #303a57;
    border-radius: 23px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
}

/* GAME BUTTONS */

.stButton > button {
    width: 100%;
    height: 115px;
    border-radius: 19px;
    background: linear-gradient(145deg, #202940, #192238);
    border: 2px solid #3c496b;
    color: #eef0ff;
    font-family: 'Outfit', sans-serif;
    font-size: 37px;
    font-weight: 800;
    box-shadow: 0 5px 15px rgba(0,0,0,0.22);
    transition: all 0.2s ease;
}

.stButton > button:hover:not(:disabled) {
    background: #30274b;
    border-color: #a58aff;
    color: #d5c5ff;
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(145,110,255,0.2);
}

.stButton > button:disabled {
    opacity: 1;
    background: #1c263b;
    border-color: #35425f;
    color: #e4e6ff;
}

/* PRIMARY BUTTONS */

.stButton > button[kind="primary"] {
    height: 55px;
    background: linear-gradient(110deg, #7652c8, #477bd5);
    color: white;
    border: none;
    border-radius: 15px;
    font-size: 15px;
    font-weight: 800;
    box-shadow: 0 6px 20px rgba(112,80,205,0.25);
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(110deg, #906be3, #5794ef);
    color: white;
}

/* ALERTS */

[data-testid="stAlert"] {
    border-radius: 15px;
}

/* EXPANDER */

[data-testid="stExpander"] {
    background: #171f32;
    border: 1px solid #38425f;
    border-radius: 16px;
    color: #e5e9ff;
}

[data-testid="stExpander"] summary {
    color: #d7c8ff;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 25px 10px;
    color: #8791b0;
    font-size: 12px;
    line-height: 1.8;
}

.footer strong {
    color: #b99aff;
}

hr {
    border-color: #303952;
    margin: 25px 0;
}

/* MOBILE */

@media (max-width: 600px) {
    .hero-title { font-size: 30px; }
    .hero { padding: 25px 12px; }
    .stButton > button { height: 75px; font-size: 27px; }
    .block-container { padding: 1rem; }
    .score-number { font-size: 27px; }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "board" not in st.session_state:
    st.session_state.board = create_board()

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "result" not in st.session_state:
    st.session_state.result = ""

if "human_score" not in st.session_state:
    st.session_state.human_score = 0

if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0


# ==========================================
# RESULT HANDLING
# ==========================================

def update_result():

    winner = check_winner(st.session_state.board)

    if winner == "X":
        st.session_state.result = "🎉 Congratulations! You Won!"
        st.session_state.human_score += 1
        st.session_state.game_over = True

    elif winner == "O":
        st.session_state.result = "🤖 AI Wins! Better luck next time!"
        st.session_state.ai_score += 1
        st.session_state.game_over = True

    elif is_draw(st.session_state.board):
        st.session_state.result = "🤝 It's a Draw! Great match!"
        st.session_state.draw_score += 1
        st.session_state.game_over = True


# ==========================================
# PLAYER AND AI MOVES
# ==========================================

def play_move(position):

    if st.session_state.game_over:
        return

    if make_move(st.session_state.board, position, "X"):

        update_result()

        if not st.session_state.game_over:

            ai_move = find_best_move(st.session_state.board)

            if ai_move is not None:
                make_move(st.session_state.board, ai_move, "O")
                update_result()


# ==========================================
# RESET FUNCTIONS
# ==========================================

def reset_game():

    st.session_state.board = create_board()
    st.session_state.game_over = False
    st.session_state.result = ""


def reset_scores():

    st.session_state.human_score = 0
    st.session_state.ai_score = 0
    st.session_state.draw_score = 0

    reset_game()


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="hero">
<div class="hero-icon">🎮</div>
<div class="hero-title">TIC-TAC-TOE AI</div>
<div class="hero-subtitle">Challenge your intelligence against Artificial Intelligence</div>
<div class="hero-tag">✨ POWERED BY MINIMAX ALGORITHM</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# PLAYERS
# ==========================================

st.markdown(
    '<div class="section-heading">👥 Meet the Players</div>',
    unsafe_allow_html=True
)

p1, p2 = st.columns(2)

with p1:
    st.markdown("""
<div class="player-card human-card">
<div class="player-symbol">❌</div>
<div class="player-name">Human Player</div>
<div class="player-description">Player X • Your challenge begins here</div>
</div>
""", unsafe_allow_html=True)

with p2:
    st.markdown("""
<div class="player-card ai-card">
<div class="player-symbol">⭕</div>
<div class="player-name">AI Computer</div>
<div class="player-description">Player O • Minimax intelligence</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# SCOREBOARD
# ==========================================

st.markdown(
    '<div class="section-heading">🏆 Match Scoreboard</div>',
    unsafe_allow_html=True
)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(f"""
<div class="score-card">
<div class="score-label">❌ YOUR WINS</div>
<div class="score-number pink-score">{st.session_state.human_score}</div>
</div>
""", unsafe_allow_html=True)

with s2:
    st.markdown(f"""
<div class="score-card">
<div class="score-label">🤖 AI WINS</div>
<div class="score-number blue-score">{st.session_state.ai_score}</div>
</div>
""", unsafe_allow_html=True)

with s3:
    st.markdown(f"""
<div class="score-card">
<div class="score-label">🤝 DRAWS</div>
<div class="score-number green-score">{st.session_state.draw_score}</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# GAME STATUS
# ==========================================

if st.session_state.game_over:

    if "You Won" in st.session_state.result:
        st.success(st.session_state.result)

    elif "AI Wins" in st.session_state.result:
        st.warning(st.session_state.result)

    else:
        st.info(st.session_state.result)

else:
    st.markdown("""
<div class="status-card">
✨ YOUR TURN! Select an empty box to make your move.
</div>
""", unsafe_allow_html=True)


# ==========================================
# GAME BOARD
# ==========================================

st.markdown(
    '<div class="section-heading">🎯 The Battle Arena</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="game-panel">', unsafe_allow_html=True)

for row in range(3):

    cols = st.columns(3, gap="medium")

    for col in range(3):

        position = row * 3 + col
        value = st.session_state.board[position]

        if value == "X":
            label = "❌"
        elif value == "O":
            label = "⭕"
        else:
            label = " "

        with cols[col]:

            st.button(
                label,
                key=f"cell_{position}",
                disabled=(
                    value != " " or st.session_state.game_over
                ),
                on_click=play_move,
                args=(position,),
                use_container_width=True
            )

st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# CONTROLS
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "🔄 NEW GAME",
        type="primary",
        use_container_width=True
    ):
        reset_game()
        st.rerun()

with c2:

    if st.button(
        "🗑️ RESET SCORES",
        use_container_width=True
    ):
        reset_scores()
        st.rerun()


# ==========================================
# GAME INFORMATION
# ==========================================

with st.expander("📖 HOW TO PLAY & ABOUT THE AI"):

    st.markdown("""
### 🎮 Game Instructions

1. You play as ❌ Player X.
2. The computer plays as ⭕ Player O.
3. Select an empty cell.
4. The AI automatically analyses and makes its move.
5. The first player to get three symbols in a row wins.

### 🧠 About Minimax Algorithm

Minimax is an Artificial Intelligence search algorithm.

- **Maximizing:** AI tries to achieve the highest score.
- **Minimizing:** AI considers the opponent's best possible response.
- **Decision Making:** It examines possible future game states before choosing a move.

### 🏆 Scoring System

| Result | Score |
|---|---:|
| AI Win | +10 |
| Human Win | -10 |
| Draw | 0 |
""")


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
<strong>🎮 TIC-TAC-TOE AI</strong>
<br>
Intelligent Gaming • Python • Streamlit • Minimax Algorithm
<br>
Mini Project | Artificial Intelligence
</div>
""", unsafe_allow_html=True)
