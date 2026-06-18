# Especificación: Módulo Calculadora

## Propósito

Proveer cuatro operaciones aritméticas básicas como funciones puras, sin estado y sin dependencias externas, para ser usadas como ejemplo de aplicación testeable en un pipeline de Integración Continua.

## Requisitos funcionales

### RF-01: Suma

- **Entrada:** dos números `a`, `b` (enteros o decimales)
- **Salida:** la suma de `a` y `b`
- **Criterio de aceptación:** `sumar(2, 3)` debe devolver `5`

### RF-02: Resta

- **Entrada:** dos números `a`, `b`
- **Salida:** la resta de `a` menos `b`
- **Criterio de aceptación:** `restar(5, 3)` debe devolver `2`

### RF-03: Multiplicación

- **Entrada:** dos números `a`, `b`
- **Salida:** el producto de `a` y `b`
- **Criterio de aceptación:** `multiplicar(4, 3)` debe devolver `12`

### RF-04: División

- **Entrada:** dos números `a`, `b`
- **Salida:** el cociente de `a` dividido `b`
- **Criterio de aceptación:** `dividir(10, 2)` debe devolver `5`

## Requisitos no funcionales

### RNF-01: Manejo de errores

El sistema **no debe permitir** la división por cero. Ante `b == 0` en la función `dividir`, se debe lanzar una excepción `ValueError` con un mensaje descriptivo, en lugar de devolver un resultado indefinido o provocar un error no controlado de Python.

### RNF-02: Pureza funcional

Ninguna función debe depender de estado externo (variables globales, archivos, entrada de usuario) ni producir efectos secundarios. Esto garantiza que el comportamiento sea determinístico y, por lo tanto, automatizable en un pipeline de CI.

## Trazabilidad: Especificación → Tests

| Requisito | Test que lo valida      |
| --------- | ----------------------- |
| RF-01     | `test_sumar`            |
| RF-02     | `test_restar`           |
| RF-03     | `test_multiplicar`      |
| RF-04     | `test_dividir`          |
| RNF-01    | `test_dividir_por_cero` |

## Notas

Esta especificación se escribió antes de implementar el código (`calculadora.py`), siguiendo el enfoque de Spec Driven Development: los requisitos formales preceden y guían tanto la implementación como los criterios de prueba.
