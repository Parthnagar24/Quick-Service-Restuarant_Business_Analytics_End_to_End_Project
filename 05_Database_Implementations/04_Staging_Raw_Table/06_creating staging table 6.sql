-- Inventory
CREATE TABLE Staging.Inventory_Raw
(
    InventoryID VARCHAR(20),
    BranchID VARCHAR(20),
    IngredientID VARCHAR(20),
    StockAuditDate VARCHAR(30),
    OpeningStock VARCHAR(30),
    StockReceived VARCHAR(30),
    StockUsed VARCHAR(30),
    ClosingStock VARCHAR(30),
    ReorderLevel VARCHAR(30),
    ExpiryDate VARCHAR(30)
);
