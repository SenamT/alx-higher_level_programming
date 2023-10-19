-- this will list all the shows contained in hbtn_0d_tvshows that have at least 1 genre linked, and list all rows of database that have 1 column in common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
