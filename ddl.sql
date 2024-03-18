create table student
    (student_id			SERIAL, 
     first_name			TEXT not null, 
     last_name			TEXT not null, 
     email				TEXT not null UNIQUE,
	 enrollment_date	DATE,
     primary key (student_id)
    );
