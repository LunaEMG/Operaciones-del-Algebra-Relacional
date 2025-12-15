# **Prácticas 7, 8 y 9: "Operaciones del Álgebra Relacional"**

Bienvenido al repositorio de las practicas 7, 8 y 9 de la materia de Bases de Datos. Este sistema ha sido diseñado para simular la gestión integral de una tienda especializada en componentes de PC, abarcando desde el control de stock hasta el análisis financiero de los productos.

---

## **🚀 Arquitectura y Despliegue**

**El sistema está completamente Dockerizado**. Esto asegura que cualquier usuario pueda desplegar la base de datos y la aplicación cliente en cuestión de segundos, sin preocuparse por dependencias locales o versiones de software. El archivo `docker-compose.yml` orquesta la comunicación entre el contenedor de la base de datos y la interfaz de control.

Se ha implementado un **Menú Interactivo (CLI)**. A diferencia de ejecutar scripts SQL sueltos, esta interfaz de línea de comandos ofrece una experiencia de usuario fluida, permitiendo navegar por el catálogo de operaciones, ejecutar cualquiera de las 20 consultas disponibles y visualizar los resultados formateados en tiempo real.

---

## **🛠️ Instrucciones de Puesta en Marcha**

Para iniciar el sistema, simplemente clona este repositorio y utiliza Docker Compose para levantar la infraestructura.

### **1. Descarga el código fuente**

```bash
git clone https://github.com/LunaEMG/Operaciones-del-Algebra-Relacional.git
cd Operaciones-del-Algebra-Relacional
```

### **2. Construye y lanza los contenedores**

```bash
docker-compose run --rm --service-ports app
```

Una vez finalizada la construcción, la terminal te mostrará automáticamente el menú principal para comenzar a interactuar con la base de datos.

---

## **📚 Análisis Detallado de Consultas**

A continuación, presento el desglose de las 20 operaciones que el sistema es capaz de realizar. Cada una incluye una explicación de su utilidad en un contexto de negocio real, su formulación matemática y el código SQL correspondiente.

---

## **GRUPO 1: Gestión de Inventario y Filtrado Básico**

### **1. Alerta de Stock Crítico**
Esta consulta es vital para la logística diaria. Su objetivo es identificar aquellos productos cuyo nivel de existencias ha descendido por debajo del umbral de seguridad (30 unidades). Esto permite al gerente de compras reaccionar rápidamente y generar órdenes de reabastecimiento antes de que el producto se agote.

- **Álgebra Relacional:**  
  $\\sigma_{stock < 30}(Productos)$
- **SQL:**
```sql
SELECT * FROM Productos WHERE stock < 30;
```

---

### **2. Segmentación de Productos Premium**
Aquí nos enfocamos en el segmento de lujo. Filtramos el catálogo para mostrar únicamente aquellos componentes de gama alta cuyo valor supera los $1000. Esto es útil para campañas de marketing dirigidas a entusiastas o profesionales que buscan el máximo rendimiento.

- **Álgebra Relacional:**  
  $\\sigma_{precio > 1000}(Productos)$
- **SQL:**
```sql
SELECT * FROM Productos WHERE precio > 1000;
```

---

### **3. Filtrado por Categoría Específica**
En una tienda con miles de ítems, la organización es clave. Esta consulta aísla un subconjunto específico del inventario: las Tarjetas de Video (identificadas con el ID 2). Permite a los vendedores acceder rápidamente a todos los modelos de GPUs disponibles sin distracciones.

- **Álgebra Relacional:**  
  $\\sigma_{id_categoria = 2}(Productos)$
- **SQL:**
```sql
SELECT * FROM Productos WHERE id_categoria = 2;
```

---

### **4. Búsqueda por Rango de Presupuesto**
La mayoría de los clientes llegan con un presupuesto definido. Esta operación permite encontrar productos que se ajusten a un rango de precio medio, específicamente entre $500 y $1200, facilitando la recomendación de productos que equilibran costo y beneficio.

- **Álgebra Relacional:**  
  $\\sigma_{precio \\geq 500 \\land precio \\leq 1200}(Productos)$
- **SQL:**
```sql
SELECT * FROM Productos WHERE precio BETWEEN 500 AND 1200;
```

---

### **5. Búsqueda de Productos por Nombre**
Implementamos una búsqueda flexible basada en patrones de texto. Esta consulta localiza cualquier producto que contenga la cadena "RTX" en su nombre, lo cual es fundamental para los sistemas de búsqueda donde el usuario no recuerda el nombre exacto del modelo.

- **SQL:**
```sql
SELECT * FROM Productos WHERE nombre LIKE '%RTX%';
```

---

## **GRUPO 2: Proyecciones y Cálculos Financieros**

### **6. Catálogo de Precios Simplificado**
A veces no necesitamos todos los detalles técnicos de la base de datos. Esta proyección genera una lista limpia que muestra únicamente el nombre del producto y su precio, ideal para generar listas de precios físicas o catálogos rápidos para clientes.

- **Álgebra Relacional:**  
  $\\pi_{nombre, precio}(Productos)$
- **SQL:**
```sql
SELECT nombre, precio FROM Productos;
```

---

### **7. Simulación de Campaña de Descuentos**
Esta consulta permite previsualizar escenarios de ventas. Calculamos dinámicamente cómo quedarían los precios si aplicáramos un descuento global del 10% a todo el inventario, sin modificar los datos reales de la base de datos.

- **SQL:**
```sql
SELECT nombre, precio, (precio * 0.9) AS precio_descuento FROM Productos;
```

---

### **8. Valoración de Activos en Bodega**
Desde una perspectiva contable, es crucial saber cuánto dinero está "parado" en el almacén. Esta operación multiplica el precio unitario por la cantidad en stock de cada producto para determinar el valor total de los activos por ítem.

- **SQL:**
```sql
SELECT nombre, (precio * stock) AS valor_total FROM Productos;
```

---

### **9. Reporte de Productos Agotados**
Identifica los productos que tienen cero unidades disponibles. A diferencia de la alerta de stock bajo, esta lista muestra las ventas perdidas actuales y requiere acción inmediata para retirar el producto del catálogo web o marcarlo como "No Disponible".

- **Álgebra Relacional:**  
  $\\sigma_{stock = 0}(Productos)$
- **SQL:**
```sql
SELECT * FROM Productos WHERE stock = 0;
```

---

### **10. Consulta de Proveedores Específicos**
Permite acceder a la información de contacto y detalles de un proveedor en particular mediante su ID. Es una operación básica de mantenimiento de relaciones con la cadena de suministro.

- **SQL:**
```sql
SELECT * FROM Proveedores WHERE id_proveedor = 1;
```

---

## **GRUPO 3: Relaciones entre Entidades (Joins)**

### **11. Enriquecimiento de Datos de Producto**
En la tabla de productos solo guardamos IDs numéricos para ahorrar espacio. Esta consulta utiliza un JOIN para recuperar el nombre textual de la categoría desde su propia tabla, presentando al usuario una vista comprensible (ej. "Tarjeta Gráfica" en lugar de "2").

- **Álgebra Relacional:**  
  $\\pi_{P.nombre, C.nombre}(Productos \\bowtie Categorias)$
- **SQL:**
```sql
SELECT P.nombre, C.nombre_categoria
FROM Productos P
JOIN Categorias C ON P.id_categoria = C.id;
```

---

### **12. Relación Producto-Proveedor**
Es esencial saber quién nos surte cada componente. Al unir la tabla de productos con la de proveedores, podemos generar un reporte que asocia cada ítem con la empresa responsable de su garantía y suministro.

- **SQL:**
```sql
SELECT P.nombre, Pr.nombre_proveedor
FROM Productos P
JOIN Proveedores Pr ON P.id_proveedor = Pr.id;
```

---

### **13. Vista Maestra del Inventario**
Esta es una de las consultas más completas del sistema. Realiza múltiples uniones para crear una "súper tabla" que muestra el producto junto con los nombres reales tanto de su categoría como de su proveedor, ofreciendo una visión holística de cada ítem.

```sql
SELECT P.nombre, C.nombre_categoria, Pr.nombre_proveedor
FROM Productos P
JOIN Categorias C ON P.id_categoria = C.id
JOIN Proveedores Pr ON P.id_proveedor = Pr.id;
```

---

### **14. Identificación de Categorías de Alto Valor**
Queremos saber qué familias de productos contienen artículos de lujo. Esta consulta filtra las categorías que poseen al menos un producto con precio superior a $1500, ayudando a identificar qué secciones de la tienda generan mayor margen.

```sql
SELECT DISTINCT C.nombre_categoria
FROM Categorias C
JOIN Productos P ON C.id = P.id_categoria
WHERE P.precio > 1500;
```

---

### **15. Catálogo por Marca (Proveedor)**
Esta operación permite listar todos los productos suministrados por un fabricante específico, como "AMD". Es útil para revisar el rendimiento de una marca particular dentro de nuestra tienda.

```sql
SELECT P.nombre
FROM Productos P
JOIN Proveedores Pr ON P.id_proveedor = Pr.id
WHERE Pr.nombre_proveedor = 'AMD';
```

---

## **GRUPO 4: Análisis Avanzado y Estadísticas**

### **16. Dimensionamiento del Catálogo**
Una métrica simple pero fundamental. Nos devuelve el conteo total de SKUs (referencias únicas) registrados en el sistema, dándonos una idea del tamaño de nuestra base de datos.

```sql
SELECT COUNT(*) AS total_productos FROM Productos;
```

---

### **17. Análisis de Precio Promedio**
Calcula el precio medio de todos los productos en la tienda. Este indicador sirve como base para evaluar si nuestra tienda se posiciona como una opción económica o una boutique de alta gama.

```sql
SELECT AVG(precio) AS precio_promedio FROM Productos;
```

---

### **18. Identificación del Producto Estrella**
Mediante una subconsulta, localizamos el producto más costoso del inventario. Este ítem suele ser el "flagship" o buque insignia de la tienda y requiere estrategias de venta y seguridad especiales.

```sql
SELECT *
FROM Productos
WHERE precio = (SELECT MAX(precio) FROM Productos);
```

---

### **19. Distribución de Inventario por Categoría**
Esta consulta de agrupación nos permite ver qué tan equilibrado está nuestro catálogo, contando cuántos productos tenemos en cada categoría (ej. cuántos procesadores vs. cuántas memorias RAM).

```sql
SELECT id_categoria, COUNT(*)
FROM Productos
GROUP BY id_categoria;
```

---

### **20. Productos sobre la Media del Mercado**
Utilizando una subconsulta avanzada, filtramos aquellos productos cuyo precio es superior al promedio general de la tienda. Esto separa estadísticamente los productos "premium" de los productos "estándar".

- **Cálculo Relacional de Tuplas:**  
  $\\{ t | P(t) \\land t.precio > AVG(P.precio) \\}$
- **SQL:**
```sql
SELECT *
FROM Productos
WHERE precio > (SELECT AVG(precio) FROM Productos);
```

---

## **📂 Estructura del Repositorio**

```text
src/
├── src/
│   ├── main.py          # Lógica del Menú Interactivo
│   └── database.py      # Conexión a BD
├── db/
│   └── init.sql         # Script de creación de tablas y datos semilla
├── Dockerfile           # Entorno Python
├── docker-compose.yml   # Orquestación (App + MySQL/Postgres)
└── README.md            # Este archivo
```

---

## **👤 Autoría**

Este proyecto fue desarrollado por **Luna Miguel Emmanuel**.


