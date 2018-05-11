/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/5/11 15:47:30                           */
/*==============================================================*/


drop table if exists city;

drop table if exists country;

drop table if exists makeComment;

drop table if exists makeOrder;

drop table if exists province;

drop table if exists room;

drop table if exists town;

drop table if exists user;

/*==============================================================*/
/* Table: city                                                  */
/*==============================================================*/
create table city
(
   cityid               varchar(32) not null,
   provinceid           varchar(32),
   cname                varchar(32),
   primary key (cityid)
);

/*==============================================================*/
/* Table: country                                               */
/*==============================================================*/
create table country
(
   cname                varchar(32),
   countryid            varchar(32) not null,
   primary key (countryid)
);

/*==============================================================*/
/* Table: makeComment                                           */
/*==============================================================*/
create table makeComment
(
   uid                  varchar(32) not null,
   roomid               varchar(32) not null,
   text                 text,
   rating               int,
   photo                varchar(32),
   primary key (uid, roomid)
);

/*==============================================================*/
/* Table: makeOrder                                             */
/*==============================================================*/
create table makeOrder
(
   uid                  varchar(32) not null,
   roomid               varchar(32) not null,
   orderedTime2         time,
   username3            varchar(32),
   roomName2            varchar(32),
   arrivalDate          date,
   departureDate        date,
   primary key (uid, roomid)
);

/*==============================================================*/
/* Table: province                                              */
/*==============================================================*/
create table province
(
   provinceid           varchar(32) not null,
   countryid            varchar(32),
   pname                varchar(32),
   primary key (provinceid)
);

/*==============================================================*/
/* Table: room                                                  */
/*==============================================================*/
create table room
(
   roomid               varchar(32) not null,
   townid               varchar(32),
   countryid            varchar(32),
   provinceid           varchar(32),
   cityid               varchar(32),
   uid                  varchar(32),
   roomName             text,
   type                 varchar(32),
   numOfPerson          int,
   description          varchar(100),
   numOfBed             int,
   numOfToilet          int,
   specificPlace        varchar(32),
   otherOption          varchar(32),
   title                varchar(32),
   photoDir             varchar(32),
   rating               int,
   createdTime          time,
   startRentDate        date,
   endRentDate          date,
   primary key (roomid)
);

/*==============================================================*/
/* Table: town                                                  */
/*==============================================================*/
create table town
(
   townid               varchar(32) not null,
   cityid               varchar(32),
   tname                varchar(32),
   primary key (townid)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   uid                  varchar(32) not null,
   username             varchar(32),
   password             varchar(32),
   paypassword          varchar(6),
   description          varchar(100),
   Email                varchar(32),
   primary key (uid)
);

alter table city add constraint FK_belong2 foreign key (provinceid)
      references province (provinceid) on delete restrict on update restrict;

alter table makeComment add constraint FK_makeComment foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table makeComment add constraint FK_makeComment2 foreign key (roomid)
      references room (roomid) on delete restrict on update restrict;

alter table makeOrder add constraint FK_makeOrder foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table makeOrder add constraint FK_makeOrder2 foreign key (roomid)
      references room (roomid) on delete restrict on update restrict;

alter table province add constraint FK_belong1 foreign key (countryid)
      references country (countryid) on delete restrict on update restrict;

alter table room add constraint FK_in1 foreign key (roomid)
      references country (countryid) on delete restrict on update restrict;

alter table room add constraint FK_in2 foreign key (roomid)
      references province (provinceid) on delete restrict on update restrict;

alter table room add constraint FK_in3 foreign key (roomid)
      references city (cityid) on delete restrict on update restrict;

alter table room add constraint FK_in4 foreign key (roomid)
      references town (townid) on delete restrict on update restrict;

alter table room add constraint FK_own foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table town add constraint FK_belong3 foreign key (cityid)
      references city (cityid) on delete restrict on update restrict;

