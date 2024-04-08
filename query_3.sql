SELECT students_by_group.group_name, subjects.subject_name, ROUND(AVG(gra.grade), 2) as average_grade
FROM grades as gra
INNER JOIN (
    SELECT stud.student_id, stud.student_name, stud.group_id, g.group_name 
    FROM students as stud  
    INNER JOIN "groups" g  
    ON stud.group_id = g.group_id 
) as students_by_group
ON gra.student_id = students_by_group.student_id
INNER JOIN subjects ON gra.subject_id = subjects.subject_id
GROUP BY students_by_group.group_name, subjects.subject_name
ORDER BY average_grade DESC;
