-- Tabela ramo_atividade
INSERT INTO ramo_atividade (cd_ramo, ds_ramo) VALUES
(1, 'Tecnologia'),
(2, 'Alimentação'),
(3, 'Saúde'),
(4, 'Moda'),
(5, 'Construção');
select * from ramo_atividade;

-- Tabela tipo_assinante
INSERT INTO tipo_assinante (cd_tipo, ds_tipo) VALUES
(1, 'Premium'),
(2, 'Regular'),
(3, 'Básico'),
(4, 'VIP'),
(5, 'Premium Plus');
select * from tipo_assinante;

-- Tabela assinante
INSERT INTO assinante (cd_assinante, cd_ramo_atividade, cd_tipo_assinante, nm_assinante) VALUES
(1, 1, 1, 10001),
(2, 2, 2, 10002),
(3, 3, 3, 10003),
(4, 1, 3, 10004),
(5, 2, 1, 10005),
(6, 4, 4, 10006),
(7, 5, 5, 10007),
(8, 4, 5, 10008),
(9, 5, 4, 10009),
(10, 3, 1, 10010);
select * from assinante;

-- Tabela municipio
INSERT INTO municipio (cd_municipio, ds_municipio) VALUES
(1, 'São Paulo'),
(2, 'Rio de Janeiro'),
(3, 'Belo Horizonte'),
(4, 'Curitiba'),
(5, 'Salvador');
select * from municipio;

-- Tabela endereco
INSERT INTO endereco (cd_endereco, cd_municipio, cd_assinante, ds_endereco, complemento, bairro, CEP) VALUES
(1, 1, 1, 'Av. Paulista, 100', 'Apto 501', 'Bela Vista', '01310-000'),
(2, 2, 2, 'Rua Copacabana, 200', 'Casa 2', 'Copacabana', '22050-000'),
(3, 3, 3, 'Av. Amazonas, 300', 'Sala 501', 'Centro', '30180-000'),
(4, 1, 4, 'Rua Augusta, 400', NULL, 'Consolação', '01413-000'),
(5, 2, 5, 'Av. Ipanema, 500', NULL, 'Ipanema', '22410-000'),
(6, 4, 6, 'Rua XV de Novembro, 600', NULL, 'Centro', '80020-000'),
(7, 5, 7, 'Av. Sete de Setembro, 700', 'Apto 1001', 'Barra', '40130-000'),
(8, 4, 8, 'Rua das Flores, 800', 'Sala 200', 'Centro', '80010-000'),
(9, 5, 9, 'Av. Oceânica, 900', NULL, 'Ondina', '40170-000'),
(10, 3, 10, 'Av. Afonso Pena, 1000', NULL, 'Centro', '30130-000');
select * from endereco;

-- Tabela telefone
INSERT INTO telefone (cd_fone, cd_endereco, ddd, n_fone) VALUES
(1, 1, '11', '9999-0001'),
(2, 2, '21', '9999-0002'),
(3, 3, '31', '9999-0003'),
(4, 4, '11', '9999-0004'),
(5, 5, '21', '9999-0005'),
(6, 6, '41', '9999-0006'),
(7, 7, '71', '9999-0007'),
(8, 8, '41', '9999-0008'),
(9, 9, '71', '9999-0009'),
(10, 10, '31', '9999-0010');
select * from telefone;

/*a) Listar os nomes dos assinantes, seguido dos dados do endereço e os telefones correspondentes.*/
select
	a.nm_assinante as nome_assinantes, e.ds_endereco as endereco, 
    e.complemento as complemento, e.bairro as bairro, m.ds_municipio as descricao_municipio,
    e.cep as cep, t.ddd as ddd, t.n_fone as telefone
from
	assinante as a
join
	endereco as e
    on e.cd_assinante = a.cd_assinante
join
	municipio as m
    on m.cd_municipio = e.cd_municipio
join
	telefone as t
    on t.cd_endereco = e.cd_endereco
order by
	nome_assinantes asc;
    
/*b) Listar os nomes dos assinantes, seguido do seu ramo, ordenados por ramo e posteriormente por nome.*/
select
	a.nm_assinante as nome_assinante, r.ds_ramo as ramo
from 
	assinante as a
join
	ramo_atividade as r
    on r.cd_ramo = a.cd_ramo_atividade
order by
	ramo, nome_assinante;
    
/*c) Listar os assinantes do município de Pelotas que são do tipo residencial.*/
select
	a.nm_assinante as nome_assinante, m.ds_municipio as municipio, tip.ds_tipo as tipo
from
	assinante as a
join
	endereco as e
    on e.cd_assinante = a.cd_assinante
join
	municipio as m
	on m.cd_municipio = e.cd_municipio
join
	tipo_assinante as tip
    on tip.cd_tipo = a.cd_tipo_assinante
where
	tip.ds_tipo = 'Residencial' and m.ds_municipio = 'Pelotas';

/*d) Listar os nomes dos assinantes que possuem mais de um telefone.*/
select
	a.nm_assinante as nome_assinante, count(t.cd_endereco) as qtd_telefone
from
	assinante as a
join
	endereco as e
    on e.cd_assinante = a.cd_assinante
join
	telefone as t
    on t.cd_endereco = e.cd_endereco
group by
	a.nm_assinante
having
	count(t.cd_endereco) >1
order by
	a.nm_assinante;

/*Listar os nomes dos assinantes seguido do número do telefone, tipo de assinante comercial, com endereço em Natal ou João Câmara.*/
SELECT 
	a.nm_assinante as assinante, t.n_fone as telefone, ta.ds_tipo as Tipo
FROM 	
	assinante as a
INNER JOIN 
	endereco as e 
	ON a.cd_assinante = e.cd_assinante
INNER JOIN 
	municipio as m 
    ON e.cd_municipio = m.cd_municipio
INNER JOIN 
	telefone as t 
    ON e.cd_endereco = t.cd_endereco
INNER JOIN 
	tipo_assinante as ta 
    ON a.cd_tipo_assinante = ta.cd_tipo
WHERE 
	m.ds_municipio = 'Natal' or m.ds_municipio = 'João Câmara' 
    AND ta.ds_tipo = 'Comercial';





