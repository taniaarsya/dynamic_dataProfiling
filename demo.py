import streamlit as st
import pandas as pd

## library visualisasi
import matplotlib.pyplot as plt
import plotly.express as px

st.write("Belajar Streamlit dari Basic")

st.write('''
**keunggulan streamlit**
- cocok untuk *pemula*
- hanya membutuhkan pemahaman bahasa **python**
         ''')

st.write("![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Ffree-png-vectors%2Fdata-scientist&psig=AOvVaw2CakQk2dnR3H7o99YXw2hC&ust=1721913922989000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOD9_6_jv4cDFQAAAAAdAAAAABAE)")

## membaca data
df = pd.read_csv ("data_input/properti_jual.csv")

## menampilkan dataframe
st.write("Data Harga Properti di Jabodetabek",df)

## menampilkan jenis sertifikat 
st.write(df['Sertifikat'].unique())

## -----------------------------------------------------------------

# visualisasi statis
fig, ax = plt.subplots()
df['Kota'].value_counts().plot(kind='bar', ax=ax)

st.write(fig)

# visualisasi interaktif
fig2 = px.bar(df['Tipe.Properti'].value_counts())

st.write(fig2)

## -----------------------------------------------------------------
st.markdown ("---")
st.markdown ("#Data Properti")

## -----------------------------------------------------------------

# membuat layout dengan 2 kolom 
col1 , col2 = st.columns(2)

# mengisi setiap column
with col1:
    st.subheader("Proporsi data dimasing-masing kota")
    st.write(fig)

with col2:
    st.subheader("Proporsi data jenis properti")
    st.write(fig2)

## -----------------------------------------------------------------
with st.expander("Klik untuk  melihat lebih detail"):
    # membuat layout dengan 2 column
    col1, col2 = st.columns(2)
    # mengisi pada setiap columns
    with col1 :
        st.subheader("Propersi data dimasing-masing kota")
        st.write(fig)
    
    with col2 :
        st.subheader("Propersi data jenis properti")
        st.write(fig)

## ----------------------------------------------------------------- sidebar
st.sidebar.markdown("## Menu")

with st.sidebar:
    st.write("---")
    st.write("Pilih Menu disini")

## ----------------------------------------------------------------- tabs
tabs = st.tabs(["Proporsi tipe properti","Persebaran harga properti"])

# menambahkan konten
with tabs [0]:
    st.write(fig)

with tabs [1]:
    st.write(fig2)

## ----------------------------------------------------------------- input
pilihan_kota = st.selectbox(
    "Pilih kota:",
    options = df['Kota'].unique(),
    index=None
)

if pilihan_kota is None:
    st.write("Silahkan pilih kota")

else :
    kota = df[df['Kota'] == pilihan_kota]
    jumlah_kota = kota.shape[0]

    # output 
    st.write(f"Jumlah data properti pada kota {pilihan_kota}\
             adalah {jumlah_kota}")








