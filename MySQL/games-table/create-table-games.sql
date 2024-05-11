-- Active: 1715406346476@@127.0.0.1@3306@board-games-collection
CREATE TABLE games(  
    game_id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    game_name VARCHAR(40) UNIQUE NOT NULL COMMENT 'game_name',
    game_description VARCHAR(100) NOT NULL COMMENT 'path to game description.txt',
    game_rules VARCHAR(100) NOT NULL COMMENT 'path to game rules.txt',
    minimum_players INT NOT NULL COMMENT 'required minimum players', 
    added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Added Date',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Updated Date',
    is_playable BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'is game playable?',
    is_active BOOLEAN NOT NULL DEFAULT TRUE COMMENT 'is game active?'
) COMMENT '';


DROP Table games;
