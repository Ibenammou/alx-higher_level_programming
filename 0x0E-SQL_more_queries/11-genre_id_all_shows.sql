-- Script to list all shows contained in a database

-- Use the database
USE hbtn_0d_tvshows;

-- Select all shows with their linked genres or display NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
