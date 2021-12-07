DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;



CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    experience INT
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255),
    registration BOOLEAN
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    pet_type VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL,
    treatment_notes TEXT
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    appointment_date DATE,
    check_in TIME,
    check_out TIME,
    pet_id INT REFERENCES pets(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id)
);