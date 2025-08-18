-- Leia müügisummad toodete kaupa​
SELECT
    p.productname,
    SUM(s.quantity * s.unitprice * (1- s.discount)) AS total_sales
FROM 
    salestable AS S
LEFT JOIN 
    producttable AS P ON s.productid = p.productid
GROUP BY 
    p.productname;

-- Leia müügisummad klientide kaupa​
SELECT
    c.customername,
    SUM(s.quantity * s.unitprice * (1- s.discount)) AS total_sales
FROM 
    salestable AS S
LEFT JOIN 
    customertable AS C ON s.customerid = c.customerid
GROUP BY 
    c.customername;

-- Leia müügisummad müügiesindajate kaupa​
SELECT
    sr."Name",
    SUM(s.quantity * s.unitprice * (1- s.discount)) AS total_sales
FROM 
    salestable AS S
LEFT JOIN 
    salesreptable AS sr ON s.salesrepid = sr.salesrepid
GROUP BY 
    sr."Name";

-- Leia müügisummad aastate kaupa​
SELECT
    DATE_PART('year', s."Date"),
    SUM(s.quantity * s.unitprice * (1- s.discount)) AS total_sales
FROM 
    salestable AS S
GROUP BY 
    DATE_PART('year', s."Date")
ORDER BY 
    DATE_PART('year', s."Date") ASC;

-- Lisa müükidele müügisumma kategooriad
SELECT
    s.saleid,
    s.quantity * s.unitprice * (1- s.discount) AS total_sales,
    CASE 
        WHEN s.quantity * s.unitprice * (1- s.discount) < 250 THEN 'Small Sale'
        WHEN s.quantity * s.unitprice * (1- s.discount) BETWEEN 250 AND 500 THEN 'Medium Sale'
        ELSE 'Large Sale'
    END AS sales_category
FROM 
    salestable AS S;

-- Leia müügid müügisumma kategooriate kaupa
WITH sales_category AS (
    SELECT
        s.saleid,
        s.quantity * s.unitprice * (1 - s.discount) AS total_sales,
        CASE 
            WHEN s.quantity * s.unitprice * (1 - s.discount) < 250 THEN 'Small Sale'
            WHEN s.quantity * s.unitprice * (1 - s.discount) BETWEEN 250 AND 500 THEN 'Medium Sale'
            ELSE 'Large Sale'
        END AS sales_category
    FROM salestable AS s
)
SELECT sales_category,
       COUNT(*) AS number_of_sales,
       SUM(total_sales) AS total_sales_amount
FROM sales_category
GROUP BY sales_category;
