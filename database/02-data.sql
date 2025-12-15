-- Poblando la Base de Datos (100+ tuplas)

-- 1. Categorias (5)
INSERT INTO Categorias (nombre, descripcion) VALUES
('Procesadores', 'CPUs de alto rendimiento'),
('Tarjetas Gráficas', 'GPUs para gaming y trabajo'),
('Almacenamiento', 'SSDs y Discos Duros'),
('Memoria RAM', 'Módulos DDR4 y DDR5'),
('Fuentes de Poder', 'PSUs certificadas');

-- 2. Proveedores (5)
INSERT INTO Proveedores (nombre_empresa, contacto_email, pais) VALUES
('TechSupply Global', 'contact@techsupply.com', 'USA'),
('Asian Chipset Ltd', 'sales@asianchip.cn', 'China'),
('EuroComp Distributors', 'info@eurocomp.de', 'Alemania'),
('MexHard Importadora', 'ventas@mexhard.mx', 'Mexico'),
('Silicon Valley Parts', 'b2b@siliconparts.com', 'USA');

-- 3. Productos (20)
INSERT INTO Productos (nombre, precio, stock, id_categoria, id_proveedor) VALUES
('Intel Core i9-13900K', 580.00, 50, 1, 1),
('AMD Ryzen 9 7950X', 550.00, 40, 1, 1),
('Intel Core i5-13600K', 300.00, 100, 1, 5),
('AMD Ryzen 5 7600X', 250.00, 80, 1, 5),
('NVIDIA RTX 4090', 1600.00, 10, 2, 2),
('NVIDIA RTX 4080', 1200.00, 20, 2, 2),
('AMD Radeon RX 7900 XTX', 1000.00, 25, 2, 1),
('NVIDIA RTX 3060', 350.00, 60, 2, 4),
('Samsung 980 Pro 1TB', 80.00, 200, 3, 3),
('Samsung 980 Pro 2TB', 150.00, 100, 3, 3),
('WD Black SN850X 1TB', 85.00, 150, 3, 5),
('Kingston NV2 1TB', 50.00, 300, 3, 4),
('Corsair Vengeance 32GB DDR5', 120.00, 100, 4, 1),
('G.Skill Trident Z5 32GB', 130.00, 80, 4, 2),
('Kingston Fury 16GB DDR4', 45.00, 200, 4, 4),
('Crucial RAM 16GB', 40.00, 250, 4, 5),
('Corsair RM850x', 110.00, 60, 5, 1),
('EVGA SuperNOVA 750 GT', 90.00, 70, 5, 1),
('Seasonic Focus GX-850', 125.00, 40, 5, 3),
('MSI MPG A850G', 115.00, 50, 5, 2);

-- 4. Clientes (10)
INSERT INTO Clientes (nombre, apellido, email) VALUES
('Juan', 'Perez', 'juan.perez@mail.com'),
('Maria', 'Lopez', 'maria.lopez@mail.com'),
('Carlos', 'Gomez', 'carlos.gomez@mail.com'),
('Ana', 'Martinez', 'ana.mtz@mail.com'),
('Luis', 'Hernandez', 'luis.hdz@mail.com'),
('Sofia', 'Diaz', 'sofia.diaz@mail.com'),
('Miguel', 'Torres', 'miguel.torres@mail.com'),
('Elena', 'Ramirez', 'elena.ram@mail.com'),
('David', 'Flores', 'david.flores@mail.com'),
('Isabel', 'Ruiz', 'isabel.ruiz@mail.com');

-- 5. Ordenes (15)
INSERT INTO Ordenes (id_cliente, total, estado) VALUES
(1, 1680.00, 'Entregado'), -- Compró i9, RTX 4090, RAM
(2, 350.00, 'Entregado'),
(3, 1200.00, 'Enviado'),
(1, 80.00, 'Procesando'),
(4, 2500.00, 'Entregado'),
(5, 45.00, 'Entregado'),
(6, 150.00, 'Enviado'),
(7, 300.00, 'Procesando'),
(8, 1000.00, 'Entregado'),
(9, 50.00, 'Entregado'),
(10, 120.00, 'Procesando'),
(1, 550.00, 'Entregado'), -- Juan sigue comprando
(2, 85.00, 'Entregado'),
(3, 1600.00, 'Enviado'),
(4, 110.00, 'Procesando');

-- 6. Detalle_Orden (40+ tuplas para vincular muchos productos)
INSERT INTO Detalle_Orden (id_orden, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 580.00), (1, 5, 1, 1600.00), (1, 13, 1, 120.00), -- Orden 1
(2, 8, 1, 350.00), -- Orden 2
(3, 6, 1, 1200.00), -- Orden 3
(4, 9, 1, 80.00), -- Orden 4
(5, 5, 1, 1600.00), (5, 2, 1, 550.00), (5, 17, 1, 110.00), -- Orden 5 (High end)
(6, 15, 1, 45.00),
(7, 10, 1, 150.00),
(8, 3, 1, 300.00),
(9, 7, 1, 1000.00),
(10, 12, 1, 50.00),
(11, 13, 1, 120.00),
(12, 2, 1, 550.00),
(13, 11, 1, 85.00),
(14, 5, 1, 1600.00),
(15, 17, 1, 110.00),
-- Rellenar detalles extra para generar volumen
(1, 18, 1, 90.00), (3, 14, 2, 130.00), (4, 16, 2, 40.00),
(6, 19, 1, 125.00), (7, 20, 1, 115.00), (8, 4, 1, 250.00),
(9, 1, 1, 580.00), (11, 8, 1, 350.00), (12, 9, 2, 80.00);

-- 7. Envios (10)
INSERT INTO Envios (id_orden, paqueteria, codigo_rastreo, fecha_envio) VALUES
(1, 'DHL', 'DHL123456', '2023-01-02'),
(2, 'FedEx', 'FDX987654', '2023-01-03'),
(3, 'Estafeta', 'EST112233', '2023-01-05'),
(5, 'DHL', 'DHL654321', '2023-01-10'),
(6, 'Correos', 'COR998877', '2023-01-12'),
(7, 'FedEx', 'FDX445566', '2023-01-15'),
(9, 'DHL', 'DHL777888', '2023-01-20'),
(10, 'Estafeta', 'EST223344', '2023-01-22'),
(12, 'DHL', 'DHL999000', '2023-02-01'),
(13, 'FedEx', 'FDX111222', '2023-02-05');

-- 8. Resenas (10)
INSERT INTO Resenas (id_producto, id_cliente, calificacion, comentario) VALUES
(1, 1, 5, 'Excelente procesador, muy rápido.'),
(5, 1, 5, 'Una bestia para gaming 4K.'),
(8, 2, 4, 'Buena relación calidad precio.'),
(9, 4, 5, 'El SSD más rápido que he tenido.'),
(15, 6, 3, 'Cumple su función, pero hay mejores.'),
(17, 1, 5, 'Silenciosa y potente.'),
(2, 3, 5, 'AMD hizo un gran trabajo.'),
(12, 10, 4, 'Buen precio por 1TB.'),
(6, 3, 5, 'Muy cara pero vale la pena.'),
(7, 9, 1, 'Drivers inestables al principio.');