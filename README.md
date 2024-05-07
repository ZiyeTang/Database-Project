# MyMusics
## Summary
For our project, we will be creating a website to search through song data, similar to Spotify. Visitors will be greeted with a search bar allowing for the searching of songs, albums, artists, or lyrics which will be used to determine what song they are trying to find. Users will be able to make an account and create playlists, adding songs from their searches, and add songs or artists to a favorites section. Additionally, upon searching a song various similar songs by genre will appear, allowing for users to discover new music to potentially add to their playlists.

## Description
We aim to help users discover new music through both recommendations and by providing extensive information on songs/artists they have heard. The data will provide all the necessary information for songs including duration, genre, artist, album, and images of the latter two for the UI side of the site. These components will also be compared to other songs to create recommendations of similar music. 
In addition to the search feature there will be accounts users can create. This will grant access to playlist creation and favoriting songs, albums or artists, which will show up on the user's account. This will act as the user's custom bio/page, and can be shown off similarly to a social media page but with a focus on one's musical tastes.

## Usefulness
This website will be similar to Spotify, with the exception of not playing music for the user. This site will focus more on the exploratory side of music with its recommendation feature, and the playlists users create would be useful to show to their friends
## Realness
Our data is about informations of musics mainly before 2019. It includes many attributes of songs, albums, lyrics, releases, etc. Here is the website our data is from: [MusicOSet](https://marianaossilva.github.io/DSW2019/#tables)
## Functionality
The website would ask each user to create an account. Users can search songs by song name, artists name, and song types, etc. They can also search for albums by songs included, artists name, and album type, etc. And users can have a Favorites to store their favorite songs with other attributes including artists, albums, release dates, etc. Users can freely add and delete songs in Favorites. If users don't have specific preference for songs, they can order the songs and albums by popularity.
## Low Fidelity UI Mockup
<img src="411 project ui.jpg" alt="ui" width="300"/>              <img src="411 ui log in.jpg" alt="ui2" width="300"/>

# Conceptual Design
## UML Diagram
<img src="UML diagram.png" alt="d" width="500"/>

## Description of Assumptions
### Descriptions for Entities
All attributes of "song" are from the data, the primary key is "song_id".

All attributes of "artist" are from the data, the primary key is "artist_id".

All attributes of "album" are from the data, the primary key is "album_id".

For "user", when users create accounts, we will ask for their real first name and last name, and those together form the attribute "name". And also, users can set their "user_name" and "password" when creating accounts. After a user finish creating an account, we will assign that user a "user_id", which is going to be the primary key of "user".

For "plan", we will have several different plans, and they can be differentiated just by their types (different plan type means different plan). And we will set price, duration, and maximum number of favorites for different plans, and user can choose whatever they want and buy that plan.

### Assumptions for Relations
Each "artist" must "write" one or more "songs", and each "song" is "written" by one or more "artists".

Each "user" can have zero or more "favorite songs", and each song is a "favorite song" of zero or more "users".

Each "song" is "contained" in only one "album", each "album" "contains" one or more "songs".

Each "artist" releases zero or more albums, and each "album" only has one "artist".

Each "user" can have zero or more "favorite albums", and each album is a "favorite album" of zero or more "users".
# Logical Design
song(song_id:INT [PK], album_id:INT [FK], song_name:VARCHAR(255), song_popularity:INT, song_type:VARCHAR(255))

artist(artist_id:INT [PK], artist_name:VARCHAR(255), artist_popularity:INT, artist_type:VARCHAR(255), genre:VARCHAR(255))

write((artist_id:INT [FK], song_id:INT [FK]) [PK])

user(user_id:INT [PK], plan_type:VARCHAR(255) [FK], name:VARCHAR(255), user_name:VARCHAR(255), password:VARCHAR(255))

favorite_song((user_id:INT [FK], song_id:INT [FK]) [PK])

album(album_id:INT [PK], artist_id:INT [FK], album_name:VARCHAR(255), album_popularity:INT, album_type:VARCHAR(255))

favorite_album((user_id:INT [FK], album_id:INT [FK]) [PK])

subscription_plan(plan_type:VARCHAR(255) [PK], price:REAL, max_duration: INT, max_favorite:INT)

# Video Link
https://youtu.be/bDWvdMf8rfY
