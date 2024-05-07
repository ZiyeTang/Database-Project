# Project Report
1\. <br/>
The main direction of our project is almost the same as our proposal. Our application enables users to search songs s by song name, artist name, and album name as intended. We have incorporated a recommendation system as intended. 
And we successfully built a Favorite Song List for each user to add their own favorite songs and also make changes or delete. <br/><br/>

2\. <br/>
What we achieved: <br/>
1. Create account and login.<br/>
2. List all songs and search songs by key words from song name, artist name, and album name. <br/>
3. Show most popular artists in certain genre and return those artists' name, genres, and albums. <br/>
4. Show albums with more than 5 songs.<br/>
5. Built Favorite Song List for users to insert, update and delete.<br/>
6. Offer the user recommendations from other users each time the user add a new favorite song.<br/>

What we failed to achive: <br/>
1. Order songs by popularity.
2. Search only by specific area. For example, searching songs only by certain artist. Our search function is too general: as long as the key word appears in song name, 
artist name, or album name, that record can be returned.
3. Subscription plans.
4. Implementing login constraints.
<br/><br/>

3\.<br/>
We didn't change the source of data but we removed some unimportant properties for each table. Some minor changes have been incorporated in the schema as per the data available and real world application. Initially a many to many relationship was proposed between song and artist but was modified to a many to one relationship due to data constraints. <br/><br/>

4\.<br/>
We removed all foriegn keys and instead created indeces for those former foreign keys because we always got some key constraints when we wanted to make some changes 
to our database like deleting from table or creating new tables. We removed "album_type" attribute from album cause we found that it causes error when doing query. <br/><br/>

5\.<br/>
We added recommendations from other users cause we thougt it's a useful funcionality and it's well suited for procedure and trigger.
We added a query to only show albums with more than 5 songs cause we found that some albums only have a few songs in data.
We removed the functionality to search by song type because there are only two song types, "Solo" and "Collaboration" and most songs are "Solo".
We removed functionality for subscription plan because we have no idea how that work, and also we do not have time for that.<br/><br/>

6\.<br/>
Advanced database program can show data with complicated constraints. And it can also help calculate new data. For example, our album popularity is calculated by the
average of song popularity. When it comes to the recommendation advanced database program, the stored procedure and trigger work nicely together to give users songs they are likely to enjoy, along with ensuring that those recommendations are removed from the list when they add a song to their favorite songs list. The advanced database program complements one's favorite list well through these recommendations allowing the list to grow as they discover new music. <br/><br/>

7\.<br/>
Ziye Tang: <br/>
When trying to exucute sql command in python with "like" in "where" clause, we should put "%s" after "like" in the sql command string and 
put the actual argument in a list. And we can use the string and the argument list as two arguments for execute(). By doing this the error cause by "%" character 
used in "like" can be solved. <br/>

Sam Krauter: <br/>
When first creating the tables to import our data into, we faced many issues such as foreign key dependencies making inserting some data difficult, finding out that  data had a blank character at the end which we could not see but made joining difficult, and some data being present in one dataset we were taking from, but not another. Being flexible with these discoveries by restructuring our database and choosing what data we wanted to include was essential to making the database function in the way we imagined it would. The first draft may not have been perfect, but the database worked well in the end.
<br/><br/>
Prerna Rathi: <br/>
It took time to understand how flask works and integrating html, jquery, python and GCP together was difficult initially. In particular, implementing user input based search was initially problematic, but we improved over time. Using a separate URL for each search helped resolve the several issues. We were unable to update our database without the user entering his/her user id everytime. The use of modal also made the update and create tasks easier.

8\.<br/>
No.<br/><br/>

9\.<br/>
The login system can be made more secure so no matter what page the user directly go to, he/she would be asked for username and password to login. Also, Once the login is complete the user should not be asked to enter userid for updating his list. 
The "Recommendations from other users" functionality can be improved, so that it doesn't show one less recommendation.<br/><br/>

10\.<br/>
Ziye Tang: <br/>
Front end: UI for login, create account, song list, popular artists, albums.<br/>
Database: create table, import data, implement one advanced query for album, query for searching songs by keywords, create indeces for former forign keys.<br/>
Python Flask: functions for searching songs, displaying songs, displaying result for two advanced queries, login and create account.<br/>

Sam Krauter: <br/>
Front end: UI for "Recommendation from other users"
Database: Transform raw data, create table, import data, procedure+trigger for recommendation functionality.<br/>
Python Flask: add the "Recommendation from other users" functionality.<br/>

Prerna Rathi: <br/>
Front end: UI for favorite song list.<br/>
Database: create table, import data, implement one advanced query for popular artists, create indices for the query, insert, update, and delete favorite_song table.<br/>
Python Flask: functions for displaying, inserting, updating and deleting favorite songs according to the entered userid.
