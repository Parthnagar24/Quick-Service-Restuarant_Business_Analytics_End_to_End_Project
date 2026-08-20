-- Create OrderDetails table

CREATE TABLE OrderDetails
(
    OrderDetailID INT NOT NULL,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(12,2) NOT NULL,
    DiscountAmount DECIMAL(12,2) NOT NULL,
    FinalAmount DECIMAL(12,2) NOT NULL,

    CONSTRAINT PK_OrderDetails
        PRIMARY KEY (OrderDetailID),

    CONSTRAINT FK_OrderDetails_Orders
        FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID),

    CONSTRAINT FK_OrderDetails_Products
        FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID)
);