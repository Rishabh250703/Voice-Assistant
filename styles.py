# Store the custom CSS in a variable to be imported by the main app
CUSTOM_CSS = """
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: #05060a;
}
[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}
/* Main title */
.friday-title {
    text-align: center;
    font-family: Arial, sans-serif;
    font-size: 42px;
    font-weight: 500;
    letter-spacing: 2px;
    color: #f4f7ff;
    margin-top: 15px;
}
.friday-subtitle {
    text-align: center;
    color: #8d94a6;
    font-size: 15px;
    margin-top: -8px;
}
/* ============================================================
   AI ORB
   ============================================================ */
.orb-container {
    height: 390px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}
/* Outer glow */
.orb {
    width: 190px;
    height: 190px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #ffffff 0%, #cbd7ff 7%, #728cff 20%, #4754ff 38%, #151a61 65%, #070817 100%);
    box-shadow: 0 0 25px rgba(92, 111, 255, 0.8), 0 0 70px rgba(65, 82, 255, 0.45), 0 0 130px rgba(65, 82, 255, 0.22);
    position: relative;
    transition: all 0.5s ease;
}
/* Orb inner light */
.orb::before {
    content: "";
    position: absolute;
    width: 85px;
    height: 55px;
    left: 32px;
    top: 25px;
    border-radius: 50%;
    background: rgba(255,255,255,0.17);
    filter: blur(12px);
}
/* Orb states */
.orb.sleeping {
    transform: scale(0.82);
    opacity: 0.65;
    box-shadow: 0 0 20px rgba(90, 100, 180, 0.35), 0 0 55px rgba(60, 70, 150, 0.15);
}
.orb.activated {
    animation: activatedPulse 2.5s infinite ease-in-out;
}
.orb.listening {
    animation: listeningPulse 1.1s infinite ease-in-out;
    box-shadow: 0 0 30px rgba(0, 220, 255, 0.9), 0 0 75px rgba(0, 190, 255, 0.55), 0 0 140px rgba(0, 160, 255, 0.25);
}
.orb.speaking {
    animation: speakingPulse 0.65s infinite alternate ease-in-out;
    box-shadow: 0 0 30px rgba(255, 150, 70, 0.9), 0 0 75px rgba(255, 110, 40, 0.55), 0 0 140px rgba(255, 80, 20, 0.25);
}
@keyframes activatedPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.06); }
}
@keyframes listeningPulse {
    0%, 100% { transform: scale(0.94); }
    50% { transform: scale(1.13); }
}
@keyframes speakingPulse {
    from { transform: scale(0.92); }
    to { transform: scale(1.14); }
}
/* Status */
.status {
    text-align: center;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #dce2f5;
    margin-top: -20px;
}
.status-small {
    text-align: center;
    color: #777f96;
    font-size: 13px;
    margin-top: 7px;
}
/* Conversation area */
.conversation {
    margin-top: 25px;
    padding: 20px;
    border-radius: 20px;
    background: rgba(20, 23, 34, 0.65);
    border: 1px solid rgba(255,255,255,0.07);
    min-height: 80px;
}
.user-text {
    color: #dce5ff;
    font-size: 15px;
}
.friday-text {
    color: #9ba8ff;
    font-size: 15px;
    margin-top: 10px;
}
/* Buttons */
div.stButton > button {
    border-radius: 25px;
    height: 50px;
    background: #111522;
    color: #e8ecff;
    border: 1px solid rgba(130,145,255,0.25);
    transition: 0.2s;
}
div.stButton > button:hover {
    border-color: rgba(130,145,255,0.8);
    background: #171c30;
}
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
"""