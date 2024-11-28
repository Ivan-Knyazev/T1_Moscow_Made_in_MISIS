create table if not exists Bot(
    BotId bigserial primary key,
    Salute varchar(1000) not null,
    description varchar(2000) not null,
    End_of_dialogue varchar(1000) not null,
    URL varchar(500),
    Prompt text,
    Neural_network_model varchar(100) not null,
    ColorSetId varchar(100) not null,
    Font varchar(100) not null,
    Assistant_name varchar(100) not null,
    Foreign key (ColorSetId) references ColorSet(ColorSetId) on delete set null
)

create table if not exists ColorSet(
    ColorSetId bigserial primary key,
    ColorId bigserial primary key,
    Foreign key (ColorId) references Color(ColorId) on delete set null
)

create table if not exists Color(
    ColorId bigserial primary key,
    Color text not null,
)
