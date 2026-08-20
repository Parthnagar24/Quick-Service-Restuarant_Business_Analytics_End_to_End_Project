-- Create ProductIngredients table

CREATE TABLE ProductIngredients
(
    ProductID INT NOT NULL,
    IngredientID INT NOT NULL,
    QuantityRequired DECIMAL(10,2) NOT NULL,

    CONSTRAINT PK_ProductIngredients
        PRIMARY KEY (ProductID, IngredientID),

    CONSTRAINT FK_ProductIngredients_Products
        FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    CONSTRAINT FK_ProductIngredients_Ingredients
        FOREIGN KEY (IngredientID)
        REFERENCES Ingredients(IngredientID),

    CONSTRAINT CHK_ProductIngredients_Quantity
        CHECK (QuantityRequired > 0)
);