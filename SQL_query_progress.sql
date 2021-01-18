
SELECT * FROM cardio_vitals

DROP TABLE cardio_demo;

-- Creating cardio_demo table 
CREATE TABLE cardio_demo (
	ID INT NOT NULL,
	age_days INT NOT NULL,
	gender INT NOT NULL,
	weight_kg INT NOT NULL,
	height_cm INT NOT NULL,
	BMI INT NOT NULL,
	cardio INT NOT NULL
);

-- creating cardio_vitals table
CREATE TABLE cardio_vitals (
	ID INT NOT NULL,
	systolic_bp INT NOT NULL,
	diastolic_bp INT NOT NULL,
	cholesterol INT NOT NULL,
	gluc INT NOT NULL,
	smoke INT NOT NULL,
	alco INT NOT NULL,
	active INT NOT NULL,
	cardio INT NOT NULL,
	FOREIGN KEY (ID) REFERENCES cardio_demo (ID)
);


SELECT * FROM cardio_vitals

-- SELECT * FROM cardio_demo

SELECT * FROM cardio_demo_2

-- JOIN of cardio_vitals and cardio_demo_2

SELECT cardio_vitals.id, cardio_vitals.systolic_bp,
	cardio_vitals.diastolic_bp, cardio_vitals.cholesterol,
	cardio_vitals.gluc, cardio_vitals.smoke, cardio_vitals.alco,
	cardio_vitals.active, cardio_vitals.cardio,
	cardio_demo_2.age_days, cardio_demo_2.gender, cardio_demo_2.weight_kg,
	cardio_demo_2.height_cm, cardio_demo_2.bmi
	INTO cardio_complete
	FROM cardio_vitals
	LEFT JOIN cardio_demo_2
	ON cardio_vitals.id = cardio_demo_2.id;
	
SELECT cardio_vitals.id, cardio_vitals.systolic_bp,
	cardio_demo_2.id, cardio_demo_2.age_days
	INTO cardio_test
	FROM cardio_vitals
	LEFT JOIN cardio_demo_2
	ON cardio_vitals.id = cardio_demo_2.id;

SELECT cardio_vitals.id FROM cardio_vitals;

SELECT cardio_demo_2.id FROM cardio_demo_2;