-- Create Refunds table

CREATE TABLE Refunds
(
    RefundID INT NOT NULL,
    OrderID INT NOT NULL,
    RefundDate DATE NOT NULL,
    RefundAmount DECIMAL(12,2) NOT NULL,
    RefundReason VARCHAR(100) NOT NULL,
    RefundStatus VARCHAR(30) NOT NULL,

    CONSTRAINT PK_Refunds
        PRIMARY KEY (RefundID),

    CONSTRAINT FK_Refunds_Orders
        FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID)
);