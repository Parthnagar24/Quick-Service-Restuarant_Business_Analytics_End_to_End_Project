-- Reviews
CREATE TABLE Staging.Reviews_Raw
(
    ReviewID VARCHAR(20),
    CustomerID VARCHAR(20),
    OrderID VARCHAR(20),
    ProductID VARCHAR(20),
    BranchID VARCHAR(20),
    ReviewDate VARCHAR(30),
    Rating VARCHAR(20),
    ReviewText VARCHAR(500),
    SentimentCategory VARCHAR(30)
);