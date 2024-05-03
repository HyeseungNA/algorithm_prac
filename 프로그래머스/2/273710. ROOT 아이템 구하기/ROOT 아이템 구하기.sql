-- 코드를 작성해주세요
SELECT I.ITEM_ID, ITEM_NAME
FROM ITEM_INFO I
JOIN ITEM_TREE T
ON I.ITEM_ID = T.ITEM_ID
WHERE PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID 