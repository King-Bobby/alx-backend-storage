-- Creates a procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;

    -- Compute the total score and count of corrections for the user
    SELECT SUM(score) INTO total_score, COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score (with decimal places)
    DECLARE avg_score DECIMAL(10, 2);
    IF total_count > 0 THEN
        SET avg_score = total_score / total_count;
    ELSE
        SET avg_score = 0.0;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
//
DELIMITER ;
