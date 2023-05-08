# import dl streamlit nya
from PIL import Image
import streamlit as st
# Biar bisa masukan animasi dari lottie import dl ke sini
import requests
from streamlit_lottie import st_lottie

# Emoji bisa didapatkan disini: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Halaman Web Saya", page_icon=":man:", layout="wide")

# Definisikan lottie nya dl

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200: 
        return None
    return r.json()
    
# Munculkan assets -----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_49rdyysj.json")
img_tbl = Image.open("images/tbl1.png")


# Bagian Header -----
# Biar rapih pake container
with st.container():
	st.subheader("Hi, My name is Malik :wave:")
	st.title("A Data Analyst from Bandung, Indonesia")
left_column, right_column = st.columns([1,3])
with left_column:
    st.image('images/Malik Habibi small.png', caption='Imam Malik Habibi', width=200)
    with right_column:
            st.write("I am passionate about learning everything related to Data, now I am focusing on learning python as my new learning subject. Currently I am working as a data analyst in an education technology company. I am so happy working in a company who applied work from anywhere policy, so I can stay closely with my family and have a work life balance environment.")
            st.write("Hobbyes: Watching movies, swimming, playing badminton, reading")
            st.write("This website is one of my project, I create this website with python and streamlit as the framework")
            st.write("[See Profile>](https://www.linkedin.com/in/imam-malik-habibi-malik-b506354a/)")
# Bagian kerjaan ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do in my current company")
        st.write("##")
        st.write(
            """ 
            1.	Running Queries daily and weekly with more than 100Gb data collection using Big Query and Redash
            2.	Working with more than 10000 rows spreadsheets daily
            3.	I analyzed data and I make a summary or report according to the needs of each team and diagnosing problems if any
            4.	I also do an analysis of the data that I have pulled to get useful insights for the team. The insights that can be obtained can be in the form of data on the user's habits in using the application, when do users usually make payments, or how long do users use our application, and so on. Then provide suggestions that can support the progress of each team. Also help the team to identifying key components of problems and situation
            5.	Creates daily, weekly, monthly, and analytical dashboards to monitor retention/upgrade payment so we can overcome obstacles if any. And also create another dashboard for other teams with spreadsheets or Redash or Google data studio
            6.	Skill: SQL, Big Query, Spreadsheets, Excel, Power BI, Tableau, Python        
            """
            )
        with right_column:
            st_lottie(lottie_coding, height=550, key="data")
with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_tbl)
    with text_column:
        st.subheader("Sales dashboard 2")
        st.write(
            """
            Another view from Sales dashboard shows sales activity from an online learning platform. You can see sales data per period and by package and type of user
            """
            )
        st.markdown("[See Dashboard...](https://public.tableau.com/app/profile/imam.malik.habibi/viz/Salesdashboard2_16831712901900/SalesDashboard)")
