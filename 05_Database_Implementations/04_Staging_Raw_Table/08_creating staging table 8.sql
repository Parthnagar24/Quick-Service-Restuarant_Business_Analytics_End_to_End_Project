-- Order Details
CREATE TABLE Staging.OrderDetails_Raw
(
    OrderDetailID VARCHAR(20),
    OrderID VARCHAR(20),
    ProductID VARCHAR(20),
    Quantity VARCHAR(20),
    UnitPrice VARCHAR(30),
    DiscountAmount VARCHAR(30),
    FinalAmount VARCHAR(30)
);