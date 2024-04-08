create table if not exists groups(
group_id smallserial PRIMARY key,
group_name varchar(100) not null);

create table if not exists students(
student_id smallserial primary key,
student_name varchar(100) not null,
group_id smallint references groups(group_id) on delete cascade);

create table if not exists teachers(
teacher_id smallserial primary key,
teacher_name varchar(100) not null);

create table if not exists subjects(
subject_id smallserial primary key,
subject_name varchar(100) not null,
teacher_id smallint references teachers(teacher_id) on delete cascade);

create table if not exists grades(
id smallserial primary key,
student_id smallint references students(student_id) on delete cascade,
teacher_id smallint references teachers(teacher_id) on delete cascade,
grade smallint CHECK (grade >= 0 AND grade <= 100),
grade_date date not null);