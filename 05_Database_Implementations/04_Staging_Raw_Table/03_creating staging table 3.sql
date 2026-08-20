-- Refunds
CREATE TABLE Staging.Refunds_Raw
(
    RefundID VARCHAR(20),
    OrderID VARCHAR(20),
    RefundDate VARCHAR(30),
    RefundAmount VARCHAR(30),
    RefundReason VARCHAR(100),
    RefundStatus VARCHAR(30)
);