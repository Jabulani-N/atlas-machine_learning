-- for each row in tv_show_genres,
--  get title  of corresponding id from tv_shows
-- but only where genre = null

SELECT tv_shows.title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
