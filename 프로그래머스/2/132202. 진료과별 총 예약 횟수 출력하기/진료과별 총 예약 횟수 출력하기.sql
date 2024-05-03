-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과코드', COUNT(APNT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY 진료과코드
ORDER BY 5월예약건수, 진료과코드
# GROUP BY, ORDER BY, HAVING 절에 별칭을 쓸 경우, 
# 별칭 그대로 써주거나 백틱 사용
# 안 그럼 별칭에 나온 문자로 인식