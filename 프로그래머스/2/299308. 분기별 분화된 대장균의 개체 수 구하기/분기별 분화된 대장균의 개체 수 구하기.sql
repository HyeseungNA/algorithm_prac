-- 코드를 작성해주세요
SELECT 
    CASE WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 01 AND 03 THEN CONCAT(1,'Q')
    WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 04 AND 06 THEN CONCAT(2,'Q')
    WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 07 AND 09 THEN CONCAT(3,'Q')
    ELSE CONCAT(4,'Q')
    END AS QUARTER

,COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER