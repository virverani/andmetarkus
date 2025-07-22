```mermaid
erDiagram
    Customers {
        VARCHAR CustomerID PK
        VARCHAR CustomerName
        VARCHAR Industry
        VARCHAR Country
        VARCHAR RegionID FK
    }

    Products {
        VARCHAR ProductID PK
        VARCHAR ProductName
        VARCHAR Category
        DECIMAL CostPrice
        VARCHAR Manufacturer
    }

    Regions {
        VARCHAR RegionID PK
        VARCHAR RegionName
        VARCHAR Country
    }

    SalesReps {
        VARCHAR SalesRepID PK
        VARCHAR Name
        VARCHAR RegionID FK
    }

    Dates {
        DATE Date PK
        INT Year
        INT Quarter
        VARCHAR Month
        VARCHAR Weekday
        INT DayOfWeek
    }

    Sales {
        VARCHAR SaleID PK
        DATE Date FK
        VARCHAR CustomerID FK
        VARCHAR ProductID FK
        INT Quantity
        DECIMAL UnitPrice
        DECIMAL Discount
        VARCHAR SalesRepID FK
        VARCHAR RegionID FK
    }

    Budget {
        DATE Date PK,FK
        VARCHAR SalesRep PK
        DECIMAL Budget
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