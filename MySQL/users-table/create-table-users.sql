-- Active: 1715406346476@@127.0.0.1@3306@board-games-collection
CREATE TABLE users(  
    user_id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    username VARCHAR(40) UNIQUE NOT NULL COMMENT 'username',
    hashed_password VARCHAR(64) UNIQUE NOT NULL COMMENT 'hashed_password',
    email VARCHAR(100) UNIQUE NOT NULL COMMENT 'email',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Create Date',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Updated Date',
    is_in_game BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'is in game?',
    is_active BOOLEAN NOT NULL DEFAULT TRUE COMMENT 'is active account?'
) COMMENT '';


DROP Table users;
