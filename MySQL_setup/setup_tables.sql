-- Creates tables in the database

USE HomeCooker_db;

-- Table for Users
CREATE TABLE IF NOT EXISTS Users (
 id varchar(60) NOT NULL,
 created_at datetime NOT NULL,
 updated_at datetime NOT NULL,
 first_name varchar(128) NULL,
 last_name varchar(128) NULL,
 website varchar(256) NULL,
 email varchar(128) NOT NULL,
 password varchar(128) NOT NULL,
 user_type int NOT NULL,
 profile_image blob NULL,
 nickname varchar(128) NULL,

PRIMARY KEY (id)
);

-- Table for Recipes

CREATE TABLE IF NOT EXISTS Recipes (
 id varchar(60) NOT NULL,
 created_at datetime NOT NULL,
 updated_at datetime NOT NULL,
 name varchar(128) NOT NULL,
 text varchar(2048) NOT NULL,
 user_id varchar(60),
 review int NULL,
 ingredients varchar(1024) NOT NULL,

PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Table for Reviews

CREATE TABLE IF NOT EXISTS Reviews (
 id varchar(60) NOT NULL,
 created_at datetime NOT NULL,
 updated_at datetime NOT NULL,
 text varchar(1024) NOT NULL,
 rating int NOT NULL,
 user_id varchar(60),
 recipe_id varchar(60),

PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES Users(id),
FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
);
