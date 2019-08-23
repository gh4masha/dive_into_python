use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store where is_automated=1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from sale


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select distinct store_id from store where store_id not in (select distinct store_id from sale);

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select product.name, avg(total/quantity) from product, sale where product.product_id=sale.product_id group by sale.product_id

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select product.name from product join  (select product_id from sale group by product_id having count(store_id)=1) as p on product.product_id=p.product_id

-- 8. Получить названия всех складов, с которых продавался только один продукт
select store.name from store join (select store_id from sale group by store_id having count(product_id)=1) as s on store.store_id= s.store_id;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale order by total desc limit 1

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale order by total desc, date asc limit 1

