'''sql query structure for the given problem'''

create table user(user_id int AUTO_INCREMENT PRIMARY KEY, username varchar(100) ,password integer);


# insert into user(username,password) values("logan", 123456);

# select*from user;


create table address(


add_id int AUTO_INCREMENT PRIMARY KEY,

user_id integer,

street integer,

pincode integer,

country varchar(100),

state varchar(100),

phone_no integer,

FOREIGN KEY (user_id)

REFERENCES user(user_id)

);