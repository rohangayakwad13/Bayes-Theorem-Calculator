class stApp:
    def theme_black():
        return """<style>
    .stApp {
        background-color: black;
    }

    .main-title {
        font-family: 'Helvetica Neue', Arial, Helvetica, sans-serif;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }

    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 10px;
    }

    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: none;
        height: 50px;
        font-size: 18px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #2563EB;
        color: white;
    }

</style>"""

    def theme_white():
        return """<style>
    .stApp {
        background-color: white;
    }

    .main-title {
        font-family: 'Helvetica Neue', Arial, Helvetica, sans-serif;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }

    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 10px;
    }

    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: none;
        height: 50px;
        font-size: 18px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #2563EB;
        color: white;
    }

</style>"""


    def theme_crimson():
        return """<style>
    .stApp {
        background-color: crimson;
    }

    .main-title {
        font-family: 'Helvetica Neue', Arial, Helvetica, sans-serif;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }

    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 10px;
    }

    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: none;
        height: 50px;
        font-size: 18px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #2563EB;
        color: white;
    }

</style>"""


    def theme_cyan():
        return """<style>
    .stApp {
        background-color: cyan;
    }

    .main-title {
        font-family: 'Helvetica Neue', Arial, Helvetica, sans-serif;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }

    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 10px;
    }

    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: none;
        height: 50px;
        font-size: 18px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #2563EB;
        color: white;
    }

</style>"""


    def theme_glassmorphism():
        return """<style>
    html, body, .stApp {
        transition: 0.3s;
        font-family: Arial, sans-serif;
        background-color: #111;
        color: #eee;
    }

    .dark {
        background: #222 !important;
        color: #eee !important;
    }

    .light {
        background: #f5f5f5 !important;
        color: #111 !important;
    }

    .main-title {
        font-family: 'Helvetica Neue', Arial, Helvetica, sans-serif;
        color: #1E90FF;
        text-align: center;
        padding: 22px;
        font-weight: bold;
        font-size: 32px;
    }

    .result-card {
        background-color: #ffffff11;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ffffff22;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        text-align: center;
        margin-bottom: 12px;
        backdrop-filter: blur(6px);
    }

    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        width: 100%;
        border-radius: 10px;
        border: none;
        height: 50px;
        font-size: 18px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #2563EB;
        color: white;
        transform: scale(1.02);
    }

    textarea, input, select {
        border-radius: 8px !important;
        padding: 8px !important;
        background: #ffffff11 !important;
        border: 1px solid #ffffff33 !important;
        color: white !important;
    }

    .stSlider > div {
        color: white !important;
    }
    </style>
    """