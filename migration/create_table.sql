CREATE TABLE countries (
  country_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  country_name VARCHAR(50)
);

CREATE TABLE rig_counts (
  rig_date DATE NOT NULL,
  stateOrProvince VARCHAR(50) NOT NULL,
  land_rigs INTEGER,
  offshore_rigs INTEGER,
  country_id INTEGER NOT NULL,
  FOREIGN KEY (country_id) REFERENCES countries(country_id),
  PRIMARY KEY (rig_date, stateOrProvince)
);
