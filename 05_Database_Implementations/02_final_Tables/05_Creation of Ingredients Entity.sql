-- Create Ingredients table

CREATE TABLE Ingredients
(
    IngredientID INT NOT NULL,
    IngredientName VARCHAR(100) NOT NULL,
    IngredientCategory VARCHAR(50) NOT NULL,
    UnitOfMeasure VARCHAR(20) NOT NULL,
    ShelfLifeDays INT NOT NULL,

    CONSTRAINT PK_Ingredients PRIMARY KEY (IngredientID),

    CONSTRAINT CHK_Ingredients_ShelfLife
        CHECK (ShelfLifeDays > 0)
);