create database provabd;
use provabd;


/*questão 1*/
create table medico(
	id_medico integer (6) not null auto_increment,
    nome char (60) not null,
    crm char (60) not null,
    data_entrada date,
    ativo boolean,
    primary key (id_medico)
);

create table paciente (
	id_paciente integer (6) not null auto_increment,
    nome char (60) not null,
    CNS char (60) not null,
    cpf char (60) not null,
    ativo boolean,
    primary key (id_paciente)
);

create table atende (
	id_atende integer (6) not null auto_increment,
    id_medico integer (6) not null,
    id_paciente integer (6) not null,
    primary key (id_atende),
    foreign key (id_medico) references medico (id_medico),
    foreign key (id_paciente) references paciente (id_paciente)
);

create table leito (
	id_leito integer (6) not null auto_increment,
	nome char (60) not null,
	portaria char (60) not null,
    ativo boolean,
    id_paciente integer (6) not null,
    primary key (id_leito),
    foreign key (id_paciente) references paciente (id_paciente)
);

create table setor (
	id_setor integer (6) not null auto_increment,
	nome char (60) not null,
    ativo boolean,
    id_leito integer (6),
    primary key (id_setor),
    foreign key (id_leito) references leito (id_leito)
);


/*questão 2*/
insert into medico (nome, crm, data_entrada, ativo) values 
('Rafael', '1', '2022-08-15', 1),
('Kim', '2', '2021-10-10', 0),
('Tiago', '3', '2018-01-10', 1),
('Cris', '4', '2020-05-05', 0);
select * from medico;

insert into paciente (nome, CNS, cpf, ativo) values
('Luffy', '123', '012.852.465-85','1'),
('Zoro', '456', '045.654.459-25','1'),
('Nami', '789', '159.357.456-46','0'),
('Sanji', '159', '654.987.321-73','1');
select * from paciente;

insert into atende (id_medico, id_paciente) values (1,1), (2,2), (3,3), (4,4);
select * from atende;

insert into leito(nome, portaria, ativo, id_paciente) values 
('AA','Sala Vermelha', 1, 1),
('BB','Sala Amarelha', 0, 2),
('CC','Sala Branca', 1, 3),
('DD','Sala Azul', 1, 4);
select * from leito;

insert into setor (nome, ativo, id_leito) values 
('Enfermaria', 1, 1),
('Cirurgia', 1, 2),
('Espera', 1 ,3),
('Consulta', 1, 4);
select * from setor;


/*questão 3*/
update medico 
set	nome = 'Evans', crm = '7', data_entrada = '2023-01-27', ativo = '1' 
where id_medico = '4';
select * from medico;

update paciente
set nome = 'Robi', CNS = '357', cpf = '459.357.951-39', ativo = 1
where id_paciente = 3;
select * from paciente;

update leito
set nome = 'EE', portaria = 'Sala Black', ativo = 0
where id_leito = 4;
select * from leito;

update setor 
set nome = 'Saída', ativo = 1
where id_setor = 4;
select * from setor;


/*questão 4*/
set FOREIGN_KEY_CHECKS = 0;

delete from medico where id_medico = 4;
delete from paciente where id_paciente = 4;
delete from leito where id_leito = 4;
delete from medico where id_setor = 4;

set FOREIGN_KEY_CHECKS = 1;


/*questão 5*/
select *
from
	medico as m
inner join
	atende as a
    on m.id_medico = a.id_medico
inner join
	paciente as p
    on p.id_paciente = a.id_paciente
inner join
	leito as l
	on l.id_paciente = p.id_paciente
inner join
	setor as s
    on s.id_leito = l.id_leito;


/*questão 6*/
select
	s.nome as setor,
	m.nome as medico,
    p.nome as paciente,
    l.nome as leitos    
from 
	medico as m
inner join
	atende as a
    on m.id_medico = a.id_medico
inner join
	paciente as p
    on p.id_paciente = a.id_paciente
inner join
	leito as l
	on l.id_paciente = p.id_paciente
inner join
	setor as s
    on s.id_leito = l.id_leito
where
	m.id_medico = 1
group by
	setor, medico;


/*questão 7*/
select
	m.nome as medico,
    count(m.id_medico) as qtd_atendimento
from
	medico as m
inner join
	atende as a
    on m.id_medico = a.id_medico
inner join
	paciente as p
    on p.id_paciente = a.id_paciente
where
	m.id_medico = 2;
    
    
    
    
    
    
    












