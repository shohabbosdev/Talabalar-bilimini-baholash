import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_elements import elements, mui, html
from streamlit_elements import nivo

st.set_page_config("Talabalar bilimini baholashning kompleks tizimi","🎓","wide","expanded")
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Baholash", ["Bosh sahifa", "Talabalar", "Fanlar", 'QR code'],
                            icons=['house-heart', 'file-earmark-person-fill', "book-half", 'qr-code'], key='menu_5', orientation="vertical")
    st.markdown(f"<hr>",unsafe_allow_html=True)
    # selected
if selected == 'Bosh sahifa':
    st.title('🌐 Bu bosh sahifa hisoblanadi')
    import random
    from datetime import date

    import numpy as np
    import pandas as pd
    import streamlit as st

    @st.cache_data
    def get_profile_dataset(number_of_items: int = 25, seed: int = 0) -> pd.DataFrame:
        new_data = []

        def calculate_age(born):
            today = date.today()
            return (
                today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            )

        from faker import Faker

        fake = Faker()
        random.seed(seed)
        Faker.seed(seed)

        for i in range(number_of_items):
            profile = fake.profile()
            new_data.append(
                {
                    "rasmi": f"https://picsum.photos/400/200?lock={i}",
                    "ismi": profile["name"],
                    "yoshi": calculate_age(profile["birthdate"]),
                    "faolligi": random.choice([True, False]),
                    "kunlik_faolligi": np.random.rand(25),
                    "bosh_sahifa": profile["website"][0],
                    "email": profile["mail"],
                    "faol": np.random.randint(2, 90, size=25),
                    "jinsi": random.choice(["erkak", "ayol", "boshqa", None]),
                    "Tug'ilgan yili": profile["birthdate"],
                    "holati": round(random.uniform(0, 1), 2),
                }
            )

        profile_df = pd.DataFrame(new_data)
        profile_df["jinsi"] = profile_df["jinsi"].astype("category")
        return profile_df


    column_configuration = {
        "ismi": st.column_config.TextColumn(
            "Ismi", help="Talaba ismi", max_chars=100
        ),
        "rasmi": st.column_config.ImageColumn("Avatar", help="Talaba rasmi"),
        "faolligi": st.column_config.CheckboxColumn("Faolmi?", help="Ushbu foydalanuvchi faolmi?"),
        "bosh_sahifa": st.column_config.LinkColumn(
            "Bosh sahifa", help="Talaba bosh sahifasi"
        ),
        "jinsi": st.column_config.SelectboxColumn(
            "Jinsi", options=["erkak", "ayol", "boshqa"]
        ),
        "yoshi": st.column_config.NumberColumn(
            "Yoshi",
            min_value=0,
            max_value=120,
            format="%d yosh",
            help="Talaba yoshi",
        ),
        "faol": st.column_config.LineChartColumn(
            "1 yillik faolligi",
            help="The user's activity over the last 1 year",
            width="large",
            y_min=0,
            y_max=100,
        ),
        "kunlik_faolligi": st.column_config.BarChartColumn(
            "Kunlik faolligi",
            help="The user's activity in the last 25 days",
            width="medium",
            y_min=0,
            y_max=1,
        ),
        "holati": st.column_config.ProgressColumn(
            "Holati", min_value=0, max_value=1, format="%.2f"
        ),
        "Tug'ilgan kuni": st.column_config.DateColumn(
            "Tug'ilgan kuni",
            help="The user's birthdate",
            min_value=date(1999, 1, 1),
        ),
        "email": st.column_config.TextColumn(
            "Elektron pochta",
            help="Talaba elektron pochtasi",
            validate=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
        ),
    }

    st.data_editor(
        get_profile_dataset(),
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed"
    )    

# Talabalar bo'limi ----------------------------------------------------------------

elif selected == 'Talabalar':
    st.title('↖️ Bu talabalar sahifa hisoblanadi')
    st.html('<hr />')
    tugma=st.button("Talaba qo'shish", icon='➕')
    columns1, columns2, columns3, columns4 = st.columns(4)
    qator1,qator2, qator3, qator4 = st.columns([1,1,3,3])
    
    id = columns1.text_input(label='ID')
    ismi = columns2.selectbox("Ismi", options=['Tanlang...'])
    familiyasi = columns3.selectbox("Familiyasi", options=['Tanlang...'])
    dataofBirth = columns4.date_input("Tug'ilgan sanasi")
    searchBtn = qator1.button("Qidirish", icon="🔎")
    resetBtn = qator2.button("Reset", icon='🔁', type='primary')
    st.html('<hr />')
    
    st.dataframe({
         "#": [1,2,3,4],
         "Ismi": ["Akram", "Nurbek", "Sarvar","Odil"],
         "Familiyasi":["Mahmudov", "Sayviyev", "Ro'ziqulov", "Ahmedov"],
         "Tug'ilgan sanasi":["07.08.2004","19.10.2003","19.04.2004","19.10.2003"]
    }, use_container_width=True)

# Fanlar bo'limi ----------------------------------------------------------------

elif selected == 'Fanlar':
    st.title('🧪 Bu fanlar sahifa hisoblanadi')
    st.html('<hr />')
    tugmaFan=st.button("Fan yaratish", icon='➕')
    
    fqator1, fqator2, fqator3, fqator4, fqator5 =st.columns([3,3,3,1,1])
    fid = fqator1.text_input("ID")
    fnomi = fqator2.text_input("Fan nomi")
    ftil = fqator3.text_input("Til")
    fsearch = fqator4.button("Search", type='primary')
    freset = fqator5.button("Reset")
    st.html("<hr />")
    import random
    st.dataframe({
         "#": [1,2,3,4,5],
         "ID": [random.randrange(9) for i in range(5)],
         "Fan nomi":["Kompyuter arxitekturasi","Informatika","Informatika(rus)","Matematika","Kompyuter gragikasi"],
         "Til":[random.randrange(9) for i in range(5)]
    }, use_container_width=True)
    
    

# QR-Code bo'limi ----------------------------------------------------------------

else:
    st.title('🏳️‍🌈 Bu QR-Code images sahifasi hisoblanadi')
    st.html('<hr />')
    tugmaQR=st.button("QR-Code yaratish", icon='🖥')
    QRcolumns1, QRcolumns2, QRcolumns3 = st.columns(3)
    QRqator1,QRqator2, QRqator3, QRqator4 = st.columns([1,1,3,3])
    
    idQR = QRcolumns1.text_input(label='ID')
    imgQR = QRcolumns2.text_input("Image")
    variantQR = QRcolumns3.selectbox("Variant ID", options=['Tanlang...'])
    searchBtnQR = QRqator1.button("Qidirish", icon="🔎")
    resetBtnQR = QRqator2.button("Reset", icon='🔁', type='primary')
    st.html('<hr />')
    import segno
        
    matn = st.text_input("Ixtiyoriy matn kiriting", value='', max_chars=500)
    
    with st.expander("Qo'shimcha imkoniyatlarni ochish"):
        col1, col2, col3 = st.columns(3)
        selectColor = col1.color_picker("Rang tanlang", value='#fff')        
        selectScale = col2.slider("Tasvir shkalasini tanlang", 2, 20, 5, 1)
        selectBorder = col3.slider("Tasvir ramka qalinligini tanlang", 0, 15, 2, 1)
        
    images = segno.make_qr(f"{matn}", encoding='utf-8')
    images.save(    
        "src/scaled_qrcode.png",
        scale=selectScale,
        border=selectBorder,
        light=selectColor
    )
    rasm=st.image('src/scaled_qrcode.png', caption=f"{matn} so'zining qrcode natijasi", clamp=True)
