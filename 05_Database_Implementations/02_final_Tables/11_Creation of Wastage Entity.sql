-- Create Wastage table

CREATE TABLE Wastage
(
    WastageID INT NOT NULL,
    BranchID INT NOT NULL,
    IngredientID INT NOT NULL,
    WastageDate DATE NOT NULL,
    WastageQuantity DECIMAL(12,2) NOT NULL,
    WastageReason VARCHAR(100) NOT NULL,
    EstimatedWastageCost DECIMAL(12,2) NOT NULL,

    CONSTRAINT PK_Wastage
        PRIMARY KEY (WastageID),

    CONSTRAINT FK_Wastage_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID),

    CONSTRAINT FK_Wastage_Ingredients
        FOREIGN KEY (IngredientID)
        REFERENCES Ingredients(IngredientID)
);