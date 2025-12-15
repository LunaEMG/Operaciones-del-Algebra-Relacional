# Definición de las 20 consultas complejas con sus equivalencias.

queries = [
    # --- GRUPO 1: OPERADORES BÁSICOS (Selección, Proyección, Conjuntos) ---
    {
        "id": 1,
        "categoria": "Operadores Básicos",
        "descripcion": "Seleccionar productos con stock menor a 30 (Alerta de Inventario)",
        "algebra": "σ stock < 30 (Productos)",
        "crt": "{ t | Productos(t) ∧ t.stock < 30 }",
        "crd": "{ <id, nom, prec, st, cat, prov> | Productos(id, nom, prec, st, cat, prov) ∧ st < 30 }",
        "sql": "SELECT * FROM Productos WHERE stock < 30;"
    },
    {
        "id": 2,
        "categoria": "Operadores Básicos",
        "descripcion": "Proyección de nombres y correos de Clientes",
        "algebra": "π nombre, email (Clientes)",
        "crt": "{ t.nombre, t.email | Clientes(t) }",
        "crd": "{ <nom, em> | ∃id, ap, f (Clientes(id, nom, ap, em, f)) }",
        "sql": "SELECT nombre, email FROM Clientes;"
    },
    {
        "id": 3,
        "categoria": "Operadores Básicos",
        "descripcion": "Unión: Nombres de empresas (Proveedores) y nombres de paqueterías (Envios) - Entidades Logísticas",
        "algebra": "π nombre_empresa (Proveedores) ∪ π paqueteria (Envios)",
        "crt": "{ t.nombre | (∃p (Proveedores(p) ∧ t.nombre = p.nombre_empresa)) ∨ (∃e (Envios(e) ∧ t.nombre = e.paqueteria)) }",
        "crd": "{ <n> | ∃id, em, p (Proveedores(id, n, em, p)) ∨ ∃id_e, ord, cod, f (Envios(id_e, ord, n, cod, f)) }",
        "sql": "SELECT nombre_empresa as entidad FROM Proveedores UNION SELECT paqueteria FROM Envios;"
    },
    {
        "id": 4,
        "categoria": "Operadores Básicos",
        "descripcion": "Diferencia: Productos que NO tienen ninguna reseña",
        "algebra": "π id_producto (Productos) - π id_producto (Resenas)",
        "crt": "{ t.id_producto | Productos(t) ∧ ¬∃r (Resenas(r) ∧ r.id_producto = t.id_producto) }",
        "crd": "{ <id> | ∃n, p, s, c, pr (Productos(id, n, p, s, c, pr)) ∧ ¬∃id_r, cl, cal, com, f (Resenas(id_r, id, cl, cal, com, f)) }",
        "sql": "SELECT id_producto, nombre FROM Productos WHERE id_producto NOT IN (SELECT id_producto FROM Resenas);"
    },
    {
        "id": 5,
        "categoria": "Operadores Básicos",
        "descripcion": "Intersección: Clientes que han comprado y también han dejado reseña",
        "algebra": "π id_cliente (Ordenes) ∩ π id_cliente (Resenas)",
        "crt": "{ t.id_cliente | (∃o (Ordenes(o) ∧ o.id_cliente = t.id_cliente)) ∧ (∃r (Resenas(r) ∧ r.id_cliente = t.id_cliente)) }",
        "crd": "{ <id> | ∃id_o, f, tot, est (Ordenes(id_o, id, f, tot, est)) ∧ ∃id_r, p, cal, com, fr (Resenas(id_r, p, id, cal, com, fr)) }",
        "sql": "SELECT DISTINCT id_cliente FROM Ordenes INTERSECT SELECT id_cliente FROM Resenas;"
    },

    # --- GRUPO 2: REUNIONES (Joins) ---
    {
        "id": 6,
        "categoria": "Reuniones",
        "descripcion": "Natural Join: Productos con sus nombres de Categoría",
        "algebra": "Productos ⋈ Categorias",
        "crt": "{ t | ∃p, c (Productos(p) ∧ Categorias(c) ∧ p.id_categoria = c.id_categoria ∧ t = (p ∪ c)) }",
        "crd": "Equivalente a listar todas las variables de ambas tablas igualando id_categoria",
        "sql": "SELECT P.nombre as Producto, C.nombre as Categoria FROM Productos P JOIN Categorias C ON P.id_categoria = C.id_categoria;"
    },
    {
        "id": 7,
        "categoria": "Reuniones",
        "descripcion": "Left Outer Join: Todos los Clientes y sus Ordenes (incluso si no tienen)",
        "algebra": "Clientes ⟕ Ordenes",
        "crt": "No estándar en CRT básico (requiere manejo de nulos)",
        "crd": "No estándar en CRD básico",
        "sql": "SELECT C.nombre, O.id_orden, O.total FROM Clientes C LEFT JOIN Ordenes O ON C.id_cliente = O.id_cliente;"
    },
    {
        "id": 8,
        "categoria": "Reuniones",
        "descripcion": "Theta Join: Productos más caros que el promedio de su categoría (Simulado con Join)",
        "algebra": "Productos ⋈ (precio > 1000) Proveedores",
        "crt": "{ t | ∃p, pr (Productos(p) ∧ Proveedores(pr) ∧ p.id_proveedor = pr.id_proveedor ∧ p.precio > 1000) }",
        "crd": "...",
        "sql": "SELECT P.nombre, P.precio, Pr.nombre_empresa FROM Productos P JOIN Proveedores Pr ON P.id_proveedor = Pr.id_proveedor WHERE P.precio > 1000;"
    },
    {
        "id": 9,
        "categoria": "Reuniones",
        "descripcion": "Reunión de 3 tablas: Detalle de orden con nombre de producto y cliente",
        "algebra": "(Clientes ⋈ Ordenes) ⋈ (Detalle_Orden ⋈ Productos)",
        "crt": "{ t.nombre_cliente, t.producto | ...complejo... }",
        "crd": "...",
        "sql": "SELECT C.nombre, P.nombre as producto, D.cantidad FROM Clientes C JOIN Ordenes O ON C.id_cliente = O.id_cliente JOIN Detalle_Orden D ON O.id_orden = D.id_orden JOIN Productos P ON D.id_producto = P.id_producto;"
    },
    {
        "id": 10,
        "categoria": "Reuniones",
        "descripcion": "Semi-Join: Proveedores que suministran productos con stock bajo (<20)",
        "algebra": "Proveedores ⋉ (σ stock<20 (Productos))",
        "crt": "{ t | Proveedores(t) ∧ ∃p (Productos(p) ∧ p.id_proveedor = t.id_proveedor ∧ p.stock < 20) }",
        "crd": "...",
        "sql": "SELECT * FROM Proveedores WHERE id_proveedor IN (SELECT id_proveedor FROM Productos WHERE stock < 20);"
    },

    # --- GRUPO 3: AGRUPACIÓN Y AGREGACIÓN ---
    {
        "id": 11,
        "categoria": "Agregación",
        "descripcion": "Contar cuántos productos hay por Categoria",
        "algebra": "Categoria γ COUNT(id_producto) (Productos)",
        "crt": "No soportado directamente en CRT estándar",
        "crd": "No soportado directamente en CRD estándar",
        "sql": "SELECT C.nombre, COUNT(P.id_producto) FROM Categorias C JOIN Productos P ON C.id_categoria = P.id_categoria GROUP BY C.nombre;"
    },
    {
        "id": 12,
        "categoria": "Agregación",
        "descripcion": "Precio promedio de productos por Proveedor",
        "algebra": "Proveedor γ AVG(precio) (Productos)",
        "crt": "-",
        "crd": "-",
        "sql": "SELECT id_proveedor, AVG(precio) FROM Productos GROUP BY id_proveedor;"
    },
    {
        "id": 13,
        "categoria": "Agregación",
        "descripcion": "Total gastado por cada cliente (SUM)",
        "algebra": "id_cliente γ SUM(total) (Ordenes)",
        "crt": "-",
        "crd": "-",
        "sql": "SELECT id_cliente, SUM(total) as total_gastado FROM Ordenes GROUP BY id_cliente;"
    },
    {
        "id": 14,
        "categoria": "Agregación",
        "descripcion": "Encontrar la orden más costosa (MAX)",
        "algebra": "ℑ MAX(total) (Ordenes)",
        "crt": "-",
        "crd": "-",
        "sql": "SELECT MAX(total) FROM Ordenes;"
    },
    {
        "id": 15,
        "categoria": "Agregación",
        "descripcion": "Agrupación con HAVING: Categorías con más de 3 productos en catálogo",
        "algebra": "σ count > 3 (id_categoria γ COUNT(id_producto)->count (Productos))",
        "crt": "-",
        "crd": "-",
        "sql": "SELECT id_categoria, COUNT(*) FROM Productos GROUP BY id_categoria HAVING COUNT(*) > 3;"
    },

    # --- GRUPO 4: DIVISIÓN (Las consultas más complejas) ---
    {
        "id": 16,
        "categoria": "División",
        "descripcion": "Clientes que han comprado TODOS los productos de la categoría 'Fuentes de Poder' (ID 5)",
        "algebra": "π id_cliente, id_producto (Ventas_Completas) ÷ π id_producto (σ id_cat=5 (Productos))",
        "crt": "{ c | Clientes(c) ∧ ∀p ((Productos(p) ∧ p.id_cat=5) → ∃d,o (Detalle(d) ∧ Orden(o) ∧ d.id_prod=p.id ∧ d.id_ord=o.id ∧ o.id_cli=c.id)) }",
        "crd": "Complejo (ver PDF documentación)",
        "sql": """
        SELECT C.nombre 
        FROM Clientes C
        WHERE NOT EXISTS (
            SELECT P.id_producto 
            FROM Productos P 
            WHERE P.id_categoria = 5
            AND NOT EXISTS (
                SELECT 1 
                FROM Ordenes O 
                JOIN Detalle_Orden D ON O.id_orden = D.id_orden
                WHERE O.id_cliente = C.id_cliente 
                AND D.id_producto = P.id_producto
            )
        );
        """
    },
    {
        "id": 17,
        "categoria": "División",
        "descripcion": "Ordenes que contienen TODOS los productos del proveedor 'TechSupply Global' (ID 1)",
        "algebra": "Relación (Orden, Producto) ÷ Productos_de_Proveedor_1",
        "crt": "{ o | Ordenes(o) ∧ ∀p ((Productos(p) ∧ p.prov=1) → ∃d (Detalle(d) ∧ d.ord=o.id ∧ d.prod=p.id)) }",
        "crd": "-",
        "sql": """
        SELECT O.id_orden 
        FROM Ordenes O
        WHERE NOT EXISTS (
            SELECT P.id_producto 
            FROM Productos P 
            WHERE P.id_proveedor = 1
            AND NOT EXISTS (
                SELECT 1 
                FROM Detalle_Orden D 
                WHERE D.id_orden = O.id_orden 
                AND D.id_producto = P.id_producto
            )
        );
        """
    },
    {
        "id": 18,
        "categoria": "División",
        "descripcion": "Proveedores que han surtido al menos un producto en TODAS las ordenes realizadas el '2023-01-02'",
        "algebra": "División lógica compleja",
        "crt": "∀o (Fecha='2023-01-02' → ∃p (Producto(p) ∧ p.prov=Proveedor ∧ EstaEnOrden(p, o)))",
        "crd": "-",
        "sql": """
        SELECT Pr.nombre_empresa
        FROM Proveedores Pr
        WHERE NOT EXISTS (
            SELECT O.id_orden
            FROM Ordenes O
            WHERE O.fecha_orden = '2023-01-02'
            AND NOT EXISTS (
                SELECT 1
                FROM Detalle_Orden D
                JOIN Productos P ON D.id_producto = P.id_producto
                WHERE D.id_orden = O.id_orden
                AND P.id_proveedor = Pr.id_proveedor
            )
        );
        """
    },

    # --- GRUPO 5: CUANTIFICADORES UNIVERSALES (Lógica similar a División) ---
    {
        "id": 19,
        "categoria": "Cuantificador Universal",
        "descripcion": "Encontrar productos que han sido comprados por TODOS los clientes registrados (Best Sellers Absolutos)",
        "algebra": "R(prod, cli) ÷ Clientes",
        "crt": "{ p | Productos(p) ∧ ∀c (Clientes(c) → HaComprado(c, p)) }",
        "crd": "-",
        "sql": """
        SELECT P.nombre
        FROM Productos P
        WHERE NOT EXISTS (
            SELECT C.id_cliente
            FROM Clientes C
            WHERE NOT EXISTS (
                SELECT 1
                FROM Ordenes O
                JOIN Detalle_Orden D ON O.id_orden = D.id_orden
                WHERE O.id_cliente = C.id_cliente
                AND D.id_producto = P.id_producto
            )
        );
        """
    },
    {
        "id": 20,
        "categoria": "Cuantificador Universal",
        "descripcion": "Categorías donde TODOS sus productos tienen un stock mayor a 10",
        "algebra": "Selección universal",
        "crt": "{ c | Categorias(c) ∧ ∀p ((Productos(p) ∧ p.cat=c.id) → p.stock > 10) }",
        "crd": "-",
        "sql": """
        SELECT C.nombre
        FROM Categorias C
        WHERE NOT EXISTS (
            SELECT P.id_producto
            FROM Productos P
            WHERE P.id_categoria = C.id_categoria
            AND P.stock <= 10
        );
        """
    }
]

def get_queries():
    return queries