DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;



CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    experience INT
);

-- JOIN TABLE
CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    pet_type VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL,
    owner_id INT REFERENCES owners(id) ON DELETE SET NULL -- How to set of it is last pet that owner has?
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255),
    registration BOOLEAN
);