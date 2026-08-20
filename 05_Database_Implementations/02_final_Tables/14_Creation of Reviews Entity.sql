-- Create Reviews table

CREATE TABLE Reviews
(
    ReviewID INT NOT NULL,
    CustomerID INT NOT NULL,
    OrderID INT,
    ProductID INT,
    BranchID INT NOT NULL,
    ReviewDate DATE NOT NULL,
    Rating DECIMAL(2,1),
    ReviewText VARCHAR(1000),
    SentimentCategory VARCHAR(20),

    CONSTRAINT PK_Reviews
        PRIMARY KEY (ReviewID),

    CONSTRAINT FK_Reviews_Customers
        FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT FK_Reviews_Orders
        FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID),

    CONSTRAINT FK_Reviews_Products
        FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    CONSTRAINT FK_Reviews_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID),

    CONSTRAINT CHK_Reviews_Rating
        CHECK (Rating BETWEEN 1 AND 5)
);