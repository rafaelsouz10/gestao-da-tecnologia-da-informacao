/*1) Listar o título e a quantidade de atores para os filmes que possuem 
o idioma "ENGLISH" e mais de 10 atores ordenando por ordem*/
select
	f.titulo as filme, count(a.ator_id)
from 
	filme as f
join
	filme_ator as fa
    on fa.filme_id = f.filme_id
join
	ator as a
    on a.ator_id = fa.ator_id
join
	idioma as id
    on id.idoma_id = f.idioma_id
where
	count(a.ator_id) and idioma = 'ENGLISH';
    

select duracao_da_locacao from filme order by duracao_da_locacao desc;
/*2) Qual a maior duração da locação dentre os filmes?*/
select
	max(f.duracao_da_locacao) as maior_duracao_locacao
from
	filme as f;
    

/*3) Quantos filmes possuem a maior duração de locação?*/
select
	f.titulo as filme, count(f.duracao_da_locacao) as quantidade
from
	filme as f
where
	f.duracao_da_locacao = (select max(duracao_da_locacao) from filme);
    
    
/*4) Qual a quantidade de filmes por Ator ordenando decrescente por quantidade?*/
select
	a.primeiro_nome as ator, count(fa.ator_id) as qtd_filme
from
	ator as a
join
	filme_ator as fa
    on fa.ator_id = a.ator_id
group by
	a.primeiro_nome
order by
	qtd_filme desc;

/*5) */


/*6) Quantos clientes moram no país “Brazil”?*/
select
	p.pais as pais, count(p.pais) as qtd_pais
from
	pais as p
join
	cidade as cid
    on cid.pais_id = p.pais_id
join
	endereco as en
    on en.cidade_id = cid.cidade_id
join
	cliente as c
    on c.endereco_id = en.endereco_id
where
	pais = 'Brazil';
    

/*7) Quais Filmes possuem preço da Locação maior que a média de preço da locação?*/
select
	f.titulo as filme, pag.valor as preco
from
	pagamento as pag
join
	aluguel as al
    on al.aluguel_id = pag.aluguel_id
join
	inventario as inv
    on inv.inventario_id = al.inventario_id
join
	filme as f
    on f.filme_id = inv.filme_id
where
	pag.valor > (select avg(valor) from pagamento);
    

/*8) Qual a soma da duração dos Filmes por categoria?*/
select
	cat.nome as categoria, sum(duracao_do_filme)
from
	categoria as cat
join
	filme_categoria as fc
    on fc.categoria_id = cat.categoria_id
join
	filme as f
    on f.filme_id = fc.filme_id
group by
	cat.nome;



    
    
    