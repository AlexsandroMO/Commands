cadernodb 

-- Queries SQL
---------------------------------------------------------------------
--#Encontrar Produto que não aparecem em outra vista
SELECT COL1 FROM TABLEA
WHERE COL1 NOT IN (SELECT COL2 FROM TABLEB)

--#################### EPM ############################

SELECT COL, COUNT(*) FROM TABLEX
GROUP BY COL

SELECT COL1, COL2 FROM TABLEX
GROUP BY COL1, COL2
ORDER BY COL1


select * from tabela
where coluna in ('item1','item2')

#--------------------
SELECT * FROM (SELECT COL1, COUNT(*) QT FROM TABLEX
GROUP BY COL1)
WHERE QT > 4
