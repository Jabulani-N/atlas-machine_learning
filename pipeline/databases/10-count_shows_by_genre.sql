-- counts how many shows are in each genre
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- WHERE tv_show_genres.genre_id IS NULL
GROUP BY tv_genres.name;
ORDER BY tv_genres.name;
