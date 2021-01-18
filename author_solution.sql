SELECT title FROM Films WHERE duration < 90 AND genre = (SELECT id FROM genres WHERE title='драма')
