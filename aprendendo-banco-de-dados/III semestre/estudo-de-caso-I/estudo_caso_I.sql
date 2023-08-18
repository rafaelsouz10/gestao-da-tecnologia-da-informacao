create table editoras(
	id integer(6) not null auto_increment primary key,
    endereco varchar(64),
    nome varchar(64)
);

create table autores (
	id integer(6) not null auto_increment primary key,
    data_nasc date,
    nome varchar(64)    
);

create table cliente(
	id integer(6) not null auto_increment primary key,
    endereco varchar(64),
    nome varchar(64)
);

create table fone(
	id integer(6) not null auto_increment primary key,
    telefone varchar(64),
    id_cliente integer(6),
    foreign key (id_cliente) references cliente(id)
);

create table instituicao_ensino(
	id integer(6) not null auto_increment primary key,
    nome varchar(64)
);

create table categorias(
	id integer(6) not null auto_increment primary key,
    descricao varchar(64)
);

create table livros(
	id integer(6) not null auto_increment primary key,
    ISBN integer(6),
    titulo varchar(64),
    volume integer(6),
    nroPaginas integer(6),
    ano date,
    id_categorias integer(6),
    id_editoras integer(6),
    foreign key (id_categorias) references categorias(id),
    foreign key (id_editoras) references editoras(id)
);

create table autoria (
	id integer(6) not null auto_increment primary key,
    ordem integer(6),
    id_autores integer(6),
    foreign key (id_autores) references autores(id)
);

create table bibliotecarias(
	id integer(6) not null auto_increment primary key,
    nome varchar(64),
    salario float(10),
    cpf varchar (64),
    rg varchar (64)
);

create table estantes(
	id integer(6) not null auto_increment primary key,
    corredor integer(6)
);

create table organizacao(
	id integer(6) not null auto_increment primary key,
    id_categorias integer(6),
    id_estantes integer(6),
    foreign key (id_categorias) references categorias(id),
    foreign key (id_estantes) references estantes(id)
);

create table exemplares(
	id integer(6) not null auto_increment primary key,
    numero integer(6),
    estado varchar (64),
    id_estantes integer(6),
    id_livros integer (6),
    foreign key (id_livros) references livros(id),
    foreign key (id_estantes) references estantes(id)
);

create table emprestimos(
	id integer(6) not null auto_increment primary key,
    data_retirada date,
    data_devolucao date,
    valor_multa float (10),
    id_bibliotecarias integer(6),
    id_exemplares integer(6),
    id_clientes integer(6),
    foreign key (id_bibliotecarias) references bibliotecarias(id),
    foreign key (id_exemplares) references exemplares(id),
    foreign key (id_clientes) references clientes(id)
);

create table efetivas(
	id integer(6) not null auto_increment primary key,
    data_admissao date,
    id_bibliotecarias integer(6),
    foreign key (id_bibliotecarias) references bibliotecarias(id)
);

create table estagiarios(
	id integer(6) not null auto_increment primary key,
    id_bibliotecarias integer(6),
    id_efetivas integer(6),
    id_instituicoes_ensino integer(6),
    foreign key (id_bibliotecarias) references bibliotecarias(id),
    foreign key (id_efetivas) references efetivas(id),
    foreign key (id_instituicoes_ensino) references instituicao_ensino(id)
);