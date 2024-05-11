-- Active: 1715406346476@@127.0.0.1@3306@board-games-collection
CREATE TABLE players_gameroom(
    player_id INT NOT NULL,
    gameroom_id INT NOT NULL,
    PRIMARY KEY (player_id, gameroom_id),
    FOREIGN KEY (player_id) REFERENCES users(user_id),
    FOREIGN KEY (gameroom_id) REFERENCES gamerooms(gameroom_id)
) COMMENT '';


DROP Table players_gameroom;
