--  lists all records with score >= 10 in table second_table
-- score, name associated with it.
-- in order of highest score at top; lowest at bottom.
SELECT score, name
FROM second_table
WHERE score >= 10
-- DESC = descending order
ORDER BY score DESC;
