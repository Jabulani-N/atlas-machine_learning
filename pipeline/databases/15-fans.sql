-- take counrty of origin. sum fans of bands from that country
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
-- ORDER BY nb_fans
;
