SELECT sub_by_teach.teacher_name, ROUND(AVG(gra.grade), 2) as average_grade
FROM (select sub.subject_id, sub.teacher_id, t.teacher_name
		from subjects as sub
		inner join teachers t 
		on sub.teacher_id = t.teacher_id
		group by sub.teacher_id, sub.subject_id, t.teacher_name) as sub_by_teach
left join grades as gra
on sub_by_teach.subject_id = gra.subject_id 
GROUP BY sub_by_teach.teacher_id, sub_by_teach.teacher_name
order by average_grade;