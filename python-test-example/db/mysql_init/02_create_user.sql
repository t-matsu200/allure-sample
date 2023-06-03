create user 'test_user'@'db_server' identified by 'test_password';
grant all privileges on sample.* to test_user@db_server;
flush privileges;
