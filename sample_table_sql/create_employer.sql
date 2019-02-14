CREATE TABLE EMPLOYER (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    class VARCHAR(255) NOT NULL,
    created DATETIME,
    modified DATETIME
);

INSERT INTO EMPLOYER VALUES ('10000', 'Taro Yamada', 'Employee', '2017/1/1', '2017/1/1');
INSERT INTO EMPLOYER VALUES ('10001', 'Michiel Hartz', 'President', '2017/1/1', '2017/1/1');
INSERT INTO EMPLOYER VALUES ('10002', 'Mike Jonson', 'Employee', '2017/1/1', '2017/1/1');
INSERT INTO EMPLOYER VALUES ('10003', 'Tetsuka Hanako', 'Employee', '2017/1/1', '2017/1/1');
INSERT INTO EMPLOYER VALUES ('10004', 'Jojima Tomoya', 'Chief', '2017/1/1', '2017/1/1');
INSERT INTO EMPLOYER VALUES ('10005', 'Nagase Shigeru', 'Chief', '2017/1/1', '2017/1/1');
