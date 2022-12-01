PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE brand (
	brand_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	brand_name TEXT(50) NOT NULL
);
INSERT INTO brand VALUES(1,'fiat');
CREATE TABLE IF NOT EXISTS "cars"
(
    car_id                 INTEGER            not null
        primary key autoincrement,
    model_id               INTEGER            not null
        constraint cars_model__fk
            references model ("")
            on update cascade on delete cascade,
    last_safety_inspection TEXT(50) default None,
    is_rentable            INTEGER  default 0 not null,
    is_sold                INTEGER  default 0 not null,
    is_ranted              INTEGER  default 0 not null,
    position               INTEGER  default 0 not null
);
INSERT INTO cars VALUES(1,1,'2022-02-13',0,0,0,0);
CREATE TABLE IF NOT EXISTS "model"
(
    model_id   INTEGER   not null
        primary key autoincrement,
    engine     TEXT(100) not null,
    model_name TEXT(50)  not null,
    brand_id   INTEGER   not null
        constraint model_brand__fk
            references brand ("")
            on update cascade on delete cascade,
    car_type   TEXT(50)  not null
);
INSERT INTO model VALUES(1,'69','500',1,'citadine');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('brand',1);
INSERT INTO sqlite_sequence VALUES('cars',1);
INSERT INTO sqlite_sequence VALUES('model',1);
COMMIT;
