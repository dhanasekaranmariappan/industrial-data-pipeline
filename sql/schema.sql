CREATE DATABASE industrial_analytics;

USE industrial_analytics;

CREATE TABLE machine_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    air_temperature FLOAT,
    process_temperature FLOAT,
    rotational_speed FLOAT,
    torque FLOAT,
    tool_wear INT,
    power FLOAT,
    temp_diff FLOAT
);
