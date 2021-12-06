import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_player import st_player
from sklearn.neighbors import NearestNeighbors
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import random 

url = "https://raw.githubusercontent.com/marcpiveteau/hackatton/main/df_total_VF1.csv"
df_music = pd.read_csv(url,low_memory =False)


st.title('La musique de MURPHY')
st.title('"Le pire est toujours certain !"')

recherche = st.selectbox("Quelle est la déception de ta journée ?",['Choisis ta thématique :','Travail','Famille', 'Santé'])

if recherche == 'Travail':
	recherche2 = st.selectbox("Que s'est-il passé au travail ?",['Choisis ta raison','Licenciement','Du rouge dans ton code', 'Ta journée sur Stackoverflow', 'Dispute avec les collègues', 'Tu es muté à Guéret'])
if recherche == 'Famille':
	recherche2 = st.selectbox("Que s'est-il passé dans ton cercle familial ?",['Choisis ta raison', 'Rupture/divorce','Test de grossesse positif', 'Décès de ton hamster', 'Tu as dit OUI trop vite'])
if recherche == 'Santé':
	recherche2 = st.selectbox("Que s'est-il passé sur ta santé ?",['Résultat de ton test PCR ?','Covid','Not Covid'])
	if recherche2 =='Not Covid':
		st_player('https://www.youtube.com/watch?v=F00I4iyoi9g')
	if recherche2 =='Covid':
		st_player('https://www.youtube.com/watch?v=HepA8LzKDi8')

humeur = st.select_slider('Et comment vois tu la suite ? ',options=["Tu t'enfonces !", 'Tu prends un petit remontant !'])

choixgenerique = st.checkbox('Les Simpsons')
if choixgenerique:
	st_player('https://www.youtube.com/watch?v=QTm8Vqra7bE')

simpson = st.selectbox("Quel personnage des simpsons te représente le plus ?",['La famille','Homer','Bart', 'Lisa', 'Maggie', 'Apu', 'Otto', 'Le riche Texan', 'Flanders','Krusty le clown', 'Smithers','Disco Stu'])

if simpson == 'La famille':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/une-simpson-anecodotes.jpg)")
	choix = st.checkbox("La famille : tous les genres => Tu veux ta recommandation de musique alors clique")
	if not choix:
		st.stop()
if simpson == 'Homer':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/homer.jpg)")
	choix = st.checkbox('homer :beauf => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/homergif.gif)")
	if not choix:
		st.stop()
if simpson == 'Bart':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/bart2.jpg)")
	choix = st.checkbox('Bart : hip hop, rap, rnb => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/bartgif.gif)")
	if not choix:
		st.stop()
if simpson == 'Lisa':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Lisa%20Gothique.jpg)")
	choix = st.checkbox('Lisa : Rock, Folk => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/lisagif.gif)")
	if not choix:
		st.stop()
if simpson == 'Maggie':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/maggie.jpg)")
	choix = st.checkbox("Maggie : Musique d'enfant  => Tu veux ta recommandation de musique alors clique")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/the-simpsons-maggie-simpson.gif)")
	if not choix:
		st.stop()
if simpson == 'Apu':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Apu.jpg)")
	choix = st.checkbox("Apu : World  => Tu veux ta recommandation de musique alors clique")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/simpsons-apu.gif)")
	if not choix:
		st.stop()	
if simpson == 'Otto':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/ottomann1_1.jpg)")
	choix = st.checkbox("Otto : Reggae, reaggaton, ska => Tu veux ta recommandation de musique alors clique")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/otto-guitar.gif)")
	if not choix:
		st.stop()	
if simpson == 'Le riche Texan':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/le%20riche%20texa.jpg)")
	choix = st.checkbox("Le riche texan : Country => Tu veux ta recommandation de musique alors clique")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/riche%20texan.gif)")
	if not choix:
		st.stop()
if simpson == 'Flanders':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/ned-flanders-250.jpg)")
	choix = st.checkbox("Flanders: Classic, Opera => Tu veux ta recommandation de musique alors clique")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/flanders.gif)")
	if not choix:
		st.stop()
if simpson == 'Krusty le clown':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Krusty%20le%20clown.jpg)")
	choix = st.checkbox('krusty : electro => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://github.com/marcpiveteau/hackatton/blob/main/krusty-the-clown%20gif.gif?raw=true)")
	if not choix:
		st.stop()
if simpson == 'Smithers':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Smithers.jpg)")
	choix = st.checkbox('Smithers : Jazz, soul => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/smithersgif2.gif)")
	if not choix:
		st.stop()
if simpson == 'Disco Stu':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/disco%20stu.jpg)")
	choix = st.checkbox('Disco Stu : Dance => Tu veux ta recommandation de musique alors clique')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/disco%20stugif.gif)")
	if not choix:
		st.stop()


if simpson == 'La famille':
    df_choix = df_music
if simpson == 'Homer':
    df_choix = df_music[df_music['genre'].isin(['beauf'])]
if simpson == 'Bart':
    df_choix = df_music[df_music['genre'].isin(['Rap', 'R&B', 'Hip-Hop', 'Soul'])]
if simpson == 'Maggie':
    df_choix = df_music[df_music['genre'].isin(["Children’s Music"])]
if simpson == 'Apu':
    df_choix = df_music[df_music['genre'].isin(['World'])]
if simpson == 'Flanders':
    df_choix = df_music[df_music['genre'].isin(['Opera', 'Classical'])]
if simpson == 'Le riche Texan':
    df_choix = df_music[df_music['genre'].isin(['Country', 'Folk'])]
if simpson == 'Lisa':
    df_choix = df_music[df_music['genre'].isin(['Rock','Pop'])]
if simpson == 'Otto':
    df_choix = df_music[df_music['genre'].isin(['Reggae', 'Reggaeton','Ska'])]
if simpson == 'Smithers':
    df_choix = df_music[df_music['genre'].isin(['Jazz', 'Blues'])]
if simpson == 'Krusty le clown':
    df_choix = df_music[df_music['genre'].isin(['Electronic'])]
if simpson == 'Disco Stu':
    df_choix = df_music[df_music['genre'].isin(['Dance'])]


if humeur == "Tu t'enfonces !":
    df_humeur = df_choix[(df_choix['danceability'] < df_choix['danceability'].quantile(0.5)) & (df_choix['energy'] < df_choix['energy'].quantile(0.5)) & (df_choix['liveness'] < df_choix['liveness'].quantile(0.5))]


if humeur == 'Tu prends un petit remontant !':
    df_humeur = df_choix[(df_choix['danceability'] > df_choix['danceability'].quantile(0.5)) & (df_choix['energy'] > df_choix['energy'].quantile(0.5)) & (df_choix['liveness'] > df_choix['liveness'].quantile(0.5))]


choixgraf = st.selectbox("Tu es Data Analyst, voir un graphique te réconforte",["Fais ton choix d'analyse :",'Non merci, laisse moi tranquille !','Musiques de ton personnage', 'Musiques de ton personnage selon ton humeur'])
if choixgraf =="Fais ton choix d'analyse :":
	st.stop()
if choixgraf =='Musiques de ton personnage':
	df_graf = df_choix
if choixgraf =='Musiques de ton personnage selon ton humeur':
	df_graf = df_humeur
try:
	tablegraf2 = df_graf.pivot_table(  index = 'genre', values = 'track_name', aggfunc = 'count', )
	tablegraf3 = tablegraf2.reset_index()

	fig1 = px.bar(tablegraf3,x='genre', y="track_name",labels={"track_name" : "nombre de musique"})
	fig1.update_layout(
	     title={'text': "Nombre de musiques de ta sélection par genre",'x':0.5,'xanchor': 'center','yanchor': 'top'},
	    title_font_family="Times New Roman",
	    title_font_size= 25,
	    title_font_color="#000000")
	st.plotly_chart(fig1)
	choixgraf2 = st.selectbox("On sait que tu aimes bien les graphiques, tu peux en avoir un de plus",['Tu as le choix :','Donne moi un titre, tout de suite','Les musiques les plus populaires', 'Les artistes les plus populaires'])
	if choixgraf2 =='Tu as le choix :':
		st.stop()
	if choixgraf2 =='Les musiques les plus populaires':
		variablegraf = 'track_name'
		nbchdir = 5
		tablenbchanson1 = df_graf.sort_values(by='popularity', ascending= False).reset_index()
		tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
		fig2 = px.scatter(tablenbchanson2,x=variablegraf, y='popularity',color='danceability',size='danceability',labels={"danceability" : 'Niveau de groove', variablegraf : 'artiste'})
		fig2.update_layout(
	     title={'text': "Top des chansons les plus populaires",'x':0.5,'xanchor': 'center','yanchor': 'top'},
	    title_font_family="Times New Roman",
	    title_font_size= 25,
	    title_font_color="#000000")
		st.plotly_chart(fig2)
	if choixgraf2 =='Les artistes les plus populaires':
		variablegraf = 'artist_name'
		nbchdir = 5
		tablenbchanson1 = df_graf.sort_values(by='popularity', ascending= False).reset_index()
		tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
		fig2 = px.scatter(tablenbchanson2,x=variablegraf, y='popularity',color='danceability',size='danceability',labels={"danceability" : 'Niveau de groove', variablegraf : 'artiste'})
		fig2.update_layout(
	     title={'text': "Top des artistes les plus populaires",'x':0.5,'xanchor': 'center','yanchor': 'top'},
	    title_font_family="Times New Roman",
	    title_font_size= 25,
	    title_font_color="#000000")
		st.plotly_chart(fig2)
except:
	pass




if(st.button('voir reco ou relancer une autre reco')):
	df_humeur = df_humeur.drop_duplicates(subset=['track_id'])
	list_track = df_humeur['track_name'].to_list()
	selection = random.sample(list_track, 1)
	df_selection = df_humeur[df_humeur['track_name'].isin(selection)]
	df_selection2 = df_selection[['genre', 'artist_name','track_name']]
	df_selection2.reset_index(drop=True,inplace=True)
	df_selection2.reset_index(inplace=True)
	st.write("Nous te conseillons d'écouter le titre :")
	st.table(df_selection2.drop('index', axis=1).rename(columns={'artist_name': 'Artiste','track_name':'Titre','genre': 'Genre'}))
	lien= 'https://open.spotify.com/track/'
	lien1 = df_selection.iloc[0,4]
	lientotal = lien + lien1
	link = lientotal
	st.markdown(link, unsafe_allow_html=True)

	df_selection3 = df_selection2


	lignedelamusique= df_selection3[df_selection3['track_name'] ==selection]
	lignedelamusique2 = df_selection[df_selection['track_name'].str.contains(lignedelamusique.iloc[0,3])]
	

	df_music2 =df_humeur[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
	choixmusique2 = lignedelamusique2[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
	import numpy as np
	from sklearn.neighbors import NearestNeighbors
	X = df_music2[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
	distanceKNN = NearestNeighbors(n_neighbors=10).fit(X)
	arraydesvoisin = distanceKNN.kneighbors(choixmusique2)
	listvoisin = df_humeur.iloc[arraydesvoisin[1][0]]
	listvoisin = listvoisin.drop_duplicates(subset=['track_id'])
	st.write("Si ce titre te convient, voici 10 autres titres :")
	listvoisin1 = listvoisin[['genre','artist_name','track_name']].reset_index(drop=True)
	listvoisin1.rename(columns={'artist_name': 'Artiste','track_name':'Titre','genre': 'Genre'},inplace=True)
	listvoisin1.drop(0,0,inplace=True)
	st.table(listvoisin1)
	st.write('Et voici les lien si une autre chanson que tu kiff plus')
	for i in range(len(listvoisin)-1):
		num_index = i+1
		st.write(num_index ,' lien vers : ', listvoisin.iloc[num_index,3])
		lien2 = listvoisin.iloc[num_index,4]
		lientotal2 = lien + lien2
		link2 = lientotal2
		st.markdown(link2, unsafe_allow_html=True)
	
