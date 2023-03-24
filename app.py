import streamlit as st
# Imposta lo sfondo personalizzato
page_bg_img = '''
<style>
body {
background-image: url("pxfuel.jpg");
background-size: cover;
}
</style>
'''

# Imposta lo sfondo della pagina
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Rocket Science App')

st.video('https://www.youtube.com/watch?v=DtVBCG6ThDk')

st.slider('Quante Volte Daniele ha detto "non è rocket science" oggi?',min_value=0,max_value=100)
if st.button('Pigiami per festeggiare!'):
    st.balloons()

import pandas as pd
import numpy as np
st.write('Tabella a Caso che mostra un indice di uso di quest app')

df = pd.DataFrame(
   np.random.randn(10, 11),
   columns=('%d' % i for i in range(11)))

st.dataframe(df)   #Same as st.write(df)




