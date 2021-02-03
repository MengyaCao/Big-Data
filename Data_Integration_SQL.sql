drop table if exists bd_sales_1, bd_sales_2, bd_customers;
create table bd_customers (
	customer_name text primary key,
	region text
);
create table bd_sales_1 (
	customer_name text,
	item text,
	quarter integer,
	quantity integer,
	primary key(customer_name, item)
);
create table bd_sales_2 (
	customer_name text,
	item text,
	quarter integer,
	quantity integer,
	primary key(customer_name, item)
);
insert into bd_customers(customer_name, region) values 
	('John Doe', 'NE'),
	('Jane Doe', 'SE'),
	('Jessica Tang', 'NW'),
	('Sam Spade', 'SW'),
	('Petra Sanders', 'NW'),
	('William Williams', 'SE');
insert into bd_sales_1(customer_name, item, quarter, quantity) values
	('John Doe', 'popcorn', 1, 100),
	('Jessica Tang', 'popcorn', 1, 73),
	('John Doe', 'carrots', 1, 128),
	('Petra Sanders', 'carrots', 1, 200),
	('William, Williams', 'carrots', 1, 18),
	('Petra Sanders', 'popcorn', 1, 230);
insert into bd_sales_2(customer_name, item, quarter, quantity) values 
	('John Doe', 'popcorn', 2, 85),
	('Jane Doe', 'carrots', 2, 140),
	('Jane Doe', 'popcorn', 2, 100),
	('Sam Spade', 'carrots', 2, 25),
	('Sam Spade', 'popcorn', 2, 35),
	('William Williams', 'popcorn', 2, 341),
	('Petra Sanders', 'carrots', 2, 105),
	('Jessica Tang', 'carrots', 2, 83);

