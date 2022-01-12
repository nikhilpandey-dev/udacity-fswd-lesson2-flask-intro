CREATE TABLE drivers (
	id serial PRIMARY KEY,
	first_name varchar(255),
	last_name varchar(255)
);

CREATE TABLE vehicles (
	id serial PRIMARY KEY,
	make varchar(255),
	model varchar,
	driver_id integer REFERENCES drivers(id)
);

INSERT INTO drivers (first_name, last_name) VALUES ('Nikhil', 'Pandey'), ('Amy', 'Hua'), ('Pushkal', 'Pandey');

INSERT INTO vehicles (make, model, driver_id) VALUES ('2010', 'i10 Automatic', 1), ('2008', 'Swift Dezire', 1), ('2005', 'Honda Civic', 2), ('2012', 'Toyota Prius', 2), ('2021', 'Tesla Model S', 3);


INSERT INTO vehicles (make, model, driver_id) VALUES ('2022', 'Hyundai Creta', 3);


SELECT *
FROM drivers;

SELECT * FROM vehicles;

DELETE FROM vehicles
WHERE driver_id = 2;

SELECT * FROM vehicles;

-- SELECT * FROM drivers, vehicles
-- WHERE vehicles.driver_id = drivers.id;

SELECT * FROM vehicles
INNER JOIN drivers ON drivers.id = vehicles.driver_id
WHERE vehicles.driver_id = 3;

SELECT vehicles.make, vehicles.model FROM vehicles
INNER JOIN drivers ON drivers.id = vehicles.driver_id
WHERE drivers.first_name = 'Nikhil';

SELECT COUNT(*) as vehicles_count, first_name from vehicles
JOIN drivers ON drivers.id = vehicles.driver_id
GROUP BY drivers.first_name;

SELECT vehicles.make, count(*) as num from vehicles
JOIN drivers ON drivers.id = vehicles.driver_id
WHERE vehicles.make = '2022'
GROUP BY vehicles.make

SELECT * FROM drivers
SELECT * FROM vehicles;
ALTER TABLE vehicles
	ADD COLUMN color varchar(255) DEFAULT 'White';

ALTER TABLE vehicles
	DROP COLUMN registration_date;

ALTER TABLE vehicles
	ADD COLUMN registration_date DATE;
UPDATE vehicles
SET registration_date='2010-03-03'
WHERE id=1;

UPDATE vehicles
SET registration_date='2008-08-16'
WHERE id=2;
UPDATE vehicles
SET registration_date='2021-01-01'
WHERE id=5;
UPDATE vehicles
SET registration_date='2022-01-01'
WHERE id=7;
UPDATE vehicles
SET registration_date='2022-01-01'
WHERE id=8;
ALTER TABLE vehicles
	ADD COLUMN color varchar(255) DEFAULT 'White';

ALTER TABLE drivers
	ADD COLUMN email varchar(255),
	ADD COLUMN address TEXT;
TRUNCATE drivers RESTART IDENTITY CASCADE ;


SELECT * FROM vehicles
JOIN drivers ON drivers.id = vehicles.driver_id
WHERE vehicles.registration_date < '2020-12-31'

EXPLAIN
SELECT * FROM vehicles
JOIN drivers ON drivers.id = vehicles.driver_id
WHERE vehicles.registration_date < '2020-12-31';