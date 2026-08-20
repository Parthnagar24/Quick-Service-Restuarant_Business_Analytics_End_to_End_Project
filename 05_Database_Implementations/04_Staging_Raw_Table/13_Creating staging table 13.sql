-- Employees
CREATE TABLE Staging.Employees_Raw
(
    EmployeeID VARCHAR(20),
    BranchID VARCHAR(20),
    FirstName VARCHAR(50),
    MiddleName VARCHAR(50),
    LastName VARCHAR(50),
    GovernmentID VARCHAR(50),
    Role VARCHAR(50),
    HireDate VARCHAR(30),
    EmploymentStatus VARCHAR(30),
    ManagerID VARCHAR(20),
    Salary VARCHAR(30),
    Phone VARCHAR(30),
    Email VARCHAR(100)
);