create table professores (
	id integer(6) not null auto_increment primary key,
    nome varchar(64),
    titulacao varchar (64)
);

create table bolsas (
	id integer(6) not null auto_increment primary key,
    categoria varchar(64),
    valor float(6)
);

create table locais (
	id integer(6) not null auto_increment primary key,
    capacitade integer(6)
);

create table alunos (
	id integer(6) not null auto_increment primary key,
    nome varchar(64)
);

create table disciplina (
	id integer(6) not null auto_increment primary key,
    nome varchar(64),
    vagas integer(6),
    id_professores integer(6),
    foreign key (id_professores) references professores(id)
);

create table prerequisito(
	id integer(6) not null auto_increment primary key,
    id_tem_pr integer(6),
    id_e_pr integer(6),
    foreign key (id_tem_pr) references disciplina(id),
    foreign key (id_e_pr) references disciplina(id)
);

create table ocorrencias(
	id integer(6) not null auto_increment primary key,
    dataInicio date,
    dataTermino date,
    id_locais integer(6),
    id_disciplina integer(6),
    foreign key (id_locais) references locais(id),
    foreign key (id_disciplina) references disciplina(id)
);

create table matriculas(
	id integer(6) not null auto_increment primary key,
    mensalidade float(6),
    turno varchar(64),
    id_alunos integer(6),
    id_bolsas integer(6),
    id_disciplina integer(6),
    foreign key (id_alunos) references alunos(id),
    foreign key (id_bolsas) references bolsas(id),
    foreign key (id_disciplina) references disciplina(id)    
);

