-- 코드를 작성해주세요
SELECT E.EMP_NO, EMP_NAME, 
CASE WHEN AVG(SCORE) >= 96 THEN 'S'
    WHEN AVG(SCORE) >= 90 THEN 'A'
    WHEN AVG(SCORE) >= 80 THEN 'B'
    ELSE 'C'
END AS GRADE,
CASE WHEN AVG(SCORE) >= 96 THEN SAL * 0.2
    WHEN AVG(SCORE) >= 90 THEN SAL * 0.15
    WHEN AVG(SCORE) >= 80 THEN SAL * 0.10
    ELSE SAL * 0
END AS BONUS
FROM HR_EMPLOYEES E
JOIN HR_GRADE G
ON E.EMP_NO = G.EMP_NO
GROUP BY G.EMP_NO
ORDER BY E.EMP_NO

# SELECT
#     e.emp_no,
#     e.emp_name,
#     CASE 
#         WHEN AVG(score) >= 96 THEN 'S'
#         WHEN AVG(score) >= 90 THEN 'A'
#         WHEN AVG(score) >= 80 THEN 'B'
#         ELSE 'C'
#     END AS grade,
#     CASE 
#         WHEN AVG(score) >= 96 THEN e.sal * 0.2
#         WHEN AVG(score) >= 90 THEN e.sal * 0.15
#         WHEN AVG(score) >= 80 THEN e.sal * 0.1
#         ELSE e.sal * 0
#     END AS bonus
# FROM hr_employees e
# JOIN hr_grade g
# ON e.emp_no = g.emp_no
# GROUP BY e.emp_no
# ORDER BY e.emp_no