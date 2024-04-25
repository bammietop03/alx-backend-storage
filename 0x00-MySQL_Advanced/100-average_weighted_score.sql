--  a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for a students.

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    			FROM corrections
			INNER JOIN projects
			ON projects.id = corrections.project_id
    			WHERE user_id = user_id)
    WHERE id = user_id;
END //

DELIMITER ;
