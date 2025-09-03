-- Leia müügisummad toodete kaupa​
SELECT
    s.product_id,
    SUM(sales_sum) AS total_sales
FROM 
    salestable AS S
GROUP BY 
    s.product_id
    order by s.product_id;

-- Leia müügisummad klientide kaupa​
SELECT
    s.customer_id,
    SUM(sales_sum) AS total_sales
FROM 
    salestable AS S
GROUP BY 
    s.customer_id
    order by s.customer_id;

-- Leia müügisummad müügiesindajate kaupa​
SELECT
    s.sales_rep_id,
    SUM(sales_sum) AS total_sales
FROM 
    salestable AS S
GROUP BY 
    s.sales_rep_id
    order by s.sales_rep_id;

-- Leia müügisummad aastate kaupa​
SELECT
    TO_CHAR(s.sale_date, 'YYYY') AS sale_year,
    SUM(sales_sum) AS total_sales
FROM 
    salestable AS S
GROUP BY 
   TO_CHAR(s.sale_date, 'YYYY') 
    order by TO_CHAR(s.sale_date, 'YYYY') ;

-- Lisa müükidele müügisumma kategooriad
SELECT
    s.sale_id,
    s.sales_sum AS total_sales,
    CASE 
        WHEN s.sales_sum < 250 THEN 'Small Sale'
        WHEN s.sales_sum BETWEEN 250 AND 500 THEN 'Medium Sale'
        ELSE 'Large Sale'
    END AS sales_category
FROM 
    salestable AS S;

-- Leia müügid müügisumma kategooriate kaupa
WITH sales_category AS (
 SELECT
    s.sale_id,
    s.sales_sum AS total_sales,
    CASE 
        WHEN s.sales_sum < 250 THEN 'Small Sale'
        WHEN s.sales_sum BETWEEN 250 AND 500 THEN 'Medium Sale'
        ELSE 'Large Sale'
    END AS sales_category
FROM 
    salestable AS S
)
SELECT sales_category,
       COUNT(*) AS number_of_sales,
       SUM(total_sales) AS total_sales_amount
FROM sales_category
GROUP BY sales_category;
