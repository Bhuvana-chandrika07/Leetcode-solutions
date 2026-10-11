# Write your MySQL query statement below
(SELECT name as results FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC , name
LIMIT 1)

UNION ALL

(SELECT title as results FROM MovieRating JOIN Movies USING(movie_id)
WHERE EXTRACT(Year_Month FROM created_at ) = 202002
GROUP BY title
ORDER BY AVG(rating) DESC ,title
LIMIT 1);
