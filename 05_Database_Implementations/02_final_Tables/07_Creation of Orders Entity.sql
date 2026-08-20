-- Create Orders table

CREATE TABLE Orders
(
    OrderID INT NOT NULL,
    CustomerID INT NOT NULL,
    BranchID INT NOT NULL,
    EmployeeID INT,
    OrderDate DATE NOT NULL,
    OrderTime TIME NOT NULL,
    OrderType VARCHAR(30) NOT NULL,
    OrderStatus VARCHAR(30) NOT NULL,
    Subtotal DECIMAL(12,2) NOT NULL,
    DiscountAmount DECIMAL(12,2) NOT NULL,
    TaxAmount DECIMAL(12,2) NOT NULL,
    TotalAmount DECIMAL(12,2) NOT NULL,
    PaymentMode VARCHAR(30) NOT NULL,

    CONSTRAINT PK_Orders PRIMARY KEY (OrderID),

    CONSTRAINT FK_Orders_Customers
        FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT FK_Orders_Branches
        FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID),

    CONSTRAINT FK_Orders_Employees
        FOREIGN KEY (EmployeeID)
        REFERENCES Employees(EmployeeID)
);