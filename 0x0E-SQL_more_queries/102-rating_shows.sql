-- script to list all shows from the database by their rating

USE hbtn_0d_tvshows_rate;

SELECT tv_shows.title, SUM(tv_ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_ratings ON tv_shows.id = tv_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
