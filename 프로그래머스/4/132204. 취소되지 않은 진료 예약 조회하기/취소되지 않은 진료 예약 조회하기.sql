-- 코드를 입력하세요
# SELECT APNT_NO,PT_NAME, P.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
# FROM PATIENT P
# JOIN APPOINTMENT A
# ON P.PT_NO = A.PT_NO
# JOIN DOCTOR D
# ON A.MCDP_CD = D.MCDP_CD
# WHERE APNT_YMD LIKE '2022-04-13%' AND A.MCDP_CD = 'CS' AND APNT_CNCL_YN = 'N'
# ORDER BY APNT_YMD




SELECT APNT_NO, PT_NAME, P.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM PATIENT P
JOIN APPOINTMENT A
ON P.PT_NO = A.PT_NO
JOIN DOCTOR D
ON A.MDDR_ID = D.DR_ID
WHERE APNT_YMD LIKE '2022-04-13%' AND A.MCDP_CD = 'CS' AND APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD