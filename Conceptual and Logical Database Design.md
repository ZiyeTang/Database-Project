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

