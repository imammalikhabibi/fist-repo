# sepeti biasa, import dl
import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamli

st.set_page_config(page_title="Sales Dashboard",
                    page_icon="bar_chart:",
                    layout="wide"
)

# Baca file excel
df = pd.read_excel(
    io='payment data.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='A:P',
    nrows=1000,
)
 
# Filter samping kiri
st.sidebar.header("Please Filter Month Here:")
month = st.sidebar.multiselect(
    "Select Month",
    options=df["MONTH"].unique(),
    default=df["MONTH"].unique()
)

st.sidebar.header("Please Filter Grade Here:")
grade = st.sidebar.multiselect(
    "Select Grade",
    options=df["GRADE"].unique(),
    default=df["GRADE"].unique()
)


st.sidebar.header("Please Filter Package Here:")
package = st.sidebar.multiselect(
    "Select Package",
    options=df["PACKAGE"].unique(),
    default=df["PACKAGE"].unique()
)

df_selection = df.query(
    "MONTH == @month & GRADE == @grade & PACKAGE == @package"
)

st.dataframe(df_selection)


#----- HALAMAN UTAMA -----
st.title(":bar_chart: SALES DASHBOARD")
st.markdown("##")

# KPI Yang akan di munculkan

total_sales = int(df_selection["AMOUNT"].count())
total_revenue = int(df_selection["AMOUNT"].sum())

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Sales")
    st.subheader(f"{total_sales}")
with right_column:
    st.subheader("Total Revenue")
    st.subheader(f"Rp. {total_revenue}")


st.markdown("")
