import streamlit as st
import pandas as pd
from Bio.Seq import Seq
import base64

st.set_page_config(page_title='Brzezinski Lab Tools')


@st.cache(allow_output_mutation=True)
def get_data():
    return []

def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.
    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.
    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')
    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

st.title('Brzezinski Lab Tools')
st.header('BbsI Guide Cloning')

col1, col2 = st.beta_columns(2)

guide_name = col1.text_input("Guide Name:", )
guide = col2.text_input("Input guide 5' to 3':")

if st.button('Generate Oligos'):
    try:
        if guide[0] == 'G' or guide[0] == 'g':
            optG = ''
            optC = ''

        else:
            optG = 'g'
            optC = 'c'

        oligo1 = 'cacc' + optG + guide

        guide_dna = Seq(guide)

        oligo2 = 'aaac' + str(guide_dna.reverse_complement()) + optC

        st.write("Guide length:" + str(len(guide)))
        if optG == 'g': st.write('U6 extra G added.')

        st.write('')
        st.write('')
        st.write('IDT Oligos to order:')
        
        get_data().append({'Guide':guide_name+'.1', 'Sequence': oligo1, 'nm': '25nm', 'style': 'STD'})
        get_data().append({'Guide':guide_name+'.2', 'Sequence': oligo2, 'nm': '25nm', 'style': 'STD'})

        st.table(pd.DataFrame(get_data()).set_index('Guide'))

    except(IndexError):
        pass

st.write('')
st.write('')
botcol_1, botcol_2 = st.beta_columns(2)
if botcol_1.button('Download as CSV'):
        tmp_download_link = download_link(pd.DataFrame(get_data()), 'Guides.csv', 'CSV generated! Click here to download your data!')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

if botcol_2.button('Reset Table'):
    get_data().clear()
