# Import Library
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# ----- LOAD LOTTIE URL ----
def load_lottieurl(url):
    result = requests.get(url)
    if result.status_code != 200:
        return None
    return result.json()


# ----- LOAD LOCAL CSS -----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ----- TAB TITLE -----
st.set_page_config(page_title="Library", page_icon=":book:", layout="wide")


# ----- LOAD ASSETS -----
powershell_lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_c9eTLUgblo.json")
python_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_NGpl1AFNBd.json")
bash_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tBkhDllG4M.json")
perl_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_uR3DwK9y5B.json")
vb_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_l3sfdi9x.json")
nice_work_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_L7UPXCrytj.json")
local_css("style/style.css")


# ----- MAIN -----
def main():
    menu = ["PowerShell", "Python", "Bash", "Perl", "VB"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "PowerShell":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Powershell Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my PowerShell Codes!")
                st.write(
                    "I am passionate about finding ways to use Powershell to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(powershell_lottie, height=300, key="coding")
    elif choice == "Python":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Python Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Python Codes!")
                st.write(
                    "I am passionate about finding ways to use Python to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(python_lottie, height=300, key="coding")
    elif choice == "Bash":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Bash Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Bash Codes!")
                st.write(
                    "I am passionate about finding ways to use Bash to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(bash_lottie, height=300, key="coding")
    elif choice == "Perl":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Perl Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Perl Codes!")
                st.write(
                    "I am passionate about finding ways to use Perl to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(perl_lottie, height=300, key="coding")
    else:
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("VB Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my VB Codes!")
                st.write(
                    "I am passionate about finding ways to use VB to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(vb_lottie, height=300, key="coding")

    # ----- CONTACT FORM -----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("Feel free to share the suggestions and correction regarding codes. I will try my best to apply your"
                 "ideas. If there is something you want me to put here, I will be happy to help and provide you "
                 "the code here or as well as in GitHub for community share.")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/kaushtubhjha45.kj@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder= "Your name" required>
            <input type="email" name="email" placeholder= "Your email" required>
            <textarea name="message" name="email" placeholder= "Your message here..." required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_col, right_col = st.columns(2)
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st.empty()


if __name__ == "__main__":
    main()