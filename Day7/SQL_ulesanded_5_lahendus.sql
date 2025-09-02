-- 10. TABELITE ÜHENDAMINE

-- 10.1. Kõik eelarveread eelarve tabelist ja nendega seotud 
-- müügiesindaja nimi müügiesindajate tabelist.
select *
from budgettable 
left join salesreptable
on budgettable.sales_rep_id = salesreptable.sales_rep_id; 

-- 10.3. Kõik müügiesindajad müügiesindajate tabelist ja nendega seotud 
-- eelarveread eelarve tabelist.
select *
from salesreptable
left join budgettable on salesreptable.sales_rep_id = budgettable.sales_rep_id;

-- 10.4. Näita ainult ridu, millel on müügiesindaja nii eelarve tabelis 
-- kui ka väärtus müügiesindajate tabelis.
select *
from salesreptable r
inner join budgettable b on r.sales_rep_id = b.sales_rep_id;

-- 10.5. Näita kõiki ridu eelarve tabelist ja kõiki ridu müügiesindaja tabelist.
select *
from budgettable 
full outer join salesreptable on budgettable.sales_rep_id = salesreptable.sales_rep_id; 

-- 10.6. Näita ridu eelarve tabelist, millele pole 
-- müügiesindaja tabelis müügiesindajat kirjeldatud.
select *
from budgettable
left join salesreptable  on salesreptable.sales_rep_id = budgettable.sales_rep_id
where salesreptable.sales_rep_id is null;

-- 10.7. Näita ridu müügiesindaja tabelist, millele pole kirjeldatud ridu eelarve tabelis.
select *
from salesreptable srt 
left join budgettable bt on srt.sales_rep_id  = bt.sales_rep_id
where bt.sales_rep_id is null;

-- 10.8. Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida.
select *
from salesreptable 
full outer join budgettable on budgettable.sales_rep_id = salesreptable.sales_rep_id 
where budgettable.sales_rep_id is null or salesreptable.sales_rep_id is null;

-- 10.9. Näita ridu müügitabelist, millel on olemas 
-- müügiesindaja info eelarve ja müügiesindaja tabelis.
select s.*, c.sales_rep_name 
from salestable s 
inner join budgettable b on s.sales_rep_id = b.sales_rep_id
inner join salesreptable c on s.sales_rep_id = c.sales_rep_id;
