-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	DECLARE project_new INT;

	SELECT id INTO project_new FROM projects WHERE name = project_name;

	IF project_new IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_new = LAST_INSERT_ID();
	END IF;

	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_new, score);

END //
DELIMITER ;
