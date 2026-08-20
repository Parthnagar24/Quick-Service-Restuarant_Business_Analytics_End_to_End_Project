--create an employee table

CREATE TABLE Employees
(
	EmployeeID INT NOT NULL,
	BranchID INT NOT NULL,
	FirstName VARCHAR(20) NOT NULL,
	MiddleName VARCHAR(20),
	LastName VARCHAR(20),
	GovernmentID VARCHAR(20) UNIQUE,
	Role VARCHAR(20) NOT NULL,
	HireDate DATE NOT NULL,
	Employement_Status VARCHAR(20) NOT NULL,
	ManagerID INT ,
	Salary DECIMAL(10,2) NOT NULL,
	Phone VARCHAR(20) UNIQUE,
	Email VARCHAR(20) UNIQUE,

	CONSTRAINT pk_employees PRIMARY KEY(EmployeeID),

	CONSTRAINT FK_Employees_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID),

    CONSTRAINT FK_Employees_Manager
        FOREIGN KEY (ManagerID)
        REFERENCES Employees(EmployeeID)
)

