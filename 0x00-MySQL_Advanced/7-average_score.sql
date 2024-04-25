-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that 
-- computes and store the average score for a student. An average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average_score_new DECIMAL(10, 2);

	SELECT AVG(score) INTO average_score_new
	FROM corrections
	WHERE user_id = user_id;

	UPDATE users
	SET average_score = average_score_new
	WHERE id = user_id;
END //

DELIMITER ;
