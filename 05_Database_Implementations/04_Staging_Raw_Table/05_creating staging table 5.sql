-- Wastage
CREATE TABLE Staging.Wastage_Raw
(
    WastageID VARCHAR(20),
    BranchID VARCHAR(20),
    IngredientID VARCHAR(20),
    WastageDate VARCHAR(30),
    WastageQuantity VARCHAR(30),
    WastageReason VARCHAR(100),
    EstimatedWastageCost VARCHAR(30)
);
