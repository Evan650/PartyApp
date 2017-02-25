#Our database..
#By: Evan Yin, Angela Werner Kenny Ellis



CREATE TABLE 'UserInfo'.'tbl_user' (
'user_uid' BIGINT UNIQUE AUTO_INCREMENT,
'last_name' VARCHAR(45) NULL,
'first_name' VARCHAR(45) NULL,
'phone' INT(10),
PRIMARY KEY ('user_uid'));

CREATE TABLE 'UserInfo'.'tbl_address' (
'address_uid' BIGINT UNIQUE AUTO_INCREMENT,
'address' VARCHAR(45) NULL,
'city' VARCHAR(45) NULL,
'state' VARCHAR(20) NULL,
'country' VARCHAR(45) NULL,
'postal_code' INT(5) NULL,
PRIMARY KEY ('address_uid'));
