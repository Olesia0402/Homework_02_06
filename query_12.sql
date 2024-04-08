SELECT s.student_name, gr.group_name, su.subject_name, g.grade, g.grade_date 
FROM students s
JOIN groups gr ON s.group_id = gr.group_id
JOIN grades g ON s.student_id = g.student_id
JOIN subjects su ON g.subject_id = su.subject_id
WHERE gr.group_id = 1 AND su.subject_id = 2
ORDER BY g.grade_date DESC;