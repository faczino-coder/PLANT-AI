def load_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        margin: 0;
        padding: 0;
    }
/* ── POPOVER BUTTONS ── */
[data-testid="stPopover"] button {
    background: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 6px !important;
    color: #000000 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    padding: 0.3rem 0.6rem !important;
    box-shadow: none !important;
    min-height: 0 !important;
}
[data-testid="stPopover"] button:hover {
    background: #f4faf4 !important;
    color: #2d6a2d !important;
    border-color: #2d6a2d !important;
}
[data-testid="stPopover"] button p {
    color: #000000 !important;
    font-size: 0.88rem !important;
}
[data-testid="stPopover"] button:hover p {
    color: #2d6a2d !important;
}
   .stApp {
    background-color: #ffffff !important;
    color: #000000 !important;
}
[data-testid="column"] {
    background: transparent !important;
}
#MainMenu footer { visibility: hidden; }    
    .stDeployButton { display: none; }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    /* ── HERO ── */
    .hero-section {
        position: relative;
        width: 100%;
        min-height: 85vh;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        display: flex;
        align-items: center;
        overflow: hidden;
    }
    .hero-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            rgba(10,40,10,0.88) 0%,
            rgba(15,55,15,0.65) 55%,
            rgba(5,30,5,0.30) 100%
        );
    }
    .hero-content {
        position: relative;
        z-index: 2;
        padding: 3rem 4rem;
        max-width: 55%;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.3);
        color: white;
        padding: 0.35rem 1rem;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        line-height: 1.1;
        color: white;
        margin-bottom: 1.2rem;
    }
    .hero-title-green { color: #4cda6e; }
    .hero-subtitle {
        font-size: 1.05rem;
        color: rgba(255,255,255,0.85);
        line-height: 1.7;
        margin-bottom: 2.5rem;
        max-width: 480px;
    }
    .hero-mini-features {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
        padding-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.15);
    }
    .hero-mini-feature {
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    .hero-mini-feature-icon {
        font-size: 1.3rem;
        color: #4cda6e;
    }
    .hero-mini-feature-text strong {
        display: block;
        font-size: 0.85rem;
        font-weight: 600;
        color: white;
    }
    .hero-mini-feature-text span {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.6);
    }

    /* ── MAGNIFIER ── */
    .hero-visual {
        position: absolute;
        right: 4rem;
        top: 50%;
        transform: translateY(-50%);
        z-index: 2;
        width: 360px;
        height: 360px;
    }
    .magnifier-ring {
        width: 360px;
        height: 360px;
        border-radius: 50%;
        border: 6px solid rgba(76,218,110,0.6);
        box-shadow:
            0 0 0 12px rgba(76,218,110,0.08),
            0 0 60px rgba(76,218,110,0.25);
        overflow: hidden;
        position: relative;
        background: rgba(0,40,0,0.4);
    }
    .magnifier-handle {
        position: absolute;
        bottom: -55px;
        right: -15px;
        width: 14px;
        height: 75px;
        background: linear-gradient(180deg,#a0a0a0,#606060);
        border-radius: 7px;
        transform: rotate(45deg);
        transform-origin: top center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    }
    .magnifier-dots {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        display: grid;
        grid-template-columns: repeat(5,1fr);
        gap: 18px;
        opacity: 0.2;
    }
    .magnifier-dot {
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background: #4cda6e;
    }
    .tech-circle-1 {
        position: absolute;
        inset: -20px;
        border-radius: 50%;
        border: 2px dashed rgba(76,218,110,0.25);
        animation: spin 20s linear infinite;
    }
    .tech-circle-2 {
        position: absolute;
        inset: -45px;
        border-radius: 50%;
        border: 1px dashed rgba(76,218,110,0.12);
        animation: spin 30s linear infinite reverse;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }

    /* ── SECTION LABEL ── */
    .section-label {
        font-size: 0.78rem;
        font-weight: 700;
        color: #2d6a2d;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 1.2rem;
    }

    /* ── CROP CARDS ── */
    .crop-card {
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        background: white;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .crop-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(45,106,45,0.15);
    }
    .crop-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }
    .crop-card-label {
        padding: 0.8rem;
        text-align: center;
        font-weight: 700;
        font-size: 0.95rem;
        color: #1a1a1a;
        background: white;
    }

    /* ── FEATURE CARDS ── */
    .feature-card {
        background: #f9faf9;
        border: 1px solid #e8f0e8;
        border-radius: 12px;
        padding: 1rem 0.6rem;
        text-align: center;
        transition: box-shadow 0.2s, transform 0.2s;
    }
    .feature-card:hover {
        box-shadow: 0 6px 20px rgba(45,106,45,0.1);
        transform: translateY(-2px);
    }
    .feature-card-icon { font-size: 1.6rem; margin-bottom: 0.5rem; }
    .feature-card-title {
        font-size: 0.78rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.2rem;
    }
    .feature-card-sub { font-size: 0.7rem; color: #888; }

    /* ── STAT CARDS ── */
    .stat-card {
        background: #f9faf9;
        border: 1px solid #e8f0e8;
        border-radius: 12px;
        padding: 1rem 0.6rem;
        text-align: center;
    }
    .stat-card-icon { font-size: 1.6rem; margin-bottom: 0.3rem; }
    .stat-card-value {
        font-size: 1.4rem;
        font-weight: 800;
        color: #2d6a2d;
    }
    .stat-card-label {
        font-size: 0.7rem;
        color: #888;
        margin-top: 0.2rem;
    }

    /* ── TRUST BAR ── */
    .trust-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
        padding: 1.5rem 2rem;
        background: #f4faf4;
        border-top: 1px solid #e8f0e8;
        border-bottom: 1px solid #e8f0e8;
    }
    .trust-avatars { display: flex; align-items: center; }
    .trust-avatar {
        font-size: 1.8rem;
        background: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #e8f0e8;
        margin-right: -6px;
    }
    .trust-count {
        margin-left: 1rem;
        font-weight: 700;
        color: #2d6a2d;
        font-size: 0.9rem;
    }
    .trust-count span {
        display: block;
        font-weight: 400;
        color: #666;
        font-size: 0.75rem;
    }
    .available-on {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        font-size: 0.85rem;
        color: #666;
    }
    .platform-icon { font-size: 1.3rem; cursor: pointer; }

    /* ── FOOTER ── */
    .landing-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.2rem 2rem;
        background: white;
        border-top: 1px solid #e8f0e8;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .landing-footer-copy { font-size: 0.82rem; color: #999; }
    .landing-footer-socials {
        display: flex;
        gap: 1rem;
        font-size: 1.3rem;
    }

    /* ── PAGE BANNER ── */
    .page-banner-wrap {
        position: relative;
        width: 100%;
        height: 180px;
        overflow: hidden;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .page-banner {
        width: 100%;
        height: 180px;
        object-fit: cover;
        display: block;
    }
    .page-banner-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            rgba(10,40,10,0.80) 0%,
            rgba(15,55,15,0.50) 100%
        );
        display: flex;
        align-items: center;
        padding: 0 2.5rem;
    }
    .page-banner-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: white;
    }
    .page-banner-sub {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.8);
        margin-top: 0.3rem;
    }

    /* ── UPLOAD AREA ── */
    .upload-area {
        background: white;
        border: 2px dashed #c8e6c9;
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .upload-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
    .upload-title {
        font-size: 1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.4rem;
    }
    .upload-sub { font-size: 0.82rem; color: #888; }

    /* ── RESULT CARD ── */
    .result-card {
        background: white;
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border: 1px solid #e8f0e8;
        margin-bottom: 1rem;
    }
    .result-disease-name {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1a1a1a;
    }
    .result-crop-badge {
        display: inline-block;
        background: #e8f5e9;
        color: #2d6a2d;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-left: 0.8rem;
        vertical-align: middle;
    }
    .result-conf-label {
        font-size: 0.75rem;
        color: #888;
        margin: 0.8rem 0 0.3rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .result-conf-bar-bg {
        background: #e8f0e8;
        border-radius: 10px;
        height: 10px;
        overflow: hidden;
    }
    .result-conf-bar-fill {
        height: 10px;
        border-radius: 10px;
    }
    .result-conf-value {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }
    .result-section-title {
        font-size: 0.78rem;
        font-weight: 700;
        color: #1a1a1a;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin: 1.2rem 0 0.6rem;
    }
    .result-treatment-item {
        display: flex;
        align-items: flex-start;
        gap: 0.6rem;
        font-size: 0.88rem;
        color: #333;
        margin: 0.4rem 0;
        line-height: 1.5;
    }
    .result-check { color: #2d6a2d; font-weight: 700; }

    /* ── CHAT ── */
    .chat-container {
        background: white;
        border-radius: 16px;
        border: 1px solid #e8f0e8;
        height: 55vh;
        overflow-y: auto;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .chat-bubble-user {
        background: #2d6a2d;
        color: white;
        padding: 0.75rem 1.1rem;
        border-radius: 18px 18px 4px 18px;
        font-size: 0.88rem;
        max-width: 70%;
        line-height: 1.5;
    }
    .chat-bubble-bot {
        background: #f4faf4;
        color: #1a1a1a;
        padding: 0.75rem 1.1rem;
        border-radius: 18px 18px 18px 4px;
        font-size: 0.88rem;
        max-width: 70%;
        line-height: 1.5;
        border: 1px solid #e8f0e8;
    }

    /* ── TIPS BOX ── */
    .tips-box {
        background: #f4faf4;
        border: 1px solid #c8e6c9;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-top: 1rem;
    }
    .tips-title {
        font-weight: 700;
        color: #2d6a2d;
        margin-bottom: 0.8rem;
        font-size: 0.9rem;
    }
    .tips-list {
        font-size: 0.83rem;
        color: #555;
        line-height: 2.1;
    }

    /* ── PANEL BOX ── */
    .panel-box {
        background: white;
        border: 1px solid #e8f0e8;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .panel-title {
        font-weight: 700;
        font-size: 0.95rem;
        color: #1a1a1a;
        margin-bottom: 1rem;
    }

    /* ── HISTORY ITEM ── */
    .history-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.75rem;
        background: #f9faf9;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        border: 1px solid #e8f0e8;
    }
    .history-name {
        font-size: 0.82rem;
        font-weight: 600;
        color: #1a1a1a;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .history-disease {
        font-size: 0.74rem;
        color: #888;
    }
    .history-dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        flex-shrink: 0;
    }
    </style>
    """
