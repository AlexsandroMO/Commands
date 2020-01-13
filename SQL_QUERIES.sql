cadernodb 

-- Queries SQL
---------------------------------------------------------------------
VW_EPM_REPORT_CABLE_CCS
duplicar cadernos no template


-- Juntar 2 tabelas
JOIN LMA_H_INTEGRACAO t2 on t1.id = t2.id_caderno

-- Especificar colunas de retorno
SELECT t2.numero_caderno,t1.IM_PAI FROM LMA_H_INTEGRACAO t1
JOIN caderno t2 on t1.id = t2.id

-- IMZ IR_CONS
select * from
vw_imz_tdpis_ctecons@epm_imz

--#Encontrar Produto que não aparecem em outra vista
SELECT NUMERO FROM CTE
WHERE NUMERO NOT IN (SELECT "cte" FROM V_LIT_INTEGRACAO_TEWEE)

--#################### EPM ############################

-- IMZ MAPA
SELECT * FROM teewe_bde.TAB_INT_CTE_FINAL_MAP@epm_imz

-- IMZ PRODUTO_x_CADERNO
SELECT ATR_COS, ATR_IM, ATR_PR, ATR_CC, ATR_CC_CNX, ATR_MON_STATUS
FROM teewe_bde.TAB_INT_DELNT_PRODXCAD

--#################### EPM ############################

-- IMZ EPM IR 
SELECT ATR_COS_NUMBER, ATR_COS_PRODUCT_VERSION, ATR_COS_DESIGNATION, ATR_RIR_NUMBER, ATR_RIR_DESIGNATION, ATR_PROD_DESIGNATION_01, ATR_PROD_DESIGNATION_02, ATR_PROD_IM_01, ATR_PROD_IM_02
FROM teewe_bde.MV_INT_TDPIS_CTE_P
WHERE ATR_RIR_DESIGNATION like '%F07%' and ATR_COS_DESIGNATION like '%PIPES%'

-- IMZ EPM PL
SELECT ATR_COS_NUMBER, ATR_COS_PRODUCT_VERSION, ATR_COS_DESIGNATION, ATR_RPLOT_NUMBER,ATR_RMP_NUMBER, ATR_RMP_DESIGNATION, ATR_RMP_IM, ATR_ITEM_NUMBER_01,
ATR_RMP_IM, ATR_ITEM_NUMBER, ATR_ITEM_DESIGNATION, ATR_PROD_QTD_PROVIDED
FROM teewe_bde.MV_INT_TDPIS_PL_P

-- IMZ EPM LMA
SELECT LMA_IM_PAI, LMA_IM_FILHO, LMA_RP_FILHO, LMA_CMX, LMA_QUANTIDADE, LMA_DESCRICAO, LMA_PESO, LMA_OBSERVACAO, LMA_UNIDADE, LMA_ELASTOMER, LMA_TORQUE,
LMA_NORDLOCK, ATR_COS, ATR_CC
FROM teewe_bde.VW_EPM_INT_REPORT_CC_LMA

-- IMZ EPM LIT
SELECT LIT_COS_NUM,LIT_COS_REV,LIT_COS_NAME,LIT_CTE_NUM,LIT_CTE_NAME,LIT_PROD_IM,LIT_CTC,LIT_EQP_PAI,ATRCST_ID_CMX,LIT_CC
FROM teewe_bde.VW_EPM_INT_REPORT_CC_LIT

--#################### SIECC ############################

-- IMZ SIECC LIT
SELECT "caderno", "cos", "rev_cos", "cte", "titulo_cte", "equipamento_pai", "status"
FROM V_LIT_INTEGRACAO_TEWEE

-- IMZ SIECC LMA
SELECT CADERNO, STATUS, IM_FILHO, RP_FILHO, CMX, QUANTIDADE, DESCRICAO
FROM V_LMA_INTEGRACAO_TEWEE

-- EPM RAI
select * from teewe_bde.PR_RAI

-- EPM PR_NCR
select * from teewe_bde.PR_NCR

-- EPM RIDA
SELECT NUMERO, PROD, STATUS, COS_CATEGORY, DECRIPTION, CREATED_BY
FROM teewe_bde.PR_RIDA













--#################### SIECC ############################
--SIECC
-- Status Log-TeeWe
select * from V_FLUXO_CADERNO_LOG_TEWEE

-- Status Log
select * from caderno_log

-- Status Log-TeeWe
SELECT ch.numero_caderno as SIEECID, vhist.label as REV_CC, cl.data as DATAACAO, per.descricao as PERFIL, cl.comentario, a.descricao as ACAO, u.nome as AUTOR  FROM caderno_log cl
inner join caderno_hist ch on cl.id_caderno = ch.id
inner join perfil per on cl.id_perfil = per.id
left join acao a on cl.id_acao = a.id
inner join usuario u on cl.id_usuario = u.id
inner join versao vhist on vhist.id = ch.id_versao;



-- buscar por vários itens de uma vez
select * from tabela
where coluna in ('item1','item2')



-- Achar Documento no CC
SELECT CODIGO, REVISAO, DESCRICAO, NUMERO_CADERNO FROM CADERNO
inner join COS cos  on cos.id = caderno.id_cos
where NUMERO_CADERNO = 'CC-319698-80500-11-014'




select NUMERO_CADERNO, DOCUMENTO, REVISAO from CADERNO t1
inner join V_DOCUMENTOS_CADERNO t2 on t1.ID = t2.ID_DOCUMENTO
where NUMERO_CADERNO = 'CC-319698-80500-11-014'


SELECT * FROM CADERNO
inner join COS cos  on cos.id = caderno.id_cos

SELECT CODIGO, REVISAO, DESCRICAO, NUMERO_CADERNO FROM CADERNO
inner join COS cos  on cos.id = caderno.id_cos
where NUMERO_CADERNO = 'CC-319698-80500-11-014'

SELECT CODIGO, REVISAO, DESCRICAO FROM COS


SELECT NUMERO FROM CTE
WHERE NUMERO NOT IN (select "cte" from V_LIT_INTEGRACAO_TEWEE)




-- SIECC Original

CADERNODB.V_LMA_INTEGRACAO_TEWEE@siecc
CADERNODB.V_LIT_INTEGRACAO_TEWEE@siecc 

--#################################


--#Localizar PRs na capa dos cadernos
select * from (
SELECT ID, ID_CADERNO, NUMERO_DOC, REVISAO, PRODUTO FROM CADERNO_DOCUMENTO
WHERE ID_CADERNO in (SELECT ID FROM CADERNO
WHERE NUMERO_CADERNO != '-')
order by ID_CADERNO)
where NUMERO_DOC in 
(
'SMB-TDP-PR-XXXXXXX',
'SMB-TDP-PR-XXXXXXX',
'SMB-TDP-PR-XXXXXXX'
)

--#Select dados cadernos
SELECT ID, TITULO, COMENTARIO_CC, NUMERO_CADERNO FROM CADERNO
WHERE NUMERO_CADERNO != 'x'

--#Select dados Capa dos cadernos
SELECT ID, ID_CADERNO, NUMERO_DOC, REVISAO, PRODUTO FROM CADERNO_DOCUMENTO


-- Localizar caderno por documentos
SELECT NUMERO_CADERNO FROM CADERNO
WHERE ID in (
select ID_CADERNO from (
SELECT ID_CADERNO, NUMERO_DOC, REVISAO, PRODUTO FROM CADERNO_DOCUMENTO
WHERE ID_CADERNO in (SELECT ID FROM CADERNO
WHERE NUMERO_CADERNO != '-'))
where NUMERO_DOC in 
(
'SMB-EQUIPMENT-P0118274'
)
)

select
tabela.*
-- ,col_a || col_b resultado
from
(
select 'a' col_a, 'x' col_b from dual union
select 'b' col_a, 'x' col_b from dual union
select 'c' col_a, 'x' col_b from dual union
select 'a' col_a, 'y' col_b from dual union
select 'b' col_a, 'y' col_b from dual union
select 'c' col_a, 'y' col_b from dual union
select 'a' col_a, 'z' col_b from dual union
select 'b' col_a, 'z' col_b from dual union
select 'c' col_a, 'z' col_b from dual 
) tabela 
where col_a || col_b in ('ay','bz')





--LIT SIECC ORIGINAL
Select
verificador.nome as VERIFICADOR  ,
aprovador.nome as APROVADOR ,
elaborador.nome as ELABORADOR,
DIS.descricao AS disciplina,
Cad.Numero_Caderno caderno, 
Cad.Id As id_caderno, 
Ver.Label versao,
Status.Descricao As status,
Cos.Codigo As cos,
Cos.Revisao As rev_cos,
Cte.Numero As cte, 
Cte.Descricao As titulo_cte,
Cte.CTC As ctc,
Cct.Produto As produto,
Cct.Equipamento As equipamento_pai,
CCT.nota as NOTA 
From Cte Cte
INNER JOIN lit_integracao CCT on CCT.ID_CTE = CTE.ID 
INNER JOIN CADERNO CAD on CAD.ID = CCT.ID_CADERNO
Inner Join Cos Cos On Cos.Id = Cad.Id_Cos
Inner Join Disciplina Dis On Dis.Id = Cos.Id_Disciplina
INNER JOIN submarino SUB on SUB.id = CAD.id_submarino 
Inner Join Versao Ver On Ver.Id = Cad.Id_Versao 
Inner Join Status_Cad Status On Status.Id = Cad.Id_Status
Inner Join Usuario verificador On verificador.Id = Cad.ID_VERIFICADOR 
Inner Join Usuario elaborador On elaborador.Id = Cad.ID_DELEGAR 
Inner Join Usuario aprovador On aprovador.Id = Cad.ID_APROVADOR
where CTE.numero = 'CTE00976524' 



--relacioan caderno e CTE SIECC
SELECT LIT_INTEGRA.id, LIT_INTEGRA.id_caderno, LIT_INTEGRA.id_cte, cte.numero, LIT_INTEGRA.produto FROM LIT_INTEGRACAO LIT_INTEGRA
inner join CTE cte on LIT_INTEGRA.id_cte = cte.id
WHERE LIT_INTEGRA.ID_CADERNO=40743 AND LIT_INTEGRA.TIPO_CADERNO='C' ORDER BY  LIT_INTEGRA.EQUIPAMENTO 



usuário: IMZ_USER
senha: IMZ_2019