import os
import datetime


def drop_table_if_exists():
    """ Deletes all tables"""

    drop_users = """ DROP TABLE IF EXISTS users """
    drop_parties = """ DROP TABLE IF EXISTS parties """
    drop_offices= """ DROP TABLE IF EXISTS offices """
    drop_candidates = """ DROP TABLE IF EXISTS candidates """
    drop_votes= """DROP TABLE IF EXISTS votes """
    drop_petitions= """DROP TABLE IF EXISTS petitions """
    deletions= [drop_users, drop_parties, drop_offices, drop_petitions,drop_candidates, drop_votes]
    return deletions
    
def create_tables():
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        firstName VARCHAR(40) NOT NULL,
        lastName VARCHAR(40) NOT NULL,
        otherName VARCHAR(40) NOT NULL,
        email VARCHAR(60) NOT NULL UNIQUE,
        phoneNumber VARCHAR (50) NOT NULL,
        passportUrl VARCHAR (60) NOT NULL,
        password VARCHAR(200) NOT NULL,
        isAdmin BOOLEAN DEFAULT False);"""

    parties_table = """
        CREATE TABLE IF NOT EXISTS parties (
        id serial PRIMARY KEY NOT NULL,
        party_name VARCHAR(50) NOT NULL,
        hqAddress VARCHAR(50) NOT NULL,
        logoUrl VARCHAR(50) NOT NULL);"""
   
    offices_table = """
        CREATE TABLE IF NOT EXISTS offices (
        id serial PRIMARY KEY NOT NULL,
        office_name VARCHAR(50) NOT NULL,
        office_type VARCHAR(50) NOT NULL
        );"""
    
    candidates_table= """"
        CREATE TABLE IF NOT EXISTS candidates(
        id serial PRIMARY KEY NOT NULL,
        party_Id  INTEGER NOT NULL,
        office_Id INTEGER NOT NULL,
        user-Id INTEGER NOT NULL,
        FOREIGN KEY (party_Id) REFERENCES parties (Id),
        FOREIGN KEY (office_Id) REFERENCES offices (Id),
        FOREIGN KEY (user_Id) REFERENCES users (Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE);"""

    votes_table= """
        CREATE TABLE IF NOT EXISTS votes(
        id serial PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP NULL DEFAULT NOW(),
        createdBy INTEGER NOT NULL,
        office_Id  INTEGER NOT NULL,
        candidate_Id INTEGER NOT NULL,
        FOREIGN KEY (office_Id) REFERENCES offices (Id),
        FOREIGN KEY (candidate_Id) REFERENCES candidates (Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE); """

    petitions_table= """
        CREATE TABLE IF NOT EXISTS votes(
        id serial PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP NULL DEFAULT NOW(),
        createdBy INTEGER NOT NULL,
        office_Id  INTEGER NOT NULL,
        FOREIGN KEY (createdBy) REFERENCES users (Id),
        FOREIGN KEY (office_Id) REFERENCES offices (Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE); """

    queries= [users, parties, offices, candidates, votes, petitions]
    return queries



