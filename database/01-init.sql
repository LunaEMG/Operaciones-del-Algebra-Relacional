-- Creación de Tablas para Tienda de Hardware

CREATE TABLE Categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_empresa VARCHAR(100) NOT NULL,
    contacto_email VARCHAR(100),
    pais VARCHAR(50)
);

CREATE TABLE Productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    id_proveedor INT,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Ordenes (
    id_orden SERIAL PRIMARY KEY,
    id_cliente INT,
    fecha_orden DATE DEFAULT CURRENT_DATE,
    total DECIMAL(10, 2),
    estado VARCHAR(20) DEFAULT 'Procesando', -- Procesando, Enviado, Entregado
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Detalle_Orden (
    id_detalle SERIAL PRIMARY KEY,
    id_orden INT,
    id_producto INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Envios (
    id_envio SERIAL PRIMARY KEY,
    id_orden INT UNIQUE,
    paqueteria VARCHAR(50),
    codigo_rastreo VARCHAR(50),
    fecha_envio DATE,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden)
);

CREATE TABLE Resenas (
    id_resena SERIAL PRIMARY KEY,
    id_producto INT,
    id_cliente INT,
    calificacion INT CHECK (calificacion >= 1 AND calificacion <= 5),
    comentario TEXT,
    fecha_resena DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);