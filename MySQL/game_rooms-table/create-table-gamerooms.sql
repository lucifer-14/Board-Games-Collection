-- Active: 1715406346476@@127.0.0.1@3306@board-games-collection
CREATE TABLE gamerooms(  
    gameroom_id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    room_name VARCHAR(40) UNIQUE NOT NULL COMMENT 'game room name',
    room_description VARCHAR(100) NOT NULL COMMENT 'path to room description.txt',
    room_hashed_password VARCHAR(64) UNIQUE NOT NULL COMMENT 'room_hashed_password',
    joined_players INT NOT NULL DEFAULT 1 COMMENT 'joined players count',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Created Date',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Updated Date',
    master_player_id INT NOT NULL COMMENT 'game room creator id',
    game_id INT DEFAULT NULL COMMENT 'chosen game id',
    FOREIGN KEY (master_player_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
) COMMENT '';


DROP Table gamerooms;
