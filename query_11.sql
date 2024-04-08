SELECT t.teacher_name, s.student_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM teachers t
JOIN subjects sub ON t.teacher_id = sub.teacher_id
JOIN grades g ON sub.subject_id = g.subject_id
JOIN students s ON g.student_id = s.student_id
WHERE t.teacher_id = 2 AND s.student_id = 30
GROUP BY t.teacher_name, s.student_name;