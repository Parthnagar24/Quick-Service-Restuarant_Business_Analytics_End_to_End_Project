-- Create Deliveries table

CREATE TABLE Deliveries
(
    DeliveryID INT NOT NULL,
    OrderID INT NOT NULL,
    DeliveryPartner VARCHAR(50),
    DeliveryDistanceKM DECIMAL(10,2),
    OrderReadyTime DATETIME,
    DeliveryPickupTime DATETIME,
    DeliveryTime DATETIME,
    DeliveryStatus VARCHAR(30) NOT NULL,
    DeliveryFee DECIMAL(10,2),

    CONSTRAINT PK_Deliveries
        PRIMARY KEY (DeliveryID),

    CONSTRAINT FK_Deliveries_Orders
        FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID)
);