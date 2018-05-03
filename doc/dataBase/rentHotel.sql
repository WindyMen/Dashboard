/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/5/3 16:05:26                            */
/*==============================================================*/


drop table if exists addRoom;

drop table if exists makeComment;

drop table if exists makeOrder;

drop table if exists room;

drop table if exists user;

/*==============================================================*/
/* Table: addRoom                                               */
/*==============================================================*/
create table addRoom
(
   uid                  varchar(32) not null,
   rid                  varchar(32) not null,
   orderedTime          time,
   primary key (uid, rid)
);

/*==============================================================*/
/* Table: makeComment                                           */
/*==============================================================*/
create table makeComment
(
   uid                  varchar(32) not null,
   rid                  varchar(32) not null,
   text                 text,
   rating               int,
   photo                varchar(32),
   primary key (uid, rid)
);

/*==============================================================*/
/* Table: makeOrder                                             */
/*==============================================================*/
create table makeOrder
(
   uid                  varchar(32) not null,
   rid                  varchar(32) not null,
   orderedTime2         time,
   username3            varchar(32),
   roomName2            varchar(32),
   arrivalDate          date,
   departureDate        date,
   primary key (uid, rid)
);

/*==============================================================*/
/* Table: room                                                  */
/*==============================================================*/
create table room
(
   rid                  varchar(32) not null,
   uid                  varchar(32),
   roomName             char(10),
   type                 varchar(32),
   numOfPerson          int,
   description          varchar(100),
   numOfBed             int,
   numOfToliet          int,
   country              varchar(32),
   province             varchar(32),
   city                 varchar(32),
   town                 varchar(32),
   specificPlace        varchar(32),
   otherOption          varchar(32),
   title                varchar(32),
   photoDir             varchar(32),
   rating               int,
   primary key (rid)
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

alter table addRoom add constraint FK_addRoom foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table addRoom add constraint FK_addRoom2 foreign key (rid)
      references room (rid) on delete restrict on update restrict;

alter table makeComment add constraint FK_makeComment foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table makeComment add constraint FK_makeComment2 foreign key (rid)
      references room (rid) on delete restrict on update restrict;

alter table makeOrder add constraint FK_makeOrder foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table makeOrder add constraint FK_makeOrder2 foreign key (rid)
      references room (rid) on delete restrict on update restrict;

alter table room add constraint FK_Relationship_4 foreign key (uid)
      references user (uid) on delete restrict on update restrict;

