-- TABELI LOOMINE: Loo tabel eelarve jaoks. - CREATE TABLE
CREATE TABLE budget (
    budget_date DATE,
    sales_rep_name VARCHAR (255),
    budget_sum NUMERIC(12,2)
);

-- LISA ANDMED CSV-st: Impordi eelarve CSV. - COPY
COPY budget
FROM 'C:\Users\virve\Documents\Sales Report\Data Sources\BudgetTable.csv'
DELIMITER ';' CSV HEADER;
 
-- SISESTA ANDMED KÄSITSI: Sisesta kaks eelarverida. - INSERT INTO
INSERT INTO budget (
    budget_date,
    sales_rep_name,
    budget_sum)
VALUES ('2026-01-31',
		'Jane Smith',
         20000), 
        ('2026-01-31',
         'John Doe',
         20000) ;

-- TABELI MUUTMINE
-- LISA TULP: Lisa müügiesindaja ID tulp. - ALTER TABLE ja ADD
ALTER TABLE budget
ADD sales_rep_id VARCHAR(255);

-- UUENDA TULBA VÄÄRTUST: Lisa müügiesindajate ID-d. - UPDATE, SET ja WHERE
UPDATE budget
SET sales_rep_id = 'SR01'
WHERE sales_rep_name = 'Jane Smith';

UPDATE budget
SET sales_rep_id = 'SR02' 
WHERE sales_rep_name = 'John Doe';

UPDATE budget
SET sales_rep_id = 'SR03' 
WHERE sales_rep_name = 'Emily Stone';

-- MUUDA TULBA NIME: Lisa täpsustus, et eelarve on eurodes. - ALTER TABLE ja RENAME COLUMN
ALTER TABLE budget
RENAME COLUMN budget_sum TO budget_sum_eur;

-- MUUDA TULBA FORMAATI: Eemalda nime tulbalt pikkuse piirang. - ALTER TABLE ja ALTER COLUMN
ALTER TABLE budget
ALTER COLUMN sales_rep_name TYPE TEXT;

-- KUSTUTA TULP: Eemalda nime tulp. - ALTER TABLE ja DROP COLUMN
ALTER TABLE budget
DROP COLUMN sales_rep_name;

-- KUSTUTA TABEL: Eemalda eelarve tabel. - DROP TABLE
DROP TABLE budget;
