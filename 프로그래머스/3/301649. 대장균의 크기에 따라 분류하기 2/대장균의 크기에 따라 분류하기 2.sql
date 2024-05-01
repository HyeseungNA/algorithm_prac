-- 코드를 작성해주세요
-- 퍼센테이지 먼저 계산

WITH PERCENTAGE AS (SELECT ID, PERCENT_RANK() OVER
                   (ORDER BY SIZE_OF_COLONY DESC) AS PER
                    FROM ECOLI_DATA)


SELECT E.ID, CASE WHEN PER <= 0.25 THEN 'CRITICAL'
                WHEN PER <= 0.50 THEN 'HIGH'
                WHEN PER <= 0.75 THEN 'MEDIUM'
                ELSE 'LOW'
            END AS COLONY_NAME

FROM ECOLI_DATA E
JOIN PERCENTAGE P
ON E.ID = P.ID