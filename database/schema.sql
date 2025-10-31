CREATE TABLE users (
  user_id VARCHAR(50) PRIMARY KEY,
  join_date DATE,
  location VARCHAR(100),
  is_verified BOOLEAN
);

CREATE TABLE cars (
  car_id VARCHAR(50) PRIMARY KEY,
  make VARCHAR(50),
  model VARCHAR(50),
  type VARCHAR(50),
  price_category VARCHAR(50)
);

CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id VARCHAR(50),
  car_id VARCHAR(50),
  start_date DATE,
  price DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (car_id) REFERENCES cars(car_id)
);
CREATE TABLE reviews (
  review_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id VARCHAR(50),
  car_id VARCHAR(50),
  rating INT,
  comment TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (car_id) REFERENCES cars(car_id)
);