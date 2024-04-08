SELECT stud.student_id, stud.student_name, ROUND(AVG(gra.grade), 2) as average_grade
FROM students as stud
left join grades as gra
on stud.student_id = gra.student_id 
where gra.subject_id = 3
GROUP BY stud.student_id 
order by average_grade desc
limit 1;

