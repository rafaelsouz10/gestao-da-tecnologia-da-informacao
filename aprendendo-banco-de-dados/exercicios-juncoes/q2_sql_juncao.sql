create table cliente (
	cpf varchar(60) not null,
    nome varchar(60),
    dtNasc date,
    primary key (cpf)
);

create table modelo (
	codMod integer(6) not null primary key,
    desc_2 varchar(40),
    ano int
);

create table patio (
	num integer(8) not null primary key,
    ender varchar(40),
    capacidade integer (10)
);

create table veiculo (
	placa varchar(8) not null primary key,
    modelo_codMod integer (6),
    cliente_cpf varchar (60) not null,
    cor varchar (20),
    foreign key (modelo_codMod) references modelo (codMod),
	foreign key (cliente_cpf) references cliente (cpf)
);

create table estaciona (
	cod integer(8) not null auto_increment primary key,
    patio_num integer (8),
    veiculo_placa varchar (8),
    dtEntrada varchar (10),
    dtSaida varchar (10),
    hsEntrada varchar (10),
    hsSaida varchar (10),
    foreign key (patio_num) references patio (num),
	foreign key (veiculo_placa) references veiculo (placa)
);

insert into cliente (cpf, nome, dtNasc) values
  ('23456789012', 'Maria Santos', '1985-09-23'),
  ('34567890123', 'Pedro Souza', '1995-02-10'),
  ('45678901234', 'Ana Oliveira', '1992-07-30'),
  ('56789012345', 'Lucas Ferreira', '1988-11-02'),
  ('67890123456', 'Carla Almeida', '1999-03-20'),
  ('78901234567', 'Marcos Pereira', '1993-06-12'),
  ('89012345678', 'Juliana Costa', '1991-08-28'),
  ('90123456789', 'Rafaela Santos', '1997-04-05'),
  ('01234567890', 'Roberto Silva', '1987-12-07');
select * from cliente;

insert into modelo (codMod, desc_2, ano) values
  (1, 'Fiat Uno', 1995),
  (2, 'Volkswagen Golf', 1998),
  (3, 'Ford Focus', 2005),
  (4, 'Chevrolet Vectra', 2003),
  (5, 'Toyota Corolla', 2008),
  (6, 'Honda Accord', 2010),
  (7, 'Renault Clio', 2001),
  (8, 'Hyundai Elantra', 2012),
  (9, 'Nissan Sentra', 2015),
  (10, 'Jeep Wrangler', 2019);
select * from modelo;

INSERT INTO patio (num, ender, capacidade) VALUES
  (1, 'Rua A, 123', 20),
  (2, 'Rua B, 456', 30),
  (3, 'Rua C, 789', 25),
  (4, 'Rua D, 987', 15),
  (5, 'Rua E, 654', 10),
  (6, 'Rua F, 321', 18),
  (7, 'Rua G, 876', 22),
  (8, 'Rua H, 543', 27),
  (9, 'Rua I, 210', 12),
  (10, 'Rua J, 987', 35);
select * from patio;

INSERT INTO veiculo (placa, modelo_codMod, cliente_cpf, cor) VALUES
  ('ABC1234', 1, '12345678901', 'Vermelho'),
  ('DEF5678', 2, '23456789012', 'Branco'),
  ('GHI9012', 3, '34567890123', 'Verde'),
  ('JKL3456', 4, '45678901234', 'Preto'),
  ('MNO7890', 5, '56789012345', 'Vermelho'),
  ('PQR2345', 6, '67890123456', 'Branco'),
  ('STU6789', 7, '78901234567', 'Verde'),
  ('VWX9012', 8, '89012345678', 'Preto'),
  ('YZA3456', 9, '90123456789', 'Vermelho'),
  ('BCD7890', 10, '01234567890', 'Branco');
select * from veiculo;

INSERT INTO estaciona (cod, patio_num, veiculo_placa, dtEntrada, dtSaida, hsEntrada, hsSaida) VALUES
  (1, 1, 'ABC1234', '2023-06-17', '2023-06-17', '09:00:00', '18:00:00'),
  (2, 2, 'DEF5678', '2023-06-17', '2023-06-17', '10:30:00', '17:45:00'),
  (3, 3, 'GHI9012', '2023-06-17', '2023-06-18', '12:15:00', '09:30:00'),
  (4, 4, 'JKL3456', '2023-06-17', '2023-06-18', '14:20:00', '11:40:00'),
  (5, 5, 'MNO7890', '2023-06-17', '2023-06-17', '15:45:00', '19:00:00'),
  (6, 6, 'PQR2345', '2023-06-17', '2023-06-18', '17:00:00', '13:30:00'),
  (7, 7, 'STU6789', '2023-06-17', '2023-06-17', '19:20:00', '22:15:00'),
  (8, 8, 'VWX9012', '2023-06-17', '2023-06-17', '20:10:00', '23:45:00'),
  (9, 9, 'JJJ2020', '2023-06-17', '2023-06-18', '21:30:00', '10:20:00'),
  (10, 10, 'BCD7890', '2023-06-17', '2023-06-18', '22:45:00', '08:15:00'),
  (11, 6, 'JJJ2020', '2023-06-19', '2023-06-20', '23:30:00', '12:20:00');
select * from estaciona;
/*a*/
select
	v.placa as placa, c.nome as cliente
from
	veiculo as v
join
	cliente as c
    on c.cpf = v.cliente_cpf;

/*b*/
select
	c.cpf as cpf, c.nome as cliente, v.placa as placa
from 
	cliente as c
join
	veiculo as v
    on v.cliente_cpf = c.cpf
where
	v.placa = 'JJJ2020';

/*c*/
select
	e.cod as codEstacionamento, v.placa as placa, v.cor as cor
from
	veiculo as v
join
	estaciona as e
    on v.placa = e.veiculo_placa
where
	e.cod = 1;

/*d*/
select
	e.cod as codEstacionamento, v.placa as placa, m.ano as ano
from
	modelo as m
join
	veiculo as v
    on m.codMod = v.Modelo_codMod
join
	estaciona as e
    on v.placa = e.veiculo_placa
where
	e.cod = 1;

/*e*/
select
	v.placa as placa, m.ano as ano, m.desc_2
from
	modelo as m
join
	veiculo as v
    on m.codMod = v.Modelo_codMod
where
	m.ano > 2000;

/*f*/
select
	p.ender as endereço, e.dtEntrada as Data_Entrada, e.dtSaida as Data_Saida, v.placa as placa
from
	patio as p
join	
	estaciona as e
    on p.num = e.patio_num
join
	veiculo as v
    on v.placa = e.veiculo_placa
where 
	v.placa = 'JJJ2020';

/*g*/
select
	v.cor as cor, count(v.cor) as quatidade_verde
from	
	veiculo as v
where
	v.cor = 'verde';

/*h*/
select
	c.nome as Cliente, m.codMod as Modelo, m.desc_2 as Descricao_Modelo
from 
	cliente as c
join
	veiculo as v
    on c.cpf = v.cliente_cpf
join
	modelo as m
    on v.modelo_codMod = m.codMod
where
	m.codMod = '1';

/*i*/
select
	m.desc_2 as Modelo, v.cor as cor, v.placa as Placa, e.hsEntrada as Horario_Entrada, e.hsEntrada as Horario_Saida
from
	estaciona as e
join
	veiculo as v
    on v.placa = e.veiculo_placa
join 
	modelo as m
    on m.codMod = v.modelo_codMod
where 
	v.cor = 'verde';

/*j*/
select
	c.nome as Cliente, m.desc_2 as Modelo, v.placa as placa, p.ender as endereco, e.dtEntrada as Data_Entrada, 
    e.dtSaida as Data_Saida, e.hsEntrada as Horario_Entrada, e.hsEntrada as Horario_Saida
from
	modelo as m
join
	veiculo as v
    on m.codMod = v.modelo_codMod
join
	estaciona as e
    on e.veiculo_placa = v.placa
join
	patio as p
    on p.num = e.patio_num
join
	cliente as c
    on c.cpf = v.cliente_cpf
where
	v.placa = 'JJJ2020';

/*k*/
select
	c.nome as Cliente, e.cod as Codigo_Estacionamento
from
	cliente as c
join
	veiculo as v
    on v.cliente_cpf = c.cpf
join
	estaciona as e
    on v.placa = e.veiculo_placa
where 
	e.cod = 2;
    
/*l*/
select
	c.cpf as CPF, e.cod as Codigo_Estacionamento
from
	cliente as c
join
	veiculo as v
    on v.cliente_cpf = c.cpf
join
	estaciona as e
    on v.placa = e.veiculo_placa
where 
	e.cod = 3;
    
/*m*/
select
	m.desc_2 as Desc_Modelo, e.cod as Codigo_Estacionamento
from
	modelo as m
join
	veiculo as v
    on v.modelo_codMod = m.codMod
join
	estaciona as e
    on v.placa = e.veiculo_placa
where 
	e.cod = 2;

/*m*/
select
	c.nome as Donos, v.placa as placa, m.desc_2 as Desc_Modelo
from
	cliente	as c
join
	veiculo as v
    on v.cliente_cpf = c.cpf
join
	modelo as m
    on v.modelo_codMod = m.codMod
order by
	Donos asc;