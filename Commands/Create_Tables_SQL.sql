-- BANCO DE DADOS
--###################################

-- Criar Tabela		    
CREATE TABLE NomeTable -- IF NOT EXISTS
	(  
	ID INTEGER PRIMARY KEY NOT NULL,
	COL1 VARCHAR(50) NOT NULL,
	COL2 INTEGER NOT NULL,
	COLn DATE NOT NULL
	);

	
-- Inserir dados na Tabela
INSERT INTO NomeTable (ID,COL1,COL2,COLn)
	VALUES (0,'valor1',123,'20/05/2017'),
	VALUES (1,'valor2',125,'20/05/2018'),
	VALUES (2,'valor3',123,'20/05/2019')
	;


-- Alterar dados na Tabela		
UPDATE NomeTable
	SET COL2 = 123
	WHERE ID = 1;

-- Selecionar dados
SELECT * FROM NomeTable;

SELECT * FROM NomeTable
WHERE COL3 = '20/05/2018';

SELECT * FROM NomeTable
WHERE COL2 like '%23%';

/*#######################################
Criar um banco de dados para armazenamento de dados de usuário para uma empresa de RH

Guardar:

Dados Pessoais

Nome
CPF
Genero
Data de Aniversário
Estado Civil
Número do Celular

Dados Endereço

CEP
Nome da rua
Número da Casa
Bairro
Cidade
Estado

Dados Profissionais

Profissão
Educação
Anos de Experiencia
Empresas
Linguas
Habilidades
*/

-- Criar Tabela		    
CREATE TABLE DadosPessoais -- IF NOT EXISTS
	(  
	ID INTEGER PRIMARY KEY NOT NULL,
	NOME VARCHAR(50) NOT NULL,
	CPF VARCHAR(50) NOT NULL,
	Genero VARCHAR(50) NOT NULL,
	DATA_ANIVERSARIO DATE NOT NULL,
	ESTADO_CIVIL VARCHAR(50) NOT NULL,
	NUMERO_CEL DATE NOT NULL,
	);

