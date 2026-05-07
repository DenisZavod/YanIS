BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "student" (
	"id_student"	INTEGER,
	"surname"	VARCHAR(255),
	"name"	VARCHAR(255),
	"oldname"	VARCHAR(255),
	PRIMARY KEY("id_student" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "university_group" (
	"id_univ_group"	INTEGER,
	"course"	VARCHAR(255),
	"faculty"	VARCHAR(255),
	"number"	VARCHAR(255),
	PRIMARY KEY("id_univ_group" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "student_group" (
	"id_str"	INTEGER,
	"id_student"	INTEGER,
	"id_univ_group"	INTEGER,
	PRIMARY KEY("id_str" AUTOINCREMENT),
	FOREIGN KEY("id_student") REFERENCES "student"("id_student"),
	FOREIGN KEY("id_univ_group") REFERENCES "university_group"("id_univ_group")
);
CREATE TABLE IF NOT EXISTS "discipline" (
	"id_discipline"	INTEGER,
	"name_discipline"	VARCHAR(255),
	PRIMARY KEY("id_discipline" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "control_work" (
	"id_control_work"	INTEGER,
	"name_control_work"	VARCHAR(255),
	"id_discipline"	INTEGER,
	PRIMARY KEY("id_control_work" AUTOINCREMENT),
	FOREIGN KEY("id_discipline") REFERENCES "discipline"("id_discipline")
);
CREATE TABLE IF NOT EXISTS "task" (
	"id_task"	INTEGER,
	"name_task"	VARCHAR(255),
	"mark_task"	VARCHAR(255),
	"id_control_work"	INTEGER,
	PRIMARY KEY("id_task" AUTOINCREMENT),
	FOREIGN KEY("id_control_work") REFERENCES "control_work"("id_control_work")
);
CREATE TABLE IF NOT EXISTS "student_control_work" (
	"id_str"	INTEGER,
	"id_student"	INTEGER,
	"id_task"	INTEGER,
	PRIMARY KEY("id_str" AUTOINCREMENT),
	FOREIGN KEY("id_task") REFERENCES "task"("id_task"),
	FOREIGN KEY("id_student") REFERENCES "student"("id_student")
);
CREATE TABLE IF NOT EXISTS "attendance" (
	"id_attendance"	INTEGER,
	"date_attendance"	DATE,
	"name_discipline"	VARCHAR(255),
	"mark"	VARCHAR(255),
	"id_student"	INTEGER,
	PRIMARY KEY("id_attendance" AUTOINCREMENT),
	FOREIGN KEY("id_student") REFERENCES "student"("id_student")
);
COMMIT;
