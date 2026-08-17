CREATE TABLE source_device (
	source_id INT PRIMARY KEY AUTO_INCREMENT,
	vendor_name TEXT,
	device_name TEXT NOT NULL,
	device_ip VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE network_device (
	net_device_id INT PRIMARY KEY AUTO_INCREMENT,
	vendor_name TEXT,
	device_layer INT NOT NULL,
	device_ip VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE instance (
	instance_id INT PRIMARY KEY AUTO_INCREMENT,
	source_id INT NOT NULL,
	timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	net_device_id INT NOT NULL,
	command TEXT NOT NULL,
	firmware_ver TEXT,
	output_text TEXT,

	CONSTRAINT FK_SOURCE_DEVICE FOREIGN KEY (source_id)
	REFERENCES source_device(source_id) ON DELETE RESTRICT,

	CONSTRAINT FK_NET_DEVICE FOREIGN KEY (net_device_id)
	REFERENCES network_device(net_device_id) ON DELETE RESTRICT
);
