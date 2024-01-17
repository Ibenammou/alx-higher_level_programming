-- script that lists all shows contained in database

--Use the database
USE hbtn_0d_tvshows;

-- Select all shows with at least one linked genre
SELECT tv_shows.title, tv_show_genres.genre.id
FROM tv_shows.title
INNER JOIN tv_show_genres.genre_id ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
