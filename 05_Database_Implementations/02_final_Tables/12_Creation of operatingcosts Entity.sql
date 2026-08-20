-- Create OperatingCosts table

CREATE TABLE OperatingCosts
(
    CostID INT NOT NULL,
    BranchID INT NOT NULL,
    CostDate DATE NOT NULL,
    CostCategory VARCHAR(50) NOT NULL,
    CostAmount DECIMAL(12,2) NOT NULL,
    Description VARCHAR(255),

    CONSTRAINT PK_OperatingCosts
        PRIMARY KEY (CostID),

    CONSTRAINT FK_OperatingCosts_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID)
);