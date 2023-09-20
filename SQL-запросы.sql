-- №1
SELECT c.login,
	COUNT(o."inDelivery")
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON o."courierId" = c.id
GROUP BY c.login;


-- №2
SELECT track AS track,
	CASE
    	WHEN finished = true THEN 2
		WHEN cancelled = true THEN -1
		WHEN "inDelivery" = true THEN 1
		ELSE 0
	END
FROM "Orders";
