BEGIN TRANSACTION;
CREATE TABLE point (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date_added DATETIME DEFAULT (datetime('now','localtime')),
    lat VARCHAR(12),
    lon VARCHAR(12),
    altitude VARCHAR(12),
    plan_id INTEGER,
    label TEXT,
    description TEXT,
    meters_error INTEGER NOT NULL,
    FOREIGN KEY(plan_id) REFERENCES plans(id)
);
CREATE TABLE plans (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date_added DATETIME DEFAULT (datetime('now','localtime')),
    description TEXT
);

CREATE TABLE shapes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date DATETIME DEFAULT (datetime('now','localtime')),
    shapetype TEXT,
    plan_id INTEGER,
    FOREIGN KEY(plan_id) REFERENCES plans(id)
);

COMMIT;
