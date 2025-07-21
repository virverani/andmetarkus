-- VALIMINE
-- Valime esimesed 10 rida tabeliga tutvumiseks - LIMIT
SELECT * 
FROM SalesTable
LIMIT 10; 

-- Valime konkreetsed tulbad - tulba nimed eraldada komadega
SELECT 
	Date, 
    ProductID, 
    Quantity
FROM 
	SalesTable
LIMIT 10; 

-- Valime unikaalsed väärtused - DISTINCT käsk
SELECT DISTINCT
	ProductID
FROM 
	SalesTable; 

-- FILTREERIMINE - kindlate ridade valimine

-- FILTREERIMINE - KINDEL VÄÄRTUS: Valime kindla toote müügid - WHERE käsk tekstilise välja puhul
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID = 'P001';
    
-- FILTREERIMINE - VÄLISTAMINE: Välistame kindla toote müügid - WHERE käsk tekstilise välja puhul
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID != 'P001';
    
-- FILTREERIMINE - NUMBRLISE VÄÄRTUSE VÕRDLEMINE: Valime ainult müügid, kus kogus on suurem viiest - WHERE käsk numbrilise välja puhul (teised võrdlused: <, <= , >=)
SELECT *
FROM 
	SalesTable
WHERE 
	Quantity > 5;  
    
-- FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid kindlale kliendile - WHERE ning AND
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID = 'P001' 
    AND CustomerID = 'C002';    

-- FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid VÕI kindla kliendi müügid - WHERE ning OR
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID = 'P001' 
    OR CustomerID = 'C002';
    
-- FILTREERIMINE VAHEMIKU ALUSEL: Valime ainult müügid, kus kogus on 5 ja 8 vahepeal - BETWEEN
SELECT *
FROM 
	SalesTable
WHERE 
	Quantity BETWEEN 5 AND 8;  
    
-- FILTREERIMINE - VALIME MITU VÄÄRTUST: Valime mitme kindla toote müügid - IN
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID in ('P001', 'P002', 'P004');
    
-- FILTREERIMINE OSALISE TEKSTI alusel: Valime kõik tooted, mille ID algab 'P00' - LIKE ja % 
SELECT *
FROM 
	SalesTable
WHERE 
	ProductID like 'P00%';

-- FILTREERIMINE - TÕSTUTUNDLIKKUSE EEMALDAMINE: Valime kõik tooted, mille ID algab 'P00' või 'p000' - LOWER või UPPER käsk
SELECT *
FROM 
	SalesTable
WHERE 
	UPPER(ProductID) like 'P00%'; 
    
-- FILTREERIMINE - MITME TINGIMUSE KOMBINEERIMINE: Valime müügid, mis esimese toote puhul on kogusega 2 ja teise toote puhul on kogusega 5 - SULGUDE KASUTAMINE
SELECT *
FROM 
	SalesTable
WHERE 
	(ProductID = 'P001' AND Quantity = 2)
	OR (ProductID = 'P002' AND Quantity = 5);    
    
-- SORTEERIMINE: Sorteerime suurema toote hinnaga müügid ette poole - ORDER BY
SELECT *
FROM 
	SalesTable
ORDER BY
	UnitPrice DESC;
    
-- ALIAS - TULBALE UUS NIMI VÄLJUNDIS: Date tulbast SalesDate tulp väljundis - AS
SELECT Date AS SalesDate
FROM 
	SalesTable;  

/* 
Mitmerealise kommentaari lisamine: 
kui tahad mitu rida kommentaari kirjutada, siis alusta * ja / ning lõpeta * ja /
*/ 
SELECT *
FROM 
	SalesTable
WHERE 
	Quantity > 5;
    
-- ARVUTUSED - võimalik teha aritmeetilisi tehteid (+, -, /, *) tulpade loomiseks, filtreerimiseks ja sorteerimiseks
-- ARVUTUS - Leia müügisummad, kus müügisumma on suurem kui 500 ja järjesta müügisumma alusel kasvavalt
SELECT 
	Quantity, 
    UnitPrice, 
    Discount, 
    Quantity * UnitPrice * (1 - Discount) AS SalesSum
FROM 
	SalesTable
WHERE
	SalesSum > 500
ORDER BY 
	SalesSum ASC;
    
-- AGREGEERIMINE

-- LOENDAMINE: Kui palju müügitehinguid on tehtud? - COUNT
SELECT COUNT (SaleID) AS Tehinguid
FROM 
	SalesTable;
    
-- UNIKAALSETE VÄÄRTUSTE LOENDAMINE: Kui palju eri tooteid on müüdud? - COUNT (DISTINCT)
SELECT 
	COUNT (DISTINCT ProductID) AS 'Eri tooteid'
FROM 
	SalesTable;
    
-- SUMMERIMINE: Kui palju on tooteid müüdud? - SUM
SELECT 
	SUM (Quantity) AS 'Tooteid müüdud'
FROM 
	SalesTable;
    
-- KESKMINE, MIINIMUM, MAKSIMUM: Mis on toodete keskmine, minimaalne ja maksimaalne hind? - AVG, MIN, MAX
SELECT 
	AVG(UnitPrice) AS Average_Price, 
    MIN(UnitPrice) AS Minimum_Price, 
    MAX(UnitPrice) AS Maximum_Price
FROM 
	SalesTable;
    
-- GRUPEERIMINE: Mis on toodete keskmine, minimaalne ja maksimaalne hind toodete kaupa? - GROUP BY
SELECT 
	ProductID,
	AVG(UnitPrice) AS Average_Price, 
    MIN(UnitPrice) AS Minimum_Price, 
    MAX(UnitPrice) AS Maximum_Price
FROM 
	SalesTable
GROUP BY ProductID;

-- AGREGEERTITUD VÄÄRTUSE ALUSEL FILTREERIMINE: Näita ainult tooteid, mille keskmine hind on suurem kui 54.50. - HAVING
SELECT 
	ProductID,
	AVG(UnitPrice) AS Average_Price, 
    MIN(UnitPrice) AS Minimum_Price, 
    MAX(UnitPrice) AS Maximum_Price
FROM 
	SalesTable
GROUP BY ProductID
HAVING Average_Price > 54.5;

-- TÜHI VÄÄRTUS: Näita tooteridu, kus kogus on või ei ole tühi väärtus - IS NULL või IS NOT NULL
SELECT 
Quantity
FROM 
	SalesTable
WHERE Quantity IS NOT NULL;

-- VÄÄRTUSE MUUTMINE: Grupeeri tooted kategooriatesse - CASE WHEN 
SELECT 
ProductID, 
CASE WHEN ProductID = 'P001' THEN 'Category1' 
	 WHEN ProductID = 'P002' THEN 'Category2' 
     ELSE 'Category3' END AS ProductCategory
FROM 
	SalesTable;

-- TABELITE ÜHENDAMINE
-- Kõik read esimesest tabelist ja seotud read teisest tabelist: Kõik eelarveread, seotud müügiesindajad. - LEFT JOIN 
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
LEFT JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena NULL väärtusega müügiesindajate tabelist ID näitab, et müügiesindajate tabelis ei ole antud ID-ga müügiesindajat

-- Kõik read teisest tabelist ja seotud read esimesest tabelist: Kõigi müügiesindajate tabelis olevate müügiesindajate eelarveread - RIGHT JOIN
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
RIGHT JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena NULL väärtusega eelarvetabelist ID näitab, et eelarvetabelis ei ole antud müügiesindajale rida.



-- Read, mis on olemas mõlemas tabelis: Näita ainult ridu, millel on müügiesindajal nii eelarve kui ka väärtus müügiesindajate tabelis. - INNER JOIN 
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
INNER JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena ainult üks rida näitab, et ainult ühel müügiesindajal on olemas eelarve ja müügiesindajate tabelis väärtus.

-- Read, mis on olemas ühes või teises tabelis: Näita kõiki eelarveridu ja kõiki müügiesindajate ridu. - FULL OUTER JOIN 
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
FULL OUTER JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena neli rida näitab, et kokku on kahe tabeli peale ära kirjeldatud nelja erinevad müügiesindaja ID-d.

-- Read, mis on olemas esimeses tabelis ja teises ei ole: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - LEFT JOIN ja IS NULL
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
LEFT JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Rep.SalesRepID IS NULL;
-- Saame ühe müügiesindajaID, kes on eelarve tabelis, aga müügiesindajate tabelis pole.

-- Read, mida pole esimeses tabelis, aga on teises tabelis: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - RIGHT JOIN ja IS NULL
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
RIGHT JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Budget.SalesRepID IS NULL;
-- Saame kaks müügiesindajat, kellel pole eelarveridu.
   
-- Read, mis on puudu ühest või teisest tabelis: Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida. - FULL OUTER JOIN, IS NULL ja OR 
SELECT
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	BudgetSalesRep AS Budget
FULL OUTER JOIN
	SalesRepTable AS Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Budget.SalesRepID IS NULL OR Rep.SalesRepID IS NULL;
-- Tulemusena kolm rida näitab, et ühest või teisest tabelist on puudu kolmel real andmed. NULL väärtuste järgi näeb, kummast tabelist info puudu on.

-- Rohkem kui kahe tabeli ühendamine: Näita müüke, millel on olemas müügiesindaja eelarve ja müügiesindaja tabelis. - INNER JOIN iga seotava tabeli vahele
SELECT
Sales.Quantity,
Budget.SalesRepID AS BudgetSalesRepID,
Budget.Budget, 
Rep.Name AS SalesRep, 
Rep.SalesRepID AS SalesRepID
FROM 
	SalesTable AS Sales
INNER JOIN 
	BudgetSalesRep AS Budget
ON Sales.SalesRepID = Budget.SalesRepID
INNER JOIN
	SalesRepTable AS Rep
ON Sales.SalesRepID = Rep.SalesRepID;
-- Tulemusena 3964 müügirida näitab, et vaid 3964 müügireal on olemas SalesRepID vaste nii eelarve kui ka müügiesindaja tabelis.


-- ALAMPÄRINGUD - viide teisele päringule: Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?
SELECT 
	SalesRep.Name
FROM 
	SalesRepTable as SalesRep
WHERE SalesRep.SalesRepID IN ( 
   SELECT Sales.SalesRepID
   FROM 
		SalesTable AS Sales
   GROUP BY 
   	Sales.SalesRepID
   HAVING
   	AVG(Sales.Discount) > 0.075); 



-- AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): : Millised töötajad on keskmiselt andnud allahindlust üle 7,5% ja kui suur on keskmine antud allahindlus?
WITH SalesRepDiscount AS (
	SELECT 
  	 	Sales.SalesRepID, 
  	 	AVG(Sales.Discount) AS AverageDiscount
	FROM 
		SalesTable AS Sales
	GROUP BY 
   	Sales.SalesRepID
	HAVING
   	AverageDiscount > 0.075)
	
SELECT 
	SalesRep.Name, 
    SalesRepDiscount.AverageDiscount
FROM 
	SalesRepTable as SalesRep
INNER JOIN
	SalesRepDiscount on SalesRep.SalesRepID = SalesRepDiscount.SalesRepID;
    
-- TABELITE KOMBINEERIMINE
-- Leia tabelite pealt unikaalsed väärtused: Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat -- UNION
-- UNION jaoks on vaja valida sama palju ja sama tüüpi tulbad tabelitest.
SELECT CustomerID
FROM SalesTable
WHERE Date >= '2025-01-01'
UNION
SELECT CustomerID
FROM SalesTable
WHERE Date < '2021-01-01';


-- Leia kõik väärtused mitmest tabelist: Leia kõik müügid 2025. aastal või enne 2021. aastat -- UNION ALL
-- UNION ALL jaoks on vaja valida sama palju ja sama tüüpi tulbad tabelitest.
SELECT SaleID, CustomerID
FROM SalesTable
WHERE Date >= '2025-01-01'
UNION
SELECT SaleID, CustomerID
FROM SalesTable
WHERE Date < '2021-01-01';


-- Rohkem funktsioone ja SQL keelte eripärad leiad: https://www.w3schools.com/sql/
    

       
    