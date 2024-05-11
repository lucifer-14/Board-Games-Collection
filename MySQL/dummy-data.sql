
# Add dummy users - dummy1, dummy2, dummy3 both password and username
insert into users (username, hashed_password, email) values ("dummy1", "$2b$12$t4/P7Jx/FRTJSeq66iBsBuGLo11e3d35SN.SSwpYBYJoPG.JufCae", "dummy1@gmail.com");
insert into users (username, hashed_password, email) values ("dummy2", "$2b$12$h1TLkv2CBu7BUAb14I.w8OJycLXVcgJVpbhfTyJ5qLj.mPBa4sQHO", "dummy2@gmail.com");
insert into users (username, hashed_password, email) values ("dummy3", "$2b$12$aEhPTmOh2Hp60S6pYkOg4OeRBLeojWEPtqY4keTaDbeD8CM3imQEe", "dummy3@gmail.com");
insert into users (username, hashed_password, email) values ("dummy4", "$2b$12$i6y5BO4.gune5GWMpU4yEeY9dT/p0D9.fMul.pZHEgXRSsFVXH482", "dummy4@gmail.com");


# Add dummy games
insert into games (game_name, game_description, game_rules, minimum_players, is_playable) 
values ("Dummy Game 1", "data//games//dummy_game_1//description.txt", "data//game//dummy_game_1//game_rules.txt", 2, TRUE);

insert into games (game_name, game_description, game_rules, minimum_players, is_playable) 
values ("Dummy Game 2", "data//games//dummy_game_2//description.txt", "data//game//dummy_game_2//game_rules.txt", 4, FALSE);


# Add dummy gamerooms #passwords - room1, room2
insert into gamerooms (room_name, room_description, room_hashed_password, master_player_id, game_id) 
values ("Dummy Room 1", "data//rooms//dummy_room_1//description.txt", "$2b$12$vzRIwf.Nm.Q.aTl6UOt.1Otbcyr9Rdowm1WwLKy2wvmk2ZUQ72Dq6", 1, 1);

insert into gamerooms (room_name, room_description, room_hashed_password, master_player_id)
values ("Dummy Room 2", "data//rooms//dummy_room_2//description.txt", "$2b$12$CrzZcoBvS0cZr0BtLT6IIOFPVDwbHrA5DcTqBUZQmcMYJjez2HkmO", 2);


# Add dummy players_gamerooms
insert into players_gameroom (player_id, gameroom_id) values (3, 1);
insert into players_gameroom (player_id, gameroom_id) values (4, 1);


