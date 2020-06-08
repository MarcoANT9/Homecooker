-- Creates tables in the database

-- Table for Users
CREATE TABLE IF NOT EXISTS `users`
(
 `id`              varchar(60) NOT NULL ,
 `created_at`      datetime NOT NULL ,
 `updated_at`      datetime NOT NULL ,
 `first_name`      varchar(128) NULL ,
 `last_name`       varchar(128) NULL ,
 `website`         varchar(256) NULL ,
 `youtube_channel` varchar(128) NULL ,
 `email`           varchar(128) NOT NULL ,
 `password`        varchar(128) NOT NULL ,
 `type`            tinyint NOT NULL ,
 `profile_image`   blob NULL ,
 `nickname`        varchar(128) NULL ,

PRIMARY KEY (`id`)
);

-- Table for Reviews

CREATE TABLE IF NOT EXISTS `reviews`
(
 `id`         varchar(60) NOT NULL ,
 `created_at` datetime NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `text`       varchar(1024) NOT NULL ,
 `rating`     tinyint NOT NULL ,
 `user_id`    varchar(60) NOT NULL ,
 `recipe_id`  varchar(60) NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_49` (`user_id`),
CONSTRAINT `user_review` FOREIGN KEY `fkIdx_49` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_52` (`recipe_id`),
CONSTRAINT `recipe_reviews` FOREIGN KEY `fkIdx_52` (`recipe_id`) REFERENCES `recipes` (`id`)
);

-- Table for Recipes

CREATE TABLE IF NOT EXISTS `recipes`
(
 `id`          varchar(60) NOT NULL ,
 `created_at`  datetime NOT NULL ,
 `updated_at`  datetime NOT NULL ,
 `name`        varchar(128) NOT NULL ,
 `text`        varchar(2048) NOT NULL ,
 `user_id`     varchar(60) NOT NULL ,
 `review`      tinyint NULL ,
 `ingredients` varchar(1024) NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_23` (`user_id`),
CONSTRAINT `user_recipe` FOREIGN KEY `fkIdx_23` (`user_id`) REFERENCES `users` (`id`)
);
