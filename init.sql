DROP DATABASE IF EXISTS sly;
CREATE DATABASE sly;
USE sly;

-- Create the users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- Create the items table
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

-- Create the purchases table
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

-- Insert a sample user
INSERT INTO users (id, name, email) VALUES (1, 'Test User #1', 'test1@example.com');
INSERT INTO users (id, name, email) VALUES (2, 'Test User #2', 'test2@example.com');
INSERT INTO users (id, name, email) VALUES (3, 'Test User #3', 'test3@example.com');

-- Insert some sample items
INSERT INTO items (name, description, price) VALUES
('Power-up Potion', 'A potion that grants a temporary power-up.', 5.99),
('Legendary Sword', 'A powerful sword for slaying dragons.', 19.99),
('Mystic Shield', 'A shield that can deflect magical attacks.', 12.50),
('Elixir of Life', 'Restores full health and mana.', 9.99),
('Invisibility Cloak', 'Makes the wearer invisible for a short period.', 15.00),
('Boots of Speed', 'Increases movement speed by 50%.', 7.50),
('Ring of Strength', 'Doubles the strength.', 11.25),
('Amulet of Wisdom', 'Increases intelligence and magical power.', 11.25),
('Fireball Scroll', 'A scroll that unleashes a powerful fireball.', 3.00),
('Ice Blast Scroll', 'A scroll that freezes enemies in their tracks.', 3.00),
('Lightning Bolt Scroll', 'A scroll that calls down a bolt of lightning.', 3.00),
('Dragon Scale Armor', 'Armor made from the scales of a dragon.', 25.00),
('Phoenix Feather', 'A feather that can revive a fallen ally.', 30.00),
('Bag of Holding', 'A bag that can hold an unlimited number of items.', 50.00);
