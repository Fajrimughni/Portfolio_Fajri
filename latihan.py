import streamlit as st
st.set_page_config(layout='wide')
st.title('Portfolio Saya')
st.header('Data Scientist')
st.sidebar.title('Navigasi Halaman')
page = st.sidebar.radio('Pilih halaman', ['Tentang saya', 
                                          'Proyek', 'Prediction', 
                                          'Kontak'])
if page == 'Tentang saya':
    import about
    about.about_me()

elif page == 'Proyek':
    import proyek
    proyek.tampilan_proyek()

elif page == 'Kontak':
    import kontak
    kontak.munculkan_kontak()

elif page == 'Prediction':
    import prediksi
    prediksi.lakukan_prediksi()    
