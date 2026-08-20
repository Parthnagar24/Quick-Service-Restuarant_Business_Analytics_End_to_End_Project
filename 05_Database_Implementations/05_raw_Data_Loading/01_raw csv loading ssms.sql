SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'Staging'
ORDER BY TABLE_NAME;


BULK INSERT Staging.Branches_Raw
FROM 'C:\01_Structured-Query-Language-Projects\Quick Service Restuarant Business Analytics Project\02_Data_Collection_Quality\02_Raw_Data\raw_data\Branches.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


SELECT TOP 10 *
FROM Staging.Branches_Raw;

SELECT COUNT(*) AS TotalRows
FROM Staging.Branches_Raw;



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


