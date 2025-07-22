```mermaid
erDiagram
    Customers {
        VARCHAR(10) CustomerID PK
        VARCHAR(255) CustomerName
        VARCHAR(100) Industry
        VARCHAR(100) Country
        VARCHAR(10) RegionID FK
    }

    Products {
        VARCHAR(10) ProductID PK
        VARCHAR(255) ProductName
        VARCHAR(100) Category
        DECIMAL(10,2) CostPrice
        VARCHAR(255) Manufacturer
    }

    Regions {
        VARCHAR(10) RegionID PK
        VARCHAR(100) RegionName
        VARCHAR(100) Country
    }

    SalesReps {
        VARCHAR(10) SalesRepID PK
        VARCHAR(255) Name
        VARCHAR(10) RegionID FK
    }

    Dates {
        DATE Date PK
        INT Year
        INT Quarter
        VARCHAR(20) Month
        VARCHAR(20) Weekday
        INT DayOfWeek
    }

    Sales {
        VARCHAR(20) SaleID PK
        DATE Date FK
        VARCHAR(10) CustomerID FK
        VARCHAR(10) ProductID FK
        INT Quantity
        DECIMAL(10,2) UnitPrice
        DECIMAL(4,2) Discount
        VARCHAR(10) SalesRepID FK
        VARCHAR(10) RegionID FK
    }

    Budget {
        DATE Date PK,FK
        VARCHAR(255) SalesRep PK
        DECIMAL(10,2) Budget
    }

    Customers ||--o{ Sales : "has"
    Products ||--o{ Sales : "sold in"
    Regions ||--o{ Customers : "located in"
    Regions ||--o{ SalesReps : "manages"
    SalesReps ||--o{ Sales : "handled by"
    Dates ||--o{ Sales : "on"
    Dates ||--o{ Budget : "for_month"

    %% Note on Budget.SalesRep: This is a weaker link as SalesReps.Name is not a primary key.
    %% For a robust relational design, Budget should ideally use SalesRepID.
    %% This diagram visually represents the direct columns from the CSV.