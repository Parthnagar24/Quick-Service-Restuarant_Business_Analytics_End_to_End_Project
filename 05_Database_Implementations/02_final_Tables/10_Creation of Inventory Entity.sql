-- Create Inventory table

CREATE TABLE Inventory
(
    InventoryID INT NOT NULL,
    BranchID INT NOT NULL,
    IngredientID INT NOT NULL,
    StockAuditDate DATE NOT NULL,
    OpeningStock DECIMAL(12,2) NOT NULL,
    StockReceived DECIMAL(12,2) NOT NULL,
    StockUsed DECIMAL(12,2) NOT NULL,
    ClosingStock DECIMAL(12,2) NOT NULL,
    ReorderLevel DECIMAL(12,2) NOT NULL,
    ExpiryDate DATE,

    CONSTRAINT PK_Inventory
        PRIMARY KEY (InventoryID),

    CONSTRAINT FK_Inventory_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID),

    CONSTRAINT FK_Inventory_Ingredients
        FOREIGN KEY (IngredientID)
        REFERENCES Ingredients(IngredientID)
);