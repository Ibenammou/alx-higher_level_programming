-- Script that list all shows without genre Comedy

USE hbtn_Od_tvshows;

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT tv_show_genres.tv_show_id
	FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
