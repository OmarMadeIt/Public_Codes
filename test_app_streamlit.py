import streamlit as st
import pandas as pd


# st.title('Explore a dataset')
# st.write('A general purpose data exploration app')
# file = st.file_uploader("Upload file", type=['csv'])
# st.write(file)
# def explore(df):
#   # DATA
#     st.write('Data:')
#     st.write(df)
    
#     # SUMMARY
#     output_globale = df.describe()
#     st.write('Summary:')
#     st.write(output_globale)
    
def explore(df):
  # DATA
    st.write('Data:')
    st.write(df)
    # SUMMARY
#     output_globale = df.describe()
    df.columns = [c.replace(' ', '_') for c in df.columns]
    #df['Date_Appel_Mois'] = df['Créé_le'].dt.to_period('M')
    df['Motif']=df['Motif'].str.lower()
    df['Motif']=df["Motif"].str.rsplit("-", 1).str[-1]
    output_globale = df.groupby(['Motif', 'Type_Offre']).Statut.count().reset_index()
    st.write('Summary:')
    st.write(output_globale)

def get_df(file):
    # get extension and read file
    extension = file.name.split('.')[1]
    if extension.upper() == 'XLSX':
        df = pd.read_excel(file)
    return df
def main():
    st.title('Explore a dataset')
    st.write('A general purpose data exploration app')
    file = st.file_uploader("Upload file", type=['csv' 
                                             ,'xlsx'
                                             ,'pickle'])
    if not file:
        st.write("Upload a .xlsx file to get started")
        return
    df = get_df(file)
    explore(df)
main()