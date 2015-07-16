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
CREATE TABLE "points" ("id" integer NOT NULL PRIMARY KEY,
    "date_added" datetime NOT NULL,
    "lat" varchar(12) NOT NULL,
    "lon" varchar(12) NOT NULL,
    "altitude" varchar(14) NOT NULL,
    "label" text NOT NULL,
    "description" text NOT NULL,
    "meters_error" real NOT NULL,
    "plan_id_id" integer NOT NULL REFERENCES "plans" ("id"));

CREATE INDEX "points_ad0ccc49" ON "points" ("plan_id_id");

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
