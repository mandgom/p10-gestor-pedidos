# P10 - Gestor de Pedidos

## Problemas detectados
1. Funciones monolíticas que asumen múltiples responsabilidades.
2. Mezcla de interfaz por consola (print/input) con la lógica matemática.
3. Código repetido y ausencia de pruebas automatizadas y documentación.

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Uso de variables genéricas | Uso de nombres descriptivos e implementación de validaciones en la clase Cliente | `clientes.py` | "Mejora nombres de variables" |
| Código monolítico y acoplado | Extracción de lógica hacia `calcular_descuento()` y métodos dentro de `LineaPedido` | `pedidos.py` | "Extrae lógica de cálculo de pedidos" |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| `test_clientes.py` | Valida instanciación de cliente, control de email inválido y nombres vacíos. |
| `test_pedidos.py` | Comprueba subtotales, rechazo de cantidades a 0, cálculos de descuento exactos y sumatorio final de pedidos. |

## Analizador de código
Analizador usado: Ruff
Opciones configuradas:
1. line-length = 100
2. target-version = "py312"
3. select = ["E", "F", "W", "I"]

## Trabajo con Git y ramas
Rama creada: `refactor-descuentos`
Commits principales: "Refactoriza lógica de descuentos"
Fusión realizada: Fusión en local y push hacia remoto (`main`).

## Integración continua
Resultado del workflow: `python-ci.yml` configurado exitosamente en `ubuntu-latest`. Instalación, linting y pruebas superadas en verde.
