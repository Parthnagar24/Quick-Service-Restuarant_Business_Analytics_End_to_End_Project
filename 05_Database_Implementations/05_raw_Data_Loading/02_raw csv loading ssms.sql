-- =====================================================
-- QSR ANALYTICS
-- BULK INSERT ALL REMAINING RAW DATA INTO STAGING TABLES
-- =====================================================


-- 1. CUSTOMERS

BULK INSERT Staging.Customers_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Customers.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 2. EMPLOYEES

BULK INSERT Staging.Employees_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Employees.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 3. PRODUCTS

BULK INSERT Staging.Products_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Products.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 4. INGREDIENTS

BULK INSERT Staging.Ingredients_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Ingredients.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 5. PRODUCT INGREDIENTS

BULK INSERT Staging.ProductIngredients_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\ProductIngredients.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 6. ORDERS

BULK INSERT Staging.Orders_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Orders.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 7. ORDER DETAILS

BULK INSERT Staging.OrderDetails_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\OrderDetails.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 8. DELIVERIES

BULK INSERT Staging.Deliveries_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Deliveries.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 9. INVENTORY

BULK INSERT Staging.Inventory_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Inventory.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 10. WASTAGE

BULK INSERT Staging.Wastage_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Wastage.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 11. OPERATING COSTS

BULK INSERT Staging.OperatingCosts_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\OperatingCosts.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 12. REFUNDS

BULK INSERT Staging.Refunds_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Refunds.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 13. REVIEWS

BULK INSERT Staging.Reviews_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Reviews.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 14. FOOD SAFETY INSPECTIONS

BULK INSERT Staging.FoodSafetyInspections_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\FoodSafetyInspections.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);