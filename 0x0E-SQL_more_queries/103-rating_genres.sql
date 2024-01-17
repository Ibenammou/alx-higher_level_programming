-- script to list all genres in database by their rating

USE hbtn_0d_tvshows_rate;

SELECT tv_genres.name, SUM(tv_ratings.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
LEFT JOIN tv_ratings ON tv_shows.id = tv_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
