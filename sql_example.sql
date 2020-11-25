drop database if exists example;
create database if not exists example;
drop table if exists example.users;
create table example.users 
(
id int primary key,
name text
);
select * from example.users; 

