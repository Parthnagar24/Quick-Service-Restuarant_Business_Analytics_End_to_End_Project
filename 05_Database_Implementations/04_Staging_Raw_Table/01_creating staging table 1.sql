-- Food Safety Inspections
CREATE TABLE Staging.FoodSafetyInspections_Raw
(
    InspectionID VARCHAR(20),
    BranchID VARCHAR(20),
    InspectionDate VARCHAR(30),
    InspectionType VARCHAR(50),
    InspectionScore VARCHAR(30),
    ComplianceStatus VARCHAR(50),
    ViolationCategory VARCHAR(100),
    ViolationSeverity VARCHAR(30),
    CorrectiveActionStatus VARCHAR(50),
    CorrectiveActionDescription VARCHAR(500)
);