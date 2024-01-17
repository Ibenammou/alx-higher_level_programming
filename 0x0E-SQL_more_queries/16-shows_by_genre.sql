-- Script that list all shows and genres linked to database

USE hbtn_0d_tv_shows;

SELECT tv_shows.title, tv_genre.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
