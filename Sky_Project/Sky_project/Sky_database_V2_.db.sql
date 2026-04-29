BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Contact Channel" (
	"channel_id_PK"	INTEGER,
	"team_id_FK"	INTEGER NOT NULL,
	"type"	TEXT NOT NULL,
	"value"	TEXT NOT NULL,
	PRIMARY KEY("channel_id_PK" AUTOINCREMENT),
	CONSTRAINT "FK_team" FOREIGN KEY("team_id_FK") REFERENCES "Team"("team_id_PK")
);
CREATE TABLE IF NOT EXISTS "Departments" (
	"department_id_PK"	INTEGER,
	" department_admin_user_id_FK"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"department_created_at"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("department_id_PK" AUTOINCREMENT),
	CONSTRAINT " department" FOREIGN KEY(" department_admin_user_id_FK") REFERENCES "User"("user_id_PK")
);
CREATE TABLE IF NOT EXISTS "Engineer" (
	"engineer_id_PK"	INTEGER,
	"full_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"job_title"	TEXT,
	"slack_user_id"	TEXT,
	PRIMARY KEY("engineer_id_PK" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Repository" (
	"repository_id_FK"	INTEGER,
	"team_id_FK"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"repository_type"	TEXT,
	PRIMARY KEY("repository_id_FK" AUTOINCREMENT),
	CONSTRAINT "FK_team_id" FOREIGN KEY("team_id_FK") REFERENCES "Team"("team_id_PK")
);
CREATE TABLE IF NOT EXISTS "Team" (
	"team_id_PK"	INTEGER,
	"department_id_FK"	INTEGER,
	"manager_team_member_id_FK"	INTEGER,
	"Field4"	INTEGER,
	PRIMARY KEY("team_id_PK" AUTOINCREMENT),
	CONSTRAINT "fk_department_id" FOREIGN KEY("department_id_FK") REFERENCES "Departments"("department_id_PK")
);
CREATE TABLE IF NOT EXISTS "Team dependency" (
	"dependency"	INTEGER,
	"team_id_FK"	INTEGER NOT NULL,
	"depends_on_team_id_FK"	INTEGER NOT NULL,
	"dependency_type"	TEXT NOT NULL,
	"team_notes"	TEXT,
	PRIMARY KEY("dependency" AUTOINCREMENT),
	CONSTRAINT "FK_Depends_team_id" FOREIGN KEY("depends_on_team_id_FK") REFERENCES "Team"("team_id_PK"),
	CONSTRAINT "FK_team_id" FOREIGN KEY("team_id_FK") REFERENCES "Team"("team_id_PK")
);
CREATE TABLE IF NOT EXISTS "Team_Member" (
	"team_member_id_PK"	INTEGER,
	"team_id_FK"	INTEGER NOT NULL,
	"engineer_id_FK"	INTEGER NOT NULL,
	"role_in_team"	TEXT,
	"joined_at"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"left_at"	TEXT,
	PRIMARY KEY("team_member_id_PK" AUTOINCREMENT),
	CONSTRAINT "fk_engineer" FOREIGN KEY("engineer_id_FK") REFERENCES "Engineer"("engineer_id_PK"),
	CONSTRAINT "fk_team" FOREIGN KEY("team_id_FK") REFERENCES "Team"("team_id_PK")
);
CREATE TABLE IF NOT EXISTS "User" (
	"user_id_PK"	INTEGER,
	"username"	TEXT NOT NULL UNIQUE,
	"full_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"passowrd"	TEXT NOT NULL,
	"datetime_last_login"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"role"	TEXT NOT NULL CHECK("role" IN ('user', 'admin', 'team_leader', 'engineer')),
	PRIMARY KEY("user_id_PK" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "audit_log" (
	"audit_id_PK"	INTEGER,
	"user_id_FK"	INTEGER NOT NULL,
	"entity_type"	TEXT NOT NULL,
	"entity_id"	INTEGER NOT NULL,
	"changed_at"	TEXT NOT NULL,
	"audit_actions"	TEXT NOT NULL,
	"audit_changed_at"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("audit_id_PK" AUTOINCREMENT),
	CONSTRAINT "user_id_FK" FOREIGN KEY("user_id_FK") REFERENCES "User"("user_id_PK")
);
COMMIT;
