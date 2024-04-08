SELECT gru.student_name, gru.group_name, gra.grade 
FROM grades as gra
inner join (select stud.student_id, stud.student_name, stud.group_id, g.group_name 
			from students as stud  
			inner join "groups" g 
			ON stud.group_id  = g.group_id 
			group by  stud.student_id, stud.student_name, stud.group_id, g.group_name) as gru
on gra.student_id = gru.student_id
where gra.subject_id = 6;