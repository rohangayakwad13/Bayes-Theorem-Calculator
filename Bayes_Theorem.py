import streamlit as st 
import LL_AnimeST as llst
import theme
import matplotlib.pyplot as plt

try:
    st.set_page_config(
        page_title="Baye's Theorem",
        page_icon="🅱️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if "welcome_once" not in st.session_state:
        st.session_state.welcome_once = False


    @st.dialog(":yellow[*Welcome*]",icon="👑",width="medium")
    def welcome():
        st.title(":rainbow[Welcome to **Baye's Theorem**]",text_alignment="center", anchor="Wels")
        st.divider()
        st.header(":red[What is **Baye's Theorem?**]",text_alignment="center")
        st.markdown("""
    -> :green[**Baye's Theorem :material/analytics:**]  helps calculate :material/calculate: :blue[**probabilities**] step-by-step.

    It's Like  updating your guess with new :yellow[**info:material/info:**].

    Example -> :green['What's the *chance* it's **rain**.']

    If your app :blue[says] :red[70:material/percent:] **cloudy**? :material/cloud:
    """,text_alignment="center")
        st.divider()
        st.info("""
        :violet[Simple Tool] By :green[**Rohan Gayakwad :red[(**SkillVerse Py**)]**].       
        Perfect For :blue[Students] & :red[Quick Math]. 
        """, icon=":material/psychology:")

    if st.session_state.welcome_once is False:
        welcome()
        st.session_state.welcome_once = True

    lottie_sci = llst.load_lottiefile("Boy_Studying_Science.json")
    lottie_robo = llst.load_lottiefile("Ai_powered_marketing_tools_abstract.json")

    st.markdown(theme.stApp.theme_black(), unsafe_allow_html=True)

    st.title(":rainbow[**Baye's Theorem Calculator**]",text_alignment="center",anchor="Baye's Theorem")
    st.caption("By Rohan Gayakwad",text_alignment="right")
    st.divider()
    st.markdown("<h3 style='color: cyan; font-family: Arial, sans-serif; font-style: italic; letter-spacing: 2px; text-transform: uppercase; text-shadow: 2px 2px 5px gray;'>Formula</h3>",unsafe_allow_html=True, text_alignment="center")
    st.latex(r"\textcolor{yellow}{P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}}")

    st.markdown("<h3 style='color: cyan; font-family: Arial, sans-serif; font-style: italic; letter-spacing: 2px; text-transform: uppercase; text-shadow: 2px 2px 5px gray;'>Formula For P(D)</h3>",unsafe_allow_html=True, text_alignment="center")
    st.latex(r"P(D) = P(A) \cdot P(D|A) + P(B) \cdot P(D|B) + P(C) \cdot P(D|C)")
    st.divider()

    co1, co2 = st.columns(2, gap="medium", vertical_alignment="top", border=True)

    with co1:
        llst.st_lottie(lottie_robo, height=300)
        
    with co2:
        llst.st_lottie(lottie_sci, height=300)
        
    st.divider()  

    st.subheader(":yellow[**⁘ Example ⁘**]",text_alignment="center",divider=True)

    st.markdown("""
    **:green[Problem]:** :red[Three mining companies :grey[A, B,] And :grey[C] supply gold to a refinery. A Defective gold bar :green[(impure or underweight)] is found during quality inspection. What is the probability it came from each company?]
    """)
    st.divider()
    st.header(":yellow[Total Supply]",text_alignment="center")
    st.subheader(":blue[Company A, B, And C]",text_alignment="center")

    supply, default = st.columns(2, gap="medium", vertical_alignment="top", border=True)
    with supply:
        st.latex(r"P(A) = 40\%")
        st.latex(r"P(B) = 30\%")
        st.latex(r"P(C) = 30\%")

    with default:
        st.latex(r"P(D|A) = 3\%")
        st.latex(r"P(D|B) = 2\%")
        st.latex(r"P(D|C) = 5\%")
        
    st.latex(r"P(D) = P(A) \cdot P(D|A) + P(B) \cdot P(D|B) + P(C) \cdot P(D|C)")
    st.markdown("---")
    pac, pbc, pcc = st.columns(3, gap="medium", vertical_alignment="center", border=True)

    with pac:
        st.latex(r"P(A|D) = \frac{P(A) \cdot P(D|A)}{P(D)}")

    with pbc:
        st.latex(r"P(B|D) = \frac{P(B) \cdot P(D|B)}{P(D)}")
    with pcc:
        st.latex(r"P(C|D) = \frac{P(C) \cdot P(D|C)}{P(D)}")

    st.latex(r"P(D) = 0.4 \cdot 0.03 + 0.3 \cdot 0.02 + 0.3 \cdot 0.05")


    st.subheader(":blue[*Probability*]",text_alignment="center")
    st.latex(rf"P(A|D) = 0.25")
    st.latex(rf"P(B|D) = 0.28125")
    st.latex(rf"P(C|D) = 0.46875")
    st.latex(rf"P(D) = 0.032")

    st.divider()

    st.divider()   

    col1, col2 = st.columns(2)

    with col1:
        pa = (st.number_input(":green[P(A)]",placeholder="Enter Value In Percent(%)", value=40, icon=":material/percent:")) / 100
        pb = (st.number_input(":green[P(B)]",placeholder="Enter Value In Percent(%)", value=30, icon=":material/percent:")) / 100

        pc = (st.number_input(":green[P(C)]",placeholder="Enter Value In Percent(%)", value=30, icon=":material/percent:")) / 100
        
    with col2:
        pda = (st.number_input(":green[P(A|D)]",placeholder="Enter Value In Percent(%)", value=2, icon=":material/percent:")) / 100
        pdb = (st.number_input(":green[P(B|D)]",placeholder="Enter Value In Percent(%)", value=3, icon=":material/percent:")) / 100
        pdc = (st.number_input(":green[P(C|D)]",placeholder="Enter Value In Percent(%)", value=5, icon=":material/percent:")) / 100
        
    st.divider()
    if st.button("Check Probability",type="primary",icon=":material/query_stats:"):
        if pa < 0 or pb < 0 or pc < 0:
            st.warning("Probabilities P(A), P(B), and P(C) cannot be negative.", icon="⚠️")

        if pa + pb + pc > 1:
            st.warning("The sum of P(A), P(B), and P(C) cannot exceed 100%.", icon="⚠️")

        if pda < 0 or pdb < 0 or pdc < 0:
            st.warning("Conditional probabilities cannot be negative.", icon="⚠️")

        if pda > 1 or pdb > 1 or pdc > 1:
            st.warning("Conditional probabilities cannot be greater than 100%.", icon="⚠️")    
            
        pd = pa * pda + pb * pdb + pc * pdc
        pad = pa * pda / pd
        pbd = pb * pdb / pd
        pcd = pc * pdc / pd
        st.divider()
        st.latex(rf"P(D) = {pd}")
        st.subheader(":blue[*Probability*]",text_alignment="center")
        st.latex(rf"P(A|D) = {pad}")
        st.latex(rf"P(B|D) = {pbd}")
        st.latex(rf"P(C|D) = {pcd}")
        st.divider()
        st.balloons()
        
        values = [pad, pbd, pcd]
        labels = ["P(A|D)", "P(B|D)", "P(C|D)"]
        
        cl1, cl2, cl3 = st.columns(3, gap="medium", vertical_alignment="bottom")
        with cl2:
            fig, ax = plt.subplots(figsize=(4,4))
            ax.pie(
            values, 
            
            labels=labels, 
            
            autopct="%1.1f%%", 
            
            startangle=90, 
            
            radius=0.75,
            
            labeldistance=1.05,

            pctdistance=0.6,
            
            textprops={'fontsize': 10}
            
            )
            
            ax.set_title("Posterior Probabilities", fontsize=15, pad=20)
            plt.tight_layout()
            st.pyplot(fig)    
            st.divider()
    st.divider()

    st.subheader("**:red[What Is Baye's Theorem]**",text_alignment="center")
    st.markdown("""
    :green[**Baye's Theorem :material/analytics:**]  helps calculate :material/calculate: :blue[**probabilities**] step-by-step.

    It's Like  updating your guess with new :yellow[**info:material/info:**].

    Example -> :green['What's the *chance* it's **rain**.']

    If your app :blue[says] :red[70:material/percent:] **cloudy**? :material/cloud:
    """,text_alignment="center")

    st.divider()
    c1, c2, c3 = st.columns(3, gap="medium",vertical_alignment="center", border=True)
        
        
    with c1:
        st.image("SkillPy.png",caption="Rohan R. Gayakwad")
        
    with c2:
        st.info("""
        :violet[Simple Tool] By :green[**Rohan Gayakwad :red[(**SkillVerse Py**)]**].       
        Perfect For :blue[Students] & :red[Quick Math].
        """, icon=":material/psychology:")
        
    with c3:
        lottie_py = llst.load_lottiefile("Python_logo.json")
        llst.st_lottie(lottie_py, height=300)
        
except Exception as e:
    @st.dialog(":red[ERROR]",icon="spinner")
    def err():
        st.title(":red[Error]",text_alignment="center", anchor="error")
        st.error(str(e))
    err()