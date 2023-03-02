import streamlit as st
from urllib.request import urlopen, urlretrieve
import json


def download_img(url, file_name):
    response = urlopen(url)
    with open(file_name, "wb") as f:
        f.write(response.read())
    st.success(f"Image saved as {file_name}")


language = ['en',
            'cs',
            ' da',
            ' de',
            ' es',
            ' fr',
            ' id',
            ' it',
            ' hu',
            ' nl',
            ' no',
            ' pl',
            ' pt',
            ' ro',
            ' sk',
            ' fi',
            ' sv',
            ' tr',
            ' vi',
            ' th',
            ' bg',
            ' ru',
            ' el',
            ' ja',
            ' ko',
            ' zh']

category = ['default',
            'backgrounds',
            'fashion',
            'nature',
            'science',
            'education',
            'feelings',
            'health',
            'people',
            'religion',
            'places',
            'animals',
            'industry',
            'computer',
            'food',
            'sports',
            'transportation',
            'travel',
            'buildings',
            'business',
            'music']

colors = ["grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue", "lilac", "pink", "white",
          "gray", "black", "brown"]

safesearch = ["Hayır", "Evet"]

aranan = st.text_input("Fotoğrafını aramak istediğiniz kelimeyi yazınız")

col1, col2, col3, col4 = st.columns(4)
with col1:
    dil = st.selectbox("Dil Seçiniz", language)
with col2:
    kat_ara = st.selectbox("Kategori Seçiniz", category)
with col3:
    renk = st.multiselect("Renk Seçiniz", colors)
with col4:
    guv_ara = st.selectbox("Güvenli Arama", safesearch)

if st.button("Ara", key=1):
    if guv_ara == "Hayır":
        guv_ara = "false"
    else:
        guv_ara = "true"
    if kat_ara == "default":
        url = "https://pixabay.com/api/?key=33380115-b8edaed9c4a65b866639700e7&q=" + aranan + "&image_type=photo&lang=" + dil + "&safesearch=" + guv_ara + "&per_page=40"
    else:
        url = "https://pixabay.com/api/?key=33380115-b8edaed9c4a65b866639700e7&q=" + aranan + "&image_type=photo&lang=" + dil + "&category=" + kat_ara + "&safesearch=" + guv_ara + "&per_page=40"
    if renk is not None:
        newrenk = ["&colors=" + color for color in renk]
        newrenkurl = " ".join(newrenk)
        url = "https://pixabay.com/api/?key=33380115-b8edaed9c4a65b866639700e7&q=" + aranan + "&image_type=photo&lang=" + dil + "&category=" + kat_ara + "&safesearch=" + guv_ara + newrenkurl + "&per_page=40"
    data1 = urlopen(url).read()
    veri = json.loads(data1)
    x = 3
    for a in veri["hits"]:
        sonuc = a["webformatURL"]
        st.image(sonuc)
        #Button'a basıldığında sayfayı yeniliyor. Bu nedenle yorum satırı haline getirildi.
        #filename = a["largeImageURL"].split("/")[-1].split("?")[0]
        #if st.button("Download Image", key=x):
        #    download_img(a["largeImageURL"], filename)
        #x += 1
