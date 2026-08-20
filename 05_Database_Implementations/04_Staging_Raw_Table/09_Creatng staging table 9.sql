-- Orders
CREATE TABLE Staging.Orders_Raw
(
    OrderID VARCHAR(20),
    CustomerID VARCHAR(20),
    BranchID VARCHAR(20),
    EmployeeID VARCHAR(20),
    OrderDate VARCHAR(30),
    OrderTime VARCHAR(30),
    OrderType VARCHAR(30),
    OrderStatus VARCHAR(30),
    Subtotal VARCHAR(30),
    DiscountAmount VARCHAR(30),
    TaxAmount VARCHAR(30),
    TotalAmount VARCHAR(30),
    PaymentMode VARCHAR(30)
);