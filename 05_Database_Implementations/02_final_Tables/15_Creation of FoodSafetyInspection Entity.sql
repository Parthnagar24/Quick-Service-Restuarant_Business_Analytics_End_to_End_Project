-- Create FoodSafetyInspections table

CREATE TABLE FoodSafetyInspections
(
    InspectionID INT NOT NULL,
    BranchID INT NOT NULL,
    InspectionDate DATE NOT NULL,
    InspectionType VARCHAR(50) NOT NULL,
    InspectionScore DECIMAL(5,2),
    ComplianceStatus VARCHAR(30) NOT NULL,
    ViolationCategory VARCHAR(100),
    ViolationSeverity VARCHAR(30),
    CorrectiveActionStatus VARCHAR(30),
    CorrectiveActionDescription VARCHAR(500),

    CONSTRAINT PK_FoodSafetyInspections
        PRIMARY KEY (InspectionID),

    CONSTRAINT FK_FoodSafetyInspections_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID)
);