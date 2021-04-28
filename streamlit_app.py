import streamlit as st
from Bio.Seq import Seq


st.title('Brzezinski Lab Tools')


st.header('BbsI Guide Cloning')
guide = st.text_input("Input guide 5' to 3':")

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
    st.write(oligo1)
    st.write(oligo2)

except(IndexError):
    pass