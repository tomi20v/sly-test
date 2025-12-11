DROP DATABASE IF EXISTS sly;
CREATE DATABASE sly;
USE sly;

-- Create the users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email TEXT NOT NULL UNIQUE
);

-- Create the items table
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

-- Create the purchases table
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at DATETIME NOT NULL,
    payment_status ENUM('pending', 'failed', 'paid') NOT NULL DEFAULT 'pending',
    xsolla_transaction_id VARCHAR(255) DEFAULT NULL,
    xsolla_token TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

-- Insert sample users
INSERT INTO users (id, email) VALUES (1, 'test1@example.com');
INSERT INTO users (id, email) VALUES (2, 'test2@example.com');
INSERT INTO users (id, email) VALUES (3, 'test3@example.com');

-- Insert some sample items
INSERT INTO items (name, description, price) VALUES
('Power-up Potion', 'A potion that grants a temporary power-up.', 5.99),
('Legendary Long Sword with a Very Long Name', 'A powerful sword for slaying dragons.', 19.99),
('Mystic Shield', 'A shield that can deflect magical attacks. A shield that can deflect magical attacks. A shield that can deflect magical attacks. A shield that can deflect magical attacks.', 12.50),
('Elixir of Life', 'Restores full health and mana.', 9.99),
('Invisibility Cloak', 'Makes the wearer invisible for a short period.', 15.00),
('Boots of Speed', 'Increases movement speed by 50%.', 7.50),
('Ring of Strength', 'Doubles the strength.', 11.25),
('Amulet of Wisdom', 'Increases intelligence and magical power.', 11.25),
('Fireball Scroll', 'A scroll that unleashes a powerful fireball.', 3.00),
('Ice Blast Scroll', 'A scroll that freezes enemies in their tracks.', 3.00),
('Lightning Bolt Scroll', 'A scroll that calls down a bolt of lightning.', 3.00),
('Shield of the Elements', 'Provides resistance to all elemental damage.', 25.00),
('Sword of the Heavens', 'A divine sword that deals extra damage to undead.', 22.50),
('Staff of the Archmage', 'A powerful staff that enhances all magical abilities.', 30.00),
('Dagger of Shadows', 'A silent dagger that allows for stealthy takedowns.', 18.75);

-- Create the webhook_log table
CREATE TABLE webhook_logs (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    data TEXT NOT NULL,
    result INT,
    error TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
