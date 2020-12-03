CREATE TRIGGER Tir_up_Monitor
	ON Class
	INSTEAD OF UPDATE
AS
	IF UPDATE(Monitor)
		DECLARE @Mon char(7)
		DECLARE @clno CHAR(5)
		SELECT @Mon = Monitor FROM Inserted
		SELECT @clno = Clno FROM Inserted
		IF @Mon IN(SELECT Sno FROM Student WHERE Student.Clno = @clno)
			UPDATE Monitor
			SET Monitor = @Mon