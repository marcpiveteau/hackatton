import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_player import st_player
import numpy as np
from sklearn.neighbors import NearestNeighbors
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

url = "https://raw.githubusercontent.com/marcpiveteau/hackatton/main/df_total_VF.csv"
df_music = pd.read_csv(url)


st.title('Bienvenue sur Christinagueret!')



recherche = st.selectbox("Quel est le fait marquant de ta journée ?",['choisissez votre tématique:','travail','famille', 'Santé'])

if recherche == 'travail':
	recherche2 = st.selectbox("Que c'est il passé au travail ?",['choisissez votre raison','Licenciment','Promotion', 'enguelade avec les collègues'])
if recherche == 'famille':
	recherche2 = st.selectbox("Que c'est il passé dans ton cercle familliale ?",['choisissez votre raison', 'Rupture/divorce','Rencontre/Mariage', 'Naissance', 'Deces', 'Anniversaire'])
if recherche == 'Santé':
	recherche2 = st.selectbox("Que c'est il passé sur ta santé ?",['resultat de ton test PCR ?','Not Covid','Covid'])
	if recherche2 =='Not Covid':
		st_player('https://www.youtube.com/watch?v=F00I4iyoi9g')
	if recherche2 =='Covid':
		st_player('https://www.youtube.com/watch?v=HepA8LzKDi8')

humeur = st.select_slider('Et comment vois tu la suite ? ',options=["On continue s'enfonce", 'On maintient', 'On redresse la barre'])



simpson = st.selectbox("Quel personnage des simpsons de represente le plus ?",['toute la famille','Homer','Bart', 'Lisa Gothique', 'Maggie', 'Apu', 'Otto bus', 'Le riche Texan', 'Flanders','Krusty le clown', 'Smithers'])

if simpson == 'toute la famille':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/une-simpson-anecodotes.jpg)")
	choix = st.checkbox("toute la famille : tous les genres")
	if not choix:
		st.stop()
if simpson == 'Homer':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/homer.jpg)")
	choix = st.checkbox('homer :bauf, dance, kitch, Tu veux ta recommandation de musique alors clic')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/homergif.gif)")
	if not choix:
		st.stop()
if simpson == 'Bart':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/bart2.jpg)")
	choix = st.checkbox('Bart : hip hop, rap, rnb')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/bartgif.gif)")
	if not choix:
		st.stop()
if simpson == 'Lisa Gothique':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Lisa%20Gothique.jpg)")
	choix = st.checkbox('Lisa gothique : Rock, Folk')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/lisagif.gif)")
	if not choix:
		st.stop()
if simpson == 'Maggie':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/maggie.jpg)")
	choix = st.checkbox("Maggie : Musique d'enfant")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/the-simpsons-maggie-simpson.gif)")
	if not choix:
		st.stop()
if simpson == 'Apu':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Apu.jpg)")
	choix = st.checkbox("Apu : indie, world")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/simpsons-apu.gif)")
	if not choix:
		st.stop()	
if simpson == 'Otto bus':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/ottomann1_1.jpg)")
	choix = st.checkbox("Otto bus : Reggae, reaggaton, ska")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/otto-guitar.gif)")
	if not choix:
		st.stop()	
if simpson == 'Le riche Texan':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/le%20riche%20texa.jpg)")
	choix = st.checkbox("Le riche texan : Country")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/riche%20texan.gif)")
	if not choix:
		st.stop()
if simpson == 'Flanders':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/ned-flanders-250.jpg)")
	choix = st.checkbox("Flanders: Classic, Opera")
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/flanders.gif)")
	if not choix:
		st.stop()
if simpson == 'Krusty le clown':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Krusty%20le%20clown.jpg)")
	choix = st.checkbox('krusty : electro')
	if choix:
		st.markdown("![Alt Text](https://github.com/marcpiveteau/hackatton/blob/main/krusty-the-clown%20gif.gif?raw=true)")
	if not choix:
		st.stop()
if simpson == 'Smithers':
	st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/Smithers.jpg)")
	choix = st.checkbox('Smithers : Jazz, soual')
	if choix:
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/hackatton/main/homergif.gif)")
	if not choix:
		st.stop()




if simpson == 'Homer':
    df_choix = df_music[df_music['genre'].isin(['Dance', 'beauf'])]
if simpson == 'Bart':
    df_choix = df_music[df_music['genre'].isin(['Rap', 'R&B', 'Hip-Hop', 'Soul'])]
if simpson == 'Maggie':
    df_choix = df_music[df_music['genre'].isin(["Children's Music", "Children`s Music"])]
if simpson == 'Apu':
    df_choix = df_music[df_music['genre'].isin(['Indie', 'World'])]
if simpson == 'Flanders':
    df_choix = df_music[df_music['genre'].isin(['Opera', 'Classical'])]
if simpson == 'Le riche Texan':
    df_choix = df_music[df_music['genre'].isin(['Country', 'Folk'])]
if simpson == 'Lisa Gothique':
    df_choix = df_music[df_music['genre'].isin(['Rock','Pop'])]
if simpson == 'Otto bus':
    df_choix = df_music[df_music['genre'].isin(['Reggae', 'Reggaeton','Ska'])]
if simpson == 'Smithers':
    df_choix = df_music[df_music['genre'].isin(['Jazz', 'Blues'])]
if simpson == 'Krusty le clown ':
    df_choix = df_music[df_music['genre'].isin(['Electronic'])]



if humeur == "On continue s'enfonce":
    df_humeur = df_choix[(df_choix['danceability'] < df_choix['danceability'].quantile(0.25)) & (df_choix['energy'] < df_choix['energy'].quantile(0.25)) & (df_choix['liveness'] < df_choix['liveness'].quantile(0.25))]

if humeur == 'On maintient':
    df_humeur = df_choix[(df_choix['danceability'].quantile(0.25) < df_choix['danceability'] < df_choix['danceability'].quantile(0.75)) & (df_choix['energy'].quantile(0.25) < df_choix['energy'] < df_choix['energy'].quantile(0.75)) & (df_choix['liveness'].quantile(0.25) < df_choix['liveness'] < df_choix['liveness'].quantile(0.75))]

if humeur == 'On redresse la barre':
    df_humeur = df_choix[(df_choix['danceability'] > df_choix['danceability'].quantile(0.75)) & (df_choix['energy'] > df_choix['energy'].quantile(0.75)) & (df_choix['liveness'] > df_choix['liveness'].quantile(0.75))]


choixgraf = st.selectbox("Tu veux voir des graphiques est des data analysts après tout?",['Fait ton choix:','non','sur toutes les musiques','Bases de ton personnages', 'base de ton personnages avec ton humeur'])
if choixgraf =='Fait ton choix:':
	st.stop()
if choixgraf =='sur toutes les musiques':
	df_graf = df_music
if choixgraf =='Bases de ton personnages':
	df_graf = df_choix
if choixgraf =='base de ton personnages avec ton humeur':
	df_graf = df_humeur

tablegraf2 = df_graf.pivot_table(  index = 'genre', values = 'track_name', aggfunc = 'count', )
tablegraf3 = tablegraf2.reset_index()

fig1 = px.bar(tablegraf3,x='genre', y="track_name",color='genre',labels={"track_name" : "nombre de musique"})
fig1.update_layout(
     title={'text': "nombre de musique par genres pour ton personnage",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_size= 25,
    title_font_color="#FA0087")
st.plotly_chart(fig1)
choixgraf2 = st.selectbox("Et maintenant tu veux voir quoi ?",['choisi ici :','rien','les musiques les plus populaires', 'les artistes les plus populaires',"tu t'enfonce encore plus avec les chansons qui bouge le moins","tu redresse avec les chansons qui bouge le plus"])
if choixgraf2 =='choisi ici :':
	st.stop()
if choixgraf2 =='les musiques les plus populaires':
	variablegraf = 'track_name'
	nbchanson = [i for i in range(1,11)]
	nbchdir = st.selectbox("jusqu'a combien veux tu voir ? ",nbchanson)
	tablenbchanson1 = df_graf.sort_values(by='popularity', ascending= False).reset_index()
	tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
	fig2 = px.bar(tablenbchanson2,x=variablegraf, y='popularity',color=variablegraf,animation_group=variablegraf,labels={"popularity" : 'note de poularité', variablegraf : 'nom de la chanson'})
	fig2.update_layout(
     title={'text': "classement des meilleurs chansons de ta selection",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_size= 25,
    title_font_color="#FA0087")
	st.plotly_chart(fig2)
if choixgraf2 =='les artistes les plus populaires':
	variablegraf = 'artist_name'
	nbchanson = [i for i in range(1,11)]
	nbchdir = st.selectbox("jusqu'a combien veux tu voir ? ",nbchanson)
	tablenbchanson1 = df_graf.sort_values(by='popularity', ascending= False).reset_index()
	tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
	fig2 = px.bar(tablenbchanson2,x=variablegraf, y='popularity',color=variablegraf,animation_group=variablegraf,labels={"popularity" : 'note de poularité', variablegraf : 'artiste'})
	fig2.update_layout(
     title={'text': "classement des meilleurs artistes de ta selection",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_size= 25,
    title_font_color="#FA0087")
	st.plotly_chart(fig2)
if choixgraf2 =="tu redresse avec les chansons qui bouge le plus":
	variablegraf = 'track_name'
	nbchanson = [i for i in range(1,11)]
	nbchdir = st.selectbox("jusqu'a combien veux tu voir ? ",nbchanson)
	tablenbchanson1 = df_graf.sort_values(by='danceability', ascending= False).reset_index()
	tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
	fig2 = px.scatter(tablenbchanson2,x=variablegraf, y='danceability',color='popularity',size='popularity',labels={"danceability" : 'niveau de bougitude', variablegraf : 'artiste'})
	fig2.update_layout(
     title={'text': "classement des chansons qui bouge le plus",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_size= 25,
    title_font_color="#FA0087")
	st.plotly_chart(fig2)
if choixgraf2 =="tu t'enfonce encore plus avec les chansons qui bouge le moins":
	variablegraf = 'track_name'
	nbchanson = [i for i in range(1,11)]
	nbchdir = st.selectbox("jusqu'a combien veux tu voir ? ",nbchanson)
	tablenbchanson1 = df_graf.sort_values(by='danceability', ascending= True).reset_index()
	tablenbchanson2 = tablenbchanson1.iloc[:nbchdir,:]
	fig2 = px.scatter(tablenbchanson2,x=variablegraf, y='danceability',color='popularity',size='popularity',labels={"danceability" : 'niveau de bougitude', variablegraf : 'artiste'})
	fig2.update_layout(
     title={'text': "classement des chansons qui bouge le moins",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_size= 25,
    title_font_color="#FA0087")
	st.plotly_chart(fig2)


import random 
df_humeur = df_humeur.drop_duplicates(subset=['track_id'])
list_track = df_humeur['track_name'].to_list()
selection = random.sample(list_track, 10)
df_selection = df_humeur[df_humeur['track_name'].isin(selection)]
df_selection2 = df_selection[['genre', 'artist_name','track_name']]
df_selection2.reset_index(drop=True,inplace=True)
df_selection2.reset_index(inplace=True)
st.dataframe(df_selection2)



if(st.button('1 : cela te plait ou veut tu une autre selection')):
	selection = random.sample(list_track, 10)
	df_selection = df_humeur[df_humeur['track_name'].isin(selection)]
	if(st.button('2 : cela te plait ou veut tu une autre selection')):
		selection = random.sample(list_track, 10)
		df_selection = df_humeur[df_humeur['track_name'].isin(selection)]
		st.dataframe(df_selection)
		if(st.button('3 : cela te plait ou veut tu une autre selection')):
			st.write('tu ne sais pas ce que tu veux va te coucher')
			
				

df_selection3 = df_selection2
choixmusique = st.number_input('choisit le numero de ta chanson que tu veux écouter entre(1 et 9)',step=1)
lignedelamusique= df_selection3[df_selection3['index'] ==choixmusique]
lignedelamusique2 = df_selection[df_selection['track_name'].str.contains(lignedelamusique.iloc[0,3])]
st.write('vous avez choisis le titre', lignedelamusique.iloc[0,3], 'interpreté par',lignedelamusique.iloc[0,2], 'du genre', lignedelamusique.iloc[0,1])

df_music2 =df_humeur[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
choixmusique2 = lignedelamusique2[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
import numpy as np
from sklearn.neighbors import NearestNeighbors
X = df_music2[['popularity','acousticness', 'danceability', 'energy','instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence']]
distanceKNN = NearestNeighbors(n_neighbors=10).fit(X)
arraydesvoisin = distanceKNN.kneighbors(choixmusique2)
listvoisin = df_music.iloc[arraydesvoisin[1][0]]
listvoisin = listvoisin.drop_duplicates(subset=['track_id'])
st.write("on vous recommande :")
nom =listvoisin['track_name'].tolist()
for i in range(len(listvoisin)):
	st.write('le titre ',listvoisin.iloc[i,3], "de l'ariste",listvoisin.iloc[i,2], 'du genre', listvoisin.iloc[i,1] )
