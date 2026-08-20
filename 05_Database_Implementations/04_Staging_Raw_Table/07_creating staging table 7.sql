-- Deliveries
CREATE TABLE Staging.Deliveries_Raw
(
    DeliveryID VARCHAR(20),
    OrderID VARCHAR(20),
    DeliveryPartner VARCHAR(50),
    DeliveryDistanceKM VARCHAR(30),
    OrderReadyTime VARCHAR(30),
    DeliveryPickupTime VARCHAR(30),
    DeliveryTime VARCHAR(30),
    DeliveryStatus VARCHAR(30),
    DeliveryFee VARCHAR(30)
);