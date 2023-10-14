-- Create a stored procedure to update the 'users' table
DELIMITER //
CREATE PROCEDURE UpdateUsersValidEmail(IN userID INT)
BEGIN
    UPDATE users
    SET valid_email = 0
    WHERE id = userID;
END;
//
DELIMITER ;

-- Create the trigger to reset 'valid_email' when 'email' changes
DELIMITER //
CREATE TRIGGER valid_email_reset
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        CALL UpdateUsersValidEmail(NEW.id);
    END IF;
END;
//
DELIMITER ;
