-- if email is updated AND CHANGED, resets valid_email
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0  -- the reset
    END IF;
END
;
//

DELIMITER ;
