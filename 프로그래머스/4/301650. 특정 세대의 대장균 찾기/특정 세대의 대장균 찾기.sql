-- 코드를 작성해주세요

SELECT F.ID
FROM ECOLI_DATA AS F # 3세대
JOIN ECOLI_DATA AS S # 2세대
ON F.PARENT_ID = S.ID
JOIN ECOLI_DATA AS T  # 1세대
ON S.PARENT_ID = T.ID
WHERE T.PARENT_ID IS NULL
ORDER BY F.ID ASC;