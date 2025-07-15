req_exists_one = """
SELECT
    CASE 
        WHEN EXISTS (
            SELECT 1
            FROM Doctors
            WHERE Surname = 'Smirnov'
        ) THEN 'TRUE'
        ELSE 'FALSE'
    END AS DoctorExists;           
"""

req_exists_two = """
SELECT 
    CASE 
        WHEN EXISTS (
            SELECT 1
            FROM Doctors d 
            JOIN DoctorsExaminations de ON d.id = de.DoctorId
            WHERE d.Surname = 'Smirnov'
        ) THEN 'TRUE'
        ELSE 'FALSE'
    END AS ExaminationExists;
"""

req_any = """ 
SELECT * 
FROM Sponsors 
WHERE id = ANY (
    SELECT SponsorId 
    FROM Donations
    WHERE Amount > 5000000
);
"""

req_some = """
SELECT * 
FROM Examinations 
WHERE id = SOME (
    SELECT ExaminationId 
    FROM DoctorsExaminations 
    WHERE StartTime > '15:00:00'
);
"""

req_all = """
SELECT * 
FROM Wards 
WHERE Places > ALL (
    SELECT Places 
    FROM Wards 
    WHERE Places <= 3
);
"""

req_any_all = """
SELECT *
FROM DoctorsExaminations
WHERE StartTime > ALL (
    SELECT '14:00:00'
)
AND StartTime < ANY (
    SELECT '16:00:00'
);
"""

req_union = """
SELECT Name FROM Doctors 
UNION 
SELECT Name FROM Sponsors;
"""

req_union_all = """
SELECT Name FROM Doctors 
UNION ALL 
SELECT Name FROM Sponsors;
"""

req_inner_join = """
SELECT d.id AS DoctorId, d.Name AS DoctorName, e.Name AS ExaminationName
FROM Doctors d 
INNER JOIN DoctorsExaminations de ON d.id = de.DoctorId 
INNER JOIN Examinations e ON de.ExaminationId = e.id;
"""

req_left_join = """
SELECT d.id AS DoctorId, d.Name AS DoctorName, e.Name AS ExaminationName
FROM Doctors d 
LEFT JOIN DoctorsExaminations de ON d.id = de.DoctorId 
LEFT JOIN Examinations e ON de.ExaminationId = e.id;   
"""

req_right_join = """
SELECT e.id AS ExaminationId, e.Name AS ExaminationName, d.Name AS DoctorName 
FROM Examinations e 
RIGHT JOIN DoctorsExaminations de ON e.id = ExaminationId 
RIGHT JOIN Doctors d ON de.DoctorId = d.Id;
"""

req_left_right_join = """
SELECT s.Name AS SponsorName, d.Name AS DepartmentName 
FROM Sponsors s
LEFT JOIN Donations dn ON s.id = dn.SponsorId 
LEFT JOIN Departments d ON dn.DepartmentId = d.Id

UNION 

SELECT s.Name AS SponsorName, d.Name AS DepartmentName
FROM Departments d 
RIGHT JOIN Donations dn ON d.id = dn.DepartmentId 
RIGHT JOIN Sponsors s ON dn.SponsorId = s.id;
"""

req_full_join = """
SELECT d.Name AS DoctorName, e.Name AS ExaminationName 
FROM Doctors d 
FULL JOIN DoctorsExaminations de ON d.id = de.DoctorId 
FULL JOIN Examinations e ON de.ExaminationId = e.id;
"""
