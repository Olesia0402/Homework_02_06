select stud.student_id, stud.student_name, stud.group_id, g.group_name 
from students as stud  
inner join "groups" g 
ON stud.group_id  = g.group_id 
where stud.group_id = 2;
