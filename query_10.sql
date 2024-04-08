SELECT s.student_name, t.teacher_name, su.subject_name
FROM students s
JOIN grades gr ON s.student_id = gr.student_id
JOIN subjects su ON gr.subject_id = su.subject_id
JOIN teachers t ON su.teacher_id = t.teacher_id
WHERE s.student_id = 3 AND t.teacher_id = 1