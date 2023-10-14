--  creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_count INT;

    -- Calculate the total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the total count of corrections for the user
    SELECT COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate and store the average score for the user
    IF total_count > 0 THEN
        SET @average_score = total_score / total_count;
        UPDATE users SET average_score = @average_score WHERE id = user_id;
    ELSE
        UPDATE users SET average_score = 0 WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;
