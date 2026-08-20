--create a product table

CREATE TABLE Products 
(
	ProductID INT NOT NULL,
	ProductName VARCHAR(20) NOT NULL,
	Category VARCHAR(20) NOT NULL,
	ProductType VARCHAR(50) NOT NULL,
	CostPrice DECIMAL(10,2) NOT NULL
        CHECK (CostPrice >= 0),

    SellingPrice DECIMAL(10,2) NOT NULL
        CHECK (SellingPrice >= 0),

    ProductStatus VARCHAR(20) NOT NULL
        CHECK (ProductStatus IN ('Active', 'Inactive', 'Discontinued')),
	
	Launch_Date DATE NOT NULL,

	CONSTRAINT pk_products PRIMARY KEY(ProductID)

)