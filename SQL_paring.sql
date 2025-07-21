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

-- TABELITE ÜHENDAMINE
-- Kõik read esimesest tabelist ja seotud read teisest tabelist: Kõik eelarveread, seotud müügiesindajad. - LEFT JOIN 
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
LEFT JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena NULL väärtusega müügiesindajate tabelist ID näitab, et müügiesindajate tabelis ei ole antud ID-ga müügiesindajat

-- Kõik read teisest tabelist ja seotud read esimesest tabelist: Kõigi müügiesindajate tabelis olevate müügiesindajate eelarveread - RIGHT JOIN
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
RIGHT JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena NULL väärtusega eelarvetabelist ID näitab, et eelarvetabelis ei ole antud müügiesindajale rida.



-- Read, mis on olemas mõlemas tabelis: Näita ainult ridu, millel on müügiesindajal nii eelarve kui ka väärtus müügiesindajate tabelis. - INNER JOIN 
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
INNER JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena ainult üks rida näitab, et ainult ühel müügiesindajal on olemas eelarve ja müügiesindajate tabelis väärtus.

-- Read, mis on olemas ühes või teises tabelis: Näita kõiki eelarveridu ja kõiki müügiesindajate ridu. - FULL OUTER JOIN 
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
FULL OUTER JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID;
-- Tulemusena neli rida näitab, et kokku on kahe tabeli peale ära kirjeldatud nelja erinevad müügiesindaja ID-d.

-- Read, mis on olemas esimeses tabelis ja teises ei ole: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - LEFT JOIN ja IS NULL
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
LEFT JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Rep.SalesRepID is null;
-- Saame ühe müügiesindajaID, kes on eelarve tabelis, aga müügiesindajate tabelis pole.

-- Read, mida pole esimeses tabelis, aga on teises tabelis: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - RIGHT JOIN ja IS NULL
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
RIGHT JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Budget.SalesRepID is null;
-- Saame kaks müügiesindajat, kellel pole eelarveridu.
   
-- Read, mis on puudu ühest või teisest tabelis: Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida. - FULL OUTER JOIN, IS NULL ja OR 
SELECT
Budget.SalesRepID as BudgetSalesRepID,
Budget.Budget, 
Rep.Name as SalesRep, 
Rep.SalesRepID as SalesRepID
FROM 
	BudgetSalesRep as Budget
FULL OUTER JOIN
	SalesRepTable as Rep
ON Budget.SalesRepID = Rep.SalesRepID
WHERE 
	Budget.SalesRepID is null OR Rep.SalesRepID is null;
-- Tulemusena kolm rida näitab, et ühest või teisest tabelist on puudu kolmel real andmed. NULL väärtuste järgi näeb, kummast tabelist info puudu on.



    

       
    