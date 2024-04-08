SELECT stu.student_name, stu.group_id, gru.group_name, sub.subject_name
FROM students as stu
JOIN grades as gra ON stu.student_id = gra.student_id
JOIN subjects as sub ON gra.subject_id = sub.subject_id
JOIN groups as gru ON stu.group_id = gru.group_id
WHERE stu.student_id = 13;