-- Operating Costs
CREATE TABLE Staging.OperatingCosts_Raw
(
    CostID VARCHAR(20),
    BranchID VARCHAR(20),
    CostDate VARCHAR(30),
    CostCategory VARCHAR(50),
    CostAmount VARCHAR(30),
    Description VARCHAR(200)
);