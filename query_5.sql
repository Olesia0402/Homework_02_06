select s.subject_id, s.subject_name, s.teacher_id, t.teacher_name 
from subjects s 
inner join teachers t
ON s.teacher_id = t.teacher_id
where s.teacher_id = 4;
