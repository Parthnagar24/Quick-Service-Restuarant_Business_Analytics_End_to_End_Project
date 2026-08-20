--create customers table

CREATE TABLE Customers 
(
	CustomerID INT NOT NULL,
	FirstName VARCHAR(20) NOT NULL,
	MiddleName VARCHAR(20) ,
	LastName VARCHAR(20) ,
	DOB DATE NOT NULL,
	Email VARCHAR(30) UNIQUE,
	Phone VARCHAR(20) UNIQUE,
	JoinDate DATE NOT NULL,
	Gender VARCHAR(10) 
		CHECK (Gender IN ('Male','Female','Transgender')),
	City VARCHAR(20) NOT NULL,
	State VARCHAR(20) NOT NULL,
	Loyalty_Status VARCHAR(20) NOT NULL,

	CONSTRAINT pk_customers PRIMARY KEY(CustomerID)
)