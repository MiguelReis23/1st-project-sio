import bcrypt
import os
import sqlite3
from cfg import *


def initializeDatabase():
  try:
    if not os.path.exists(STORAGE_PATH):
      os.makedirs(STORAGE_PATH)
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS users (
				id INTEGER PRIMARY KEY,
				mec INTEGER NOT NULL,
				name TEXT NOT NULL,
				email TEXT NOT NULL,
				password TEXT NOT NULL,
				profile_picture TEXT NOT NULL
			);
		"""
    )
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS tokens (
				id INTEGER PRIMARY KEY,
				token TEXT NOT NULL,
				expiration INTEGER NOT NULL,
				user_id INTEGER NOT NULL
			);
		"""
    )
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS rooms (
				id INTEGER PRIMARY KEY,
				name TEXT NOT NULL,
				description TEXT NOT NULL,
				image TEXT NOT NULL,
				capacity INTEGER,
				power_sockets INTEGER,
				computers INTEGER,
				oscilloscopes INTEGER,
				signal_generators INTEGER,
				multimeters INTEGER,
				sound_system INTEGER,
				projector INTEGER,
				whiteboard INTEGER,
				reservations TEXT NOT NULL
			);
		"""
    )
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS equipments (
				id INTEGER PRIMARY KEY,
				name TEXT NOT NULL,
				description TEXT NOT NULL,
				reservations TEXT NOT NULL,
				locker TEXT NOT NULL,
				image TEXT NOT NULL,
        available INTEGER NOT NULL
			);
		"""
    )
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS reservations (
				id INTEGER PRIMARY KEY,
				user_id INTEGER NOT NULL,
				room_id INTEGER NOT NULL,
				start_time INTEGER NOT NULL,
				end_time INTEGER NOT NULL,
				reason TEXT
			);    STORAGE
		"""
    )
    cur.execute(
    """
			CREATE TABLE IF NOT EXISTS equipment_reservations (
				id INTEGER PRIMARY KEY,
				user_id INTEGER NOT NULL,
				equipment_id INTEGER NOT NULL,
				start_time INTEGER NOT NULL,
				end_time INTEGER NOT NULL,
				usage_place TEXT,
        observation TEXT
			);
		"""
    )
    con.commit()
    con.close()
  except sqlite3.Error as error:
    raise Exception("Error connecting to the database: ", error)
