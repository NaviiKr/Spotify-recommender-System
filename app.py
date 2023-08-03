import pickle
import streamlit as st
import requests

def recommend(song):
    index = songs[songs['Song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_song_names = []
    recommended_song_posters = []
    recommended_song_links = []
    for i in distances[1:26]:
        # fetch the movie poster
        #movie_id = songs.iloc[i[0]]
        recommended_song_posters.append(songs.iloc[i[0]].Image)
        recommended_song_names.append(songs.iloc[i[0]].Song)
        recommended_song_links.append(songs.iloc[i[0]].link)
    return recommended_song_names, recommended_song_posters,recommended_song_links

st.header('Spotify  Song  Recommender')

songs = pickle.load(open('songs.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

songs_list = songs['Song'].values

selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    songs_list
)
st.text("")
if st.button('Show Recommendation'):
    st.text("")
    st.text("")
    st.text("")
    recommended_song_names,recommended_song_posters,recommended_song_links = recommend(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    st.text("")
    st.text("")
    st.text("")
    with col1:
        st.text(recommended_song_names[0])
        st.image(recommended_song_posters[0])
        st.write("[link](%s)" % recommended_song_links[0])
    with col2:
        st.text(recommended_song_names[1])
        st.image(recommended_song_posters[1])
        st.write("[link](%s)" % recommended_song_links[1])
    with col3:
        st.text(recommended_song_names[2])
        st.image(recommended_song_posters[2])
        st.write("[link](%s)" % recommended_song_links[2])
    with col4:
        st.text(recommended_song_names[3])
        st.image(recommended_song_posters[3])
        st.write("[link](%s)" % recommended_song_links[3])
    with col5:
        st.text(recommended_song_names[4])
        st.image(recommended_song_posters[4])
        st.write("[link](%s)" % recommended_song_links[4])
    co1, co2, co3, co4, co5 = st.columns(5)
    st.text("")
    st.text("")
    st.text("")
    with co1:
        st.text(recommended_song_names[5])
        st.image(recommended_song_posters[5])
        st.write("[link](%s)" % recommended_song_links[5])
    with co2:
        st.text(recommended_song_names[6])
        st.image(recommended_song_posters[6])
        st.write("[link](%s)" % recommended_song_links[6])
    with co3:
        st.text(recommended_song_names[7])
        st.image(recommended_song_posters[7])
        st.write("[link](%s)" % recommended_song_links[7])
    with co4:
        st.text(recommended_song_names[8])
        st.image(recommended_song_posters[8])
        st.write("[link](%s)" % recommended_song_links[8])
    with co5:
        st.text(recommended_song_names[9])
        st.image(recommended_song_posters[9])
        st.write("[link](%s)" % recommended_song_links[9])
    co1, co2, co3, co4, co5 = st.columns(5)
    st.text("")
    st.text("")
    st.text("")
    with co1:
        st.text(recommended_song_names[10])
        st.image(recommended_song_posters[10])
        st.write("[link](%s)" % recommended_song_links[10])
    with co2:
        st.text(recommended_song_names[11])
        st.image(recommended_song_posters[11])
        st.write("[link](%s)" % recommended_song_links[11])
    with co3:
        st.text(recommended_song_names[12])
        st.image(recommended_song_posters[12])
        st.write("[link](%s)" % recommended_song_links[12])
    with co4:
        st.text(recommended_song_names[13])
        st.image(recommended_song_posters[13])
        st.write("[link](%s)" % recommended_song_links[13])
    with co5:
        st.text(recommended_song_names[14])
        st.image(recommended_song_posters[14])
        st.write("[link](%s)" % recommended_song_links[14])
    co1, co2, co3, co4, co5 = st.columns(5)
    st.text("")
    st.text("")
    st.text("")
    with co1:
        st.text(recommended_song_names[15])
        st.image(recommended_song_posters[15])
        st.write("[link](%s)" % recommended_song_links[15])
    with co2:
        st.text(recommended_song_names[16])
        st.image(recommended_song_posters[16])
        st.write("[link](%s)" % recommended_song_links[16])
    with co3:
        st.text(recommended_song_names[17])
        st.image(recommended_song_posters[17])
        st.write("[link](%s)" % recommended_song_links[17])
    with co4:
        st.text(recommended_song_names[18])
        st.image(recommended_song_posters[18])
        st.write("[link](%s)" % recommended_song_links[18])
    with co5:
        st.text(recommended_song_names[19])
        st.image(recommended_song_posters[19])
        st.write("[link](%s)" % recommended_song_links[19])

    co1, co2, co3, co4, co5 = st.columns(5)
    with co1:
        st.text(recommended_song_names[20])
        st.image(recommended_song_posters[20])
        st.write("[link](%s)" % recommended_song_links[20])
    with co2:
        st.text(recommended_song_names[21])
        st.image(recommended_song_posters[21])
        st.write("[link](%s)" % recommended_song_links[21])
    with co3:
        st.text(recommended_song_names[22])
        st.image(recommended_song_posters[22])
        st.write("[link](%s)" % recommended_song_links[22])
    with co4:
        st.text(recommended_song_names[23])
        st.image(recommended_song_posters[23])
        st.write("[link](%s)" % recommended_song_links[23])
    with co5:
        st.text(recommended_song_names[24])
        st.image(recommended_song_posters[24])
        st.write("[link](%s)" % recommended_song_links[24])