--create a branch table

CREATE TABLE Branches 
(
	BranchID INT NOT NULL,
	BranchName VARCHAR(100) NOT NULL,
	City VARCHAR(50) NOT NULL,
	State VARCHAR(50) NOT NULL,
	LocationType VARCHAR(50) NOT NULL,
	Opening_Date DATE,
	Branch_Status VARCHAR(20) NOT NULL
		CHECK (Branch_Status IN ('Active', 'Closed')),
	
	CONSTRAINT pk_branches PRIMARY KEY(BranchID)
)

