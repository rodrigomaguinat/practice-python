# 📚 Sistema de Gestión de Biblioteca

## 📋 Reunión inicial

**Cliente:** Biblioteca Central de la Universidad San Miguel

**Proyecto:** Sistema de Gestión de Biblioteca

---

# 🤝 Primera reunión

Hola, necesitamos un sistema para administrar nuestra biblioteca. Actualmente todo lo hacemos en un cuaderno y en hojas de Excel, y constantemente tenemos problemas con los préstamos y las devoluciones.

---

# 🚨 El problema

Actualmente contamos aproximadamente con:

- 📚 2,500 libros
- 👨‍🎓 700 estudiantes registrados
- 🔄 40 préstamos diarios

### Problemas actuales

- No sabemos exactamente quién tiene un libro.
- Algunos estudiantes dicen que devolvieron un libro, pero no encontramos el registro.
- Prestamos un mismo libro a dos personas por error.
- Hay libros perdidos.
- No sabemos qué libros son los más solicitados.
- Buscar un libro toma mucho tiempo.

### Objetivo

Queremos que todo este proceso se realice mediante un programa que permita administrar la biblioteca de forma organizada y segura.

---

# 🎯 ¿Qué necesito que haga el sistema?

Como encargado de la biblioteca necesito poder administrar todo desde un solo lugar.

---

# 1. Registrar libros

Cuando compramos un libro nuevo quiero poder registrarlo.

Cada libro debe almacenar la siguiente información:

- Código interno
- ISBN
- Título
- Autor
- Editorial
- Año de publicación
- Categoría
- Cantidad de ejemplares

### Ejemplo

```text
Código: LIB-0001

Título:
Clean Code

Autor:
Robert Martin

Editorial:
Prentice Hall

Año:
2008

Categoría:
Programación

Cantidad:
4
```

---

# 2. Buscar libros

Los estudiantes siempre preguntan:

> ¿Tiene este libro?

Por ello necesito que el sistema permita realizar búsquedas por:

- Título
- Autor
- Categoría
- ISBN

---

# 3. Registrar estudiantes

Los alumnos deben estar registrados antes de poder solicitar préstamos.

Cada estudiante tendrá la siguiente información:

- Código
- Nombres
- Apellidos
- Correo electrónico
- Carrera
- Ciclo
- Teléfono

---

# 4. Prestar un libro

Este es el proceso más importante del sistema.

Cuando llega un estudiante y solicita un libro, por ejemplo:

> Quiero llevarme **"Python para Todos"**.

Yo quiero seleccionar al estudiante y luego seleccionar el libro.

El sistema debe verificar automáticamente:

- Que el estudiante exista.
- Que el libro exista.
- Que haya ejemplares disponibles.
- Que el estudiante no tenga multas pendientes.
- Que el estudiante no haya alcanzado el máximo de préstamos permitidos.

Si todas las validaciones son correctas, el sistema deberá registrar el préstamo.

---

# 5. Límite de préstamos

No quiero que un estudiante pueda llevar más de **3 libros** al mismo tiempo.

Si intenta solicitar un cuarto libro, deberá mostrarse el siguiente mensaje:

```text
No puede prestar más libros.
```

---

# 6. Fecha de devolución

Cada vez que se registre un préstamo, el sistema deberá almacenar:

- Fecha del préstamo
- Fecha límite de devolución

### Ejemplo

```text
Fecha préstamo:
20 de marzo

Fecha límite:
27 de marzo
```

---

# 7. Devolver un libro

Cuando el estudiante regrese un libro quiero seleccionar:

- Estudiante
- Libro

El sistema deberá:

- Registrar la devolución.
- Incrementar nuevamente la cantidad de ejemplares disponibles.
- Finalizar el préstamo.

---

# 8. Libros vencidos

Todos los días quiero consultar qué estudiantes tienen préstamos vencidos.

### Ejemplo

```text
Estudiante:
Carlos

Libro:
Clean Code

Debía devolver:
12 de marzo

Tiene:
8 días de retraso
```

---

# 9. Historial de préstamos

Necesito consultar todo el historial de préstamos de un estudiante.

### Ejemplo

```text
Juan Pérez

Libro:
Python para Todos

Prestó:
10 de marzo

Devolvió:
17 de marzo

----------------------------

Libro:
Algoritmos

Prestó:
25 de marzo

Estado:
Devuelto
```

---

# 10. Reportes

El sistema deberá generar reportes como:

- Libros más prestados.
- Estudiantes con mayor cantidad de préstamos.
- Libros que nunca fueron prestados.
- Libros disponibles.
- Libros sin ejemplares disponibles.
- Estudiantes con multas pendientes.

---

# 📜 Restricciones del negocio

Estas reglas son obligatorias y el sistema debe cumplirlas.

## Regla 1

Un estudiante no puede tener más de **tres préstamos activos** al mismo tiempo.

---

## Regla 2

Un libro solo podrá prestarse si existen ejemplares disponibles.

---

## Regla 3

Cada préstamo tendrá una duración máxima de **siete días**.

---

## Regla 4

Si un estudiante tiene un préstamo vencido, no podrá realizar nuevos préstamos hasta regularizar su situación.

---

## Regla 5

Todo préstamo debe quedar registrado permanentemente en el historial, incluso después de haber sido devuelto.

---

## Regla 6

No se podrá eliminar un estudiante que tenga préstamos activos.

---

## Regla 7

No se podrá eliminar un libro que actualmente se encuentre prestado.

---

# 💻 Lo que espero del programa

Como bibliotecario necesito que el sistema sea sencillo e intuitivo.

El menú principal podría verse de la siguiente manera:

```text
======== BIBLIOTECA ========

1. Registrar libro
2. Registrar estudiante
3. Buscar libro
4. Buscar estudiante
5. Prestar libro
6. Devolver libro
7. Mostrar libros
8. Mostrar estudiantes
9. Reportes
10. Salir
```