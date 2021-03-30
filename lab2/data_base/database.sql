CREATE DATABASE if not exists Amazon;
USE Amazon;

CREATE TABLE product (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    subgroup_id int,
    seller_id int,
    cart_id int,
    PRIMARY KEY(id)
    FOREIGN KEY (subgroup_id) REFERENCES subgroup(id)
    FOREIGN KEY (seller_id) REFERENCES seller(id)
    FOREIGN KEY (cart_id) REFERENCES cart(id)
)

CREATE TABLE subgroup (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    group_id int,
    PRIMARY KEY(id)
    FOREIGN KEY (group_id) REFERENCES group(id)
)

CREATE TABLE group (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    PRIMARY KEY(id)
)

CREATE TABLE customer (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    address varchar(50) NOT NULL,
    phone_number int NOT NULL,
    cart_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (cart_id) REFERENCES cart(id)
)

CREATE TABLE payment (
    customer_id int NOT NULL,
    card_type varchar(50) NOT NULL,
    card_number int NOT NULL
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
)

CREATE TABLE cart (
    id int NOT NULL,
    number_of_products varchar(50) NOT NULL,
    total int NOT NULL,
    PRIMARY KEY(id)
)

CREATE TABLE seller (
    id int NOT NULL,
    name varchar(50) NOT NULL
    PRIMARY KEY(id)
)