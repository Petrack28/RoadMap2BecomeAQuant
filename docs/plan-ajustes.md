# 🔧 Ajustes al plan — auditoría de mitad de camino

> Acordado tras la auditoría de la Semana 10. Estos ajustes corrigen los huecos
> detectados sin cambiar la estructura del roadmap.

## 1. Green Book — sesión quincenal de entrevista simulada
- **Cada 2 semanas, 1 sesión completa** dedicada solo a resolver problemas del
  Green Book en voz alta, con el profesor simulando entrevistador.
- Cubrir la deuda actual en este orden: Cap. 2 (verificar los asignados),
  Cap. 3 (nunca revisado), Cap. 4 (completar), Cap. 5 (nunca revisado).
- Regla: los problemas de tarea se **resuelven por escrito en 00-notes/green-book/**
  (intento propio + solución final), no solo se marcan como hechos.

## 2. Mental math — entrenamiento diario por mi cuenta
- 10 min diarios de aritmética cronometrada (Zetamac o similar).
- Registrar el score 1 vez por semana en el class log para medir progreso.
- Meta: consistencia antes que velocidad las primeras 2 semanas.

## 3. Deudas técnicas específicas a saldar
- [ ] Bootstrap formal (pospuesto en Semana 3) — sesión corta dedicada
- [ ] Problemas de Itô del Green Book Cap. 5 (teoría vista, práctica no)
- [ ] Block bootstrap para el Hurst (mejora al Proyecto 2, documentada como limitación)

## 4. Cambio de formato: yo escribo el código primero
- Desde la Semana 11 en adelante: el profesor plantea el ejercicio y **yo escribo
  el primer intento de código**, luego se corrige juntos.
- El profesor solo da código completo en setup/boilerplate (descargas, configuración),
  no en la lógica central del ejercicio.

## 5. Recursos externos — verificación real
- Las tareas de video (3Blue1Brown, Stat 110) ahora incluyen **1-2 preguntas de
  comprensión al inicio de la siguiente clase** — si no se vieron, se reasignan
  sin drama, pero el class log refleja la realidad.

## Métricas de éxito de estos ajustes (revisar en 4 semanas)
- ≥ 8 problemas del Green Book resueltos por escrito en el repo
- Score de mental math registrado ≥ 3 veces
- Deudas técnicas: al menos 2 de 3 saldadas
- Código de ejercicios centrales escrito primero por mí en ≥ 80% de los casos


## 6. Línea de investigación de trading personal (integrada, no paralela)

> Acordado en Semana 10-11. Las hipótesis de trading propias se convierten en
> los vehículos de los proyectos del roadmap — sin alterar su estructura.

### Hipótesis a investigar
1. **London Breakout (EUR/USD):** la ruptura del rango de la sesión asiática
   al abrir Londres tiene continuación estadísticamente significativa.
   Fundamento: concentración documentada de liquidez/volatilidad en el
   overlap Londres-NY.
2. **IFVG / Fair Value Gaps (concepto ICT operacionalizado):** definir el
   FVG con reglas 100% geométricas y objetivas (gap entre high de vela 1
   y low de vela 3) y testear si su relleno/inversión tiene edge medible.
   Sin ambigüedad interpretativa: si una regla no se puede codificar, no
   entra al test.

### Integración con el roadmap
| Semana | Proyecto | Vehículo |
|---|---|---|
| 11 | Proyecto 6 (Pine Script) | London Breakout en EUR/USD |
| 12 | Proyecto 7 (Walk-forward) | Validación de Breakout + IFVG |
| 22 | Proyecto 12 (Paper trading) | Lo que sobreviva la validación → ruta prop firm |

### Reglas de protección del roadmap
- Las semanas 13-21 (GARCH, pairs trading, opciones, ML, C++) NO se saltan
  ni se posponen por perseguir estrategias — son la formación que diferencia
  a un quant de un trader retail con backtests.
- Criterio de honestidad: si una hipótesis no sobrevive la validación de la
  Semana 12 (significancia, costos, out-of-sample), se documenta como
  resultado negativo en el portafolio y NO se opera. Un resultado negativo
  bien documentado es un proyecto válido.
- Nada de dinero real durante el roadmap. La ruta es: validación → paper
  trading (Sem. 22) → evaluación de prop firm solo con evidencia acumulada.