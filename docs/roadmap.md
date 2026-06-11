# 🎯 Roadmap Quant Definitivo — 6 meses (26 semanas)

> **Objetivo:** pasar de ingeniero biomédico con bases fuertes de señales/estadística a candidato quant competitivo, con portafolio real, experiencia en plataformas profesionales y preparación de entrevistas (Green Book).
>
> **Formato de cada semana:** 📚 Temas → 🎓 Dónde estudiarlo (recurso exacto) → 📗 Green Book → 🛠️ Práctica/Proyecto.
>
> **Ritmo:** ~10–12 h/semana (compatible con tesis). Distribución sugerida por semana: 5 h teoría · 4 h proyecto · 2 h Green Book.

---

## 1. Los 4 tipos de quant (elige tu énfasis)

| Rol | Qué hace | Énfasis del roadmap |
|---|---|---|
| **Quant Trader / sistemático** | Diseña y opera estrategias | Meses 3–4 + TradingView/QuantConnect |
| **Quant Researcher** | Investiga señales/alfa | Meses 1, 4, 5 + WorldQuant BRAIN |
| **Quant Developer** | Software, sistemas, latencia | Meses 5–6 (C++) + LEAN engine |
| **Quant pricing / riesgo** | Valúa derivados, riesgo | Mes 4 (Itô, Black-Scholes, Hull) |

No tienes que decidir hoy: los meses 1–3 son comunes a todos. Decide al llegar al mes 4.

---

## 2. Tu ventaja de partida

| Ya dominas | Reúso directo |
|---|---|
| Python + NumPy/Pandas | Todo el pipeline |
| Series temporales, DFA, filtros Butterworth | Volatilidad, regímenes, **exponente de Hurst** |
| Estadística (Shapiro-Wilk, t-test, Wilcoxon, Cohen's d) | Validación de estrategias |
| Álgebra lineal / cálculo de ingeniería | Optimización, procesos estocásticos |
| Streamlit, SQLite, APIs/OAuth | Dashboards, pipelines, conexión a brokers |
| MATLAB → Python (portaste DFA) | Implementar papers desde cero |

**Regla:** el tiempo que ahorras en lo que ya sabes, inviértelo en backtesting honesto y finanzas — lo que aún no conoces.

---

## 3. El Green Book — columna vertebral de entrevistas

📗 *A Practical Guide to Quantitative Finance Interviews* — **Xinfeng Zhou** (PhD en Applied Biosciences, MIT — llegó a quant desde ingeniería biomédica, como tú). +200 problemas reales de entrevista. Sus capítulos van mapeados semana a semana en el plan.

**Método:** (1) intenta cada problema solo antes de ver la solución; (2) reescribe la solución con tus palabras; (3) repite los fallados una semana después; (4) **Cap. 2 (brain teasers) = calentamiento de 15–20 min al inicio de cada sesión, los 6 meses**.

| Cap. | Tema | Cuándo |
|---|---|---|
| 1 | General Principles | Día 1 |
| 2 | Brain Teasers | Diario, todo el roadmap |
| 3 | Calculus & Linear Algebra | Sem. 1 |
| 4 | Probability (la sección estrella) | Sem. 2–3 |
| 5 | Stochastic Processes & Calculus | Sem. 4 y 15 |
| 6 | Finance | Sem. 7 y 15–16 |
| 7 | Algorithms & Numerical Methods | Sem. 17–20 |

---

# 📅 EL PLAN SEMANA A SEMANA

## MES 1 — Cimientos matemáticos

> La diferencia entre "hago backtests" y "soy quant". Con tu base, es más reorientación que aprendizaje desde cero.

### Semana 1 — Álgebra lineal y cálculo aplicados
- 📚 Eigenvalores/eigenvectores, descomposiciones, PCA; gradientes, optimización con restricciones (Lagrange).
- 🎓 ▶️ **3Blue1Brown** — *Essence of Linear Algebra* (visual, rápido para tu nivel). Refuerzo: MIT OCW 18.06 (Strang) en temas puntuales.
- 📗 Green Book Cap. 1 (día 1) + Cap. 3.
- 🛠️ PCA desde cero sobre matriz de retornos de 10 activos (descarga con `yfinance`). **Setup:** repo GitHub + cuenta TradingView + cuenta QuantConnect (gratis).

### Semana 2 — Probabilidad rigurosa
- 📚 Distribuciones (normal, log-normal, t-Student, colas pesadas), esperanza/varianza/momentos, TCL, ley de grandes números.
- 🎓 ▶️ **Harvard Stat 110** (Joe Blitzstein, YouTube, gratis; libro PDF gratis). El estándar de oro. Selecciona las lectures de estos temas, no es necesario el curso entero.
- 📗 Green Book Cap. 4 (dedícale tiempo extra: es lo más preguntado en entrevistas).
- 🛠️ Ajusta normal vs t-Student a retornos reales del S&P 500; QQ-plots y análisis de colas.

### Semana 3 — Estadística inferencial y regresión
- 📚 Pruebas de hipótesis (formaliza lo que ya usas), regresión múltiple y diagnósticos, bootstrap.
- 🎓 ▶️ **StatQuest** (regresión, bootstrap) + `statsmodels` docs.
- 📗 Green Book Cap. 4 (termina los problemas).
- 🛠️ **Proyecto 1 — Análisis de factores:** regresión de retornos de un activo contra factores de mercado (CAPM / Fama-French simple). Reporta betas, R², significancia.

### Semana 4 — Procesos estocásticos
- 📚 Cadenas de Markov, paseo aleatorio, **movimiento Browniano**, intuición del **cálculo de Itô**, proceso Ornstein-Uhlenbeck.
- 🎓 ▶️ **MIT OCW 18.S096/18.642 — *Topics in Mathematics with Applications in Finance*** (gratis, con videos; lectures de stochastic processes e Itô). Complemento: serie de stochastic calculus de **QuantPy**.
- 📗 Green Book Cap. 5 (primera pasada).
- 🛠️ Simula GBM y O-U en Python; estima el exponente de Hurst de ambos con **tu DFA** y verifica que distingue trending vs mean-reverting. (Proyecto puente perfecto entre tu tesis y quant.)

---

## MES 2 — Finanzas y mercados

### Semana 5 — Mercados, instrumentos y microestructura
- 📚 Tipos de órdenes, libro de órdenes, bid-ask, liquidez, slippage; acciones/futuros/FX/cripto/opciones (panorama); por qué importa la microestructura.
- 🎓 🔗 Khan Academy *Finance & Capital Markets* (selectivo) + Investopedia como diccionario + primeras lectures del MIT 18.642 (overview de mercados, dadas por practicantes de la industria).
- 📗 Brain teasers diarios (ya es hábito).
- 🛠️ Explora el libro de órdenes en TradingView; documenta en tu repo un "glosario quant" propio (te servirá para entrevistas).

### Semana 6 — Series temporales financieras
- 📚 Log returns, estacionariedad (ADF), ACF/PACF, volatilidad rolling/anualizada, hechos estilizados (fat tails, clustering).
- 🎓 📘 **Udemy: Quantitative Finance & Algorithmic Trading in Python** (empieza aquí; cubre los meses 2 en orden) + Hilpisch *Python for Finance* como referencia.
- 🛠️ **Proyecto 2 — EDA cuantitativo:** notebook profesional de un activo: distribución, normalidad (tu Shapiro-Wilk), ACF, volatilidad, **Hurst vía DFA**. Este es tu proyecto "firma": une tesis y quant.

### Semana 7 — Teoría de portafolio y riesgo
- 📚 Markowitz, frontera eficiente; Sharpe, Sortino, Calmar, max drawdown, CAGR; CAPM, beta/alpha; VaR.
- 🎓 Mismo curso de Udemy (sección de portfolio theory) + MIT 18.642 (lecture de portfolio management).
- 📗 Green Book Cap. 6 (primeros problemas de finanzas).
- 🛠️ **Proyecto 3 — Optimizador de portafolio:** frontera eficiente y máximo Sharpe con `scipy.optimize`, visualizado en **Streamlit**.

### Semana 8 — Simulación y dimensionamiento
- 📚 GBM, Monte Carlo, Kelly Criterion, position sizing, probabilidad de ruina.
- 🎓 Mismo curso de Udemy (sección Monte Carlo) + ▶️ QuantPy (Kelly).
- 🛠️ **Proyecto 4 — Monte Carlo de riesgo:** simula trayectorias de equity con distintos sizing (Kelly completo vs fraccionario) y compara drawdowns esperados.

---

## MES 3 — Estrategias y backtesting riguroso ⭐

> El corazón del roadmap. Aquí muere el 90% de las estrategias — y se forma el criterio que te diferencia.

### Semana 9 — Diseño de estrategias e indicadores
- 📚 Momentum/trend-following vs mean-reversion; medias móviles, RSI, Bollinger, ATR **desde primeros principios** (impleméntalos tú, no cajas negras).
- 🎓 ▶️ **NeuroTrader** y **Part Time Larry** (YouTube) + Ernest Chan *Quantitative Trading* (caps. 1–3).
- 🛠️ Cruce de medias móviles vectorizado en pandas, con señales y retornos de la estrategia.

### Semana 10 — Backtesting en Python
- 📚 Vectorizado vs event-driven; métricas completas (equity curve, profit factor, win rate, exposure).
- 🎓 🔗 **Documentación oficial de `backtesting.py`** (kernc.github.io/backtesting.py — ejemplos listos) y de **`vectorbt`** para barridos de parámetros.
- 🛠️ **Proyecto 5 — Motor de backtesting:** tu estrategia de la sem. 9 en `backtesting.py` con reporte completo de métricas y costos de transacción.

### Semana 11 — TradingView y Pine Script
- 📚 Pine Script v6: `strategy()`, `ta.*`, entradas/salidas, stops, trailing; leer el Strategy Tester.
- 🎓 🔗 **Pine Script v6 User Manual** (oficial) + ▶️ **The Art of Trading** + repos de **PineCoders** (buenas prácticas).
- 🛠️ **Proyecto 6 — Python ↔ Pine Script:** replica tu estrategia en Pine y **compara resultados trade por trade**. Las discrepancias te enseñarán más que cualquier curso (fills, comisiones, lookahead).

### Semana 12 — Validación honesta
- 📚 Overfitting, lookahead bias, **repainting** (Pine), survivorship bias, costos realistas; **walk-forward analysis**.
- 🎓 📘 López de Prado *Advances in Financial ML* (caps. de backtesting/validación) + artículos de PineCoders sobre repainting.
- 🛠️ **Proyecto 7 — Walk-forward + robustez:** in-sample/out-of-sample, sensibilidad a parámetros, y pregunta clave con tu estadística: ¿el Sharpe out-of-sample es significativo o ruido?

---

## MES 4 — Modelos avanzados y derivados

### Semana 13 — Volatilidad y regímenes
- 📚 ARCH/GARCH, pronóstico de volatilidad, detección de regímenes.
- 🎓 🔗 Documentación de la librería **`arch`** (Kevin Sheppard) + lecture de volatility modeling del MIT 18.642.
- 🛠️ Pronóstico GARCH de volatilidad; compara contra volatilidad realizada.

### Semana 14 — Mean reversion estadístico y pairs trading
- 📚 Cointegración (Engle-Granger), z-score del spread, O-U aplicado.
- 🎓 📘 Ernest Chan *Algorithmic Trading* (capítulo de mean reversion/pairs) + `statsmodels` (coint).
- 🛠️ **Proyecto 8 — Pairs trading:** busca pares cointegrados en un sector, backtestea la estrategia de spread con costos. Valídala con walk-forward (sem. 12).

### Semana 15 — Opciones y Black-Scholes
- 📚 Calls/puts, paridad put-call, **Black-Scholes** (derivación e intuición), las **Griegas**.
- 🎓 📘 **Hull, *Options, Futures and Other Derivatives*** (la referencia) + ▶️ QuantPy (implementación en Python).
- 📗 Green Book Cap. 5 (Itô aplicado a BS) y Cap. 6 (problemas de opciones).
- 🛠️ Valuador Black-Scholes propio + visualización de las Griegas en función de S, σ, T.

### Semana 16 — Métodos numéricos de pricing
- 📚 Pricing por Monte Carlo y árboles binomiales; volatilidad implícita y su superficie.
- 🎓 📘 Hilpisch (capítulos de valuación numérica).
- 🛠️ **Proyecto 9 — Valuador de opciones:** Monte Carlo + binomial + cálculo de volatilidad implícita (Newton-Raphson). Compara contra BS analítico.

---

## MES 5 — ML/DL y programación quant

### Semana 17 — ML para trading (hecho bien)
- 📚 Leakage, no-estacionariedad; feature engineering financiero; etiquetado **triple-barrier**; **purged k-fold CV**.
- 🎓 📘 López de Prado (caps. 2–7) + 📘 Udemy *Machine Learning for Quant Finance and Algorithmic Trading*.
- 📗 Green Book Cap. 7 (algoritmos).
- 🛠️ Dataset de features (¡tus 54 features por bloque de la tesis son la misma lógica!) + etiquetas triple-barrier.

### Semana 18 — Modelos ML y señales
- 📚 Random Forest, XGBoost, importancia de features, predicción → señal → sizing.
- 🎓 Mismo curso + ▶️ StatQuest si necesitas reforzar la teoría de árboles/boosting.
- 🛠️ **Proyecto 10 — Estrategia ML completa:** entrenamiento con purged CV, backtesting con costos, comparación honesta vs buy & hold.

### Semana 19 — Deep Learning para series temporales
- 📚 LSTM/GRU, atención (panorama); cuándo el DL ayuda y cuándo solo sobreajusta (spoiler: casi siempre en finanzas con pocos datos).
- 🎓 🔗 Tutoriales oficiales de **PyTorch** para series temporales.
- 🛠️ LSTM para pronóstico de volatilidad (más realista que predecir precio); evalúa contra el GARCH de la sem. 13.

### Semana 20 — C++ para quant *(opcional según rol)*
- 📚 Por qué C++ en quant dev/HFT; sintaxis esencial, STL, gestión de memoria.
- 🎓 🔗 **learncpp.com** (gratis, el mejor recurso autodidacta).
- 🛠️ **Proyecto 11 — BS en C++:** reimplementa tu valuador Black-Scholes y haz benchmark vs Python.
- ↪️ *Si no apuntas a quant dev:* sustituye por más alphas en WorldQuant BRAIN (ver sección 4) o ejecución/optimización de portafolio.

---

## MES 6 — Producción, aplicación real y empleabilidad

### Semana 21 — Datos y pipelines
- 📚 Fuentes (`yfinance`, `ccxt`, Alpaca, Polygon), almacenamiento, limpieza, automatización.
- 🎓 🔗 Docs de Alpaca y ccxt + ▶️ Part Time Larry (APIs de brokers).
- 🛠️ Pipeline automatizado: descarga diaria → SQLite → validación de datos. (Tu experiencia de PaperMind aplica directo.)

### Semana 22 — Paper trading y ejecución
- 📚 Anatomía de un bot: data → señal → orden → riesgo → logging; riesgo operativo.
- 🎓 🔗 Docs de **Alpaca paper trading** (API sencilla y gratuita) + QuantConnect para deployment alternativo.
- 🛠️ **Proyecto 12 — Bot de paper trading** de una estrategia que sobrevivió tu walk-forward.

### Semana 23 — Capstone
- 🛠️ **Proyecto 13 — Capstone end-to-end:** idea → investigación → backtesting riguroso → walk-forward → paper trading → reporte estilo paper de investigación (abstract, metodología, resultados, limitaciones). Tu formato de tesis CINVESTAV es exactamente este músculo.

### Semana 24 — Portafolio y visibilidad
- 🛠️ README profesionales en cada repo (problema → datos → método → resultados → limitaciones); dashboard Streamlit como vitrina; 1–2 posts técnicos (LinkedIn/Medium) explicando un proyecto.

### Semana 25 — Repaso integral con el Green Book
- 📗 **Segunda pasada completa cronometrada**, resolviendo en voz alta como en entrevista. Prioriza caps. 2 y 4. Repite los fallados.
- 🎓 Complementos: *Heard on the Street* (Crack) + mental math si apuntas a prop shops.
- 🛠️ Simulacros: defiende tus 13 proyectos ante preguntas de "¿por qué decidiste X?" y "¿qué limitaciones tiene?".

### Semana 26 — Especialización y siguientes pasos
- Elige rama (research/dev/pricing/trading) y profundiza.
- Decide: ¿competencias (IQC de WorldQuant, Quant League), certificación (EPAT), aplicaciones a roles?

---

# 4. 🤖 Ruta de bots de trading (tu track de algo-trading)

> Tu objetivo no es solo entender quant: es **operar sistemas**. Esta es la progresión de bots que construyes a lo largo del roadmap, cada uno apoyado en lo que ya aprendiste. La regla de hierro: **un bot solo se construye sobre una estrategia que sobrevivió la validación de la semana 12**. Un bot con una estrategia sobreajustada es solo una forma automatizada de perder dinero.

### La escalera de bots (de menor a mayor autonomía)

**Nivel 0 — Estrategia backtesteada (Mes 3).** Tu estrategia en `backtesting.py`/`vectorbt` y replicada en Pine Script. Todavía no opera nada: genera evidencia.

**Nivel 1 — Bot de alertas en TradingView (Mes 3–4).** Tu estrategia en Pine Script dispara **alertas automáticas** (app/correo) en cada señal. Tú ejecutas manualmente. Es el primer contacto con "operar en vivo" sin riesgo de automatización.
- 🛠️ *Bot 1:* convierte tu estrategia de la sem. 11 en sistema de alertas con stop y target calculados.

**Nivel 2 — Semi-automatización con webhooks (Mes 4–5).** TradingView puede enviar **webhooks** (peticiones HTTP con JSON) en cada alerta. Montas un pequeño servidor (Flask/FastAPI — trivial para ti tras PaperMind) que recibe el webhook y envía la orden a un broker **en modo paper** vía API (Alpaca para acciones, o un exchange testnet vía `ccxt` para cripto).
- 🛠️ *Bot 2:* pipeline TradingView → webhook → tu servidor → orden paper en Alpaca. Con esto, tu Pine Script ya "opera" solo.
- Aquí aprendes lo que ningún backtest enseña: latencia, rechazos de órdenes, fills parciales, reconexiones.

**Nivel 3 — Bot autónomo en Python (Mes 6 = Proyecto 12).** El bot completo sin TradingView: descarga datos → calcula señal → gestiona riesgo (sizing, stops, límites de pérdida diaria) → envía órdenes → registra todo (logging) → te notifica (Telegram). Corre solo en paper trading.
- 🛠️ *Bot 3:* tu estrategia ganadora del walk-forward, operando 24/7 en paper. Añade un **kill switch**: si el drawdown supera X%, el bot se apaga solo.

**Nivel 4 — Bot institucional en QuantConnect/LEAN (Mes 6, opcional).** Reimplementa el bot en LEAN: te da datos limpios, ejecución simulada realista y la posibilidad de competir en Quant League. Es la versión "esto es lo que usan los fondos".

### Infraestructura mínima del bot serio (checklist)
- Gestión de riesgo **antes** que la señal: tamaño máximo de posición, pérdida máxima diaria, kill switch.
- Logging de cada decisión (señal, orden, fill, P&L) — tu bitácora para depurar y para mostrar en entrevistas.
- Manejo de errores de red/API (reintentos, reconexión) — tu experiencia con ESP32 y sistemas embebidos te da el instinto correcto: asumir que todo falla.
- Notificaciones (Telegram/correo) para supervisión humana.
- **Nunca dinero real en estos 6 meses.** El paso a real (si decides darlo) es con capital mínimo y después de ≥2 meses de paper estable.

### Dónde encaja cada bot en el calendario
| Bot | Semana | Prerrequisito |
|---|---|---|
| Bot 1 — Alertas TradingView | 11–12 | Estrategia en Pine (Proy. 6) |
| Bot 2 — Webhooks → paper | 16–17 (paralelo) | Validación sem. 12 |
| Bot 3 — Autónomo Python | 22 (Proy. 12) | Pipeline sem. 21 |
| Bot 4 — LEAN/QuantConnect | 23+ (opcional) | Bot 3 funcionando |

---

# 5. 🌍 Aplicación real (lo que convierte estudio en currículum)

> Esta capa corre **en paralelo** al plan y es lo que más diferencia tu perfil. Ordenadas por cuándo incorporarlas:

### TradingView (desde el Mes 3)
Tu laboratorio visual de estrategias. Publica tus mejores scripts como open-source en la comunidad: es visibilidad real y feedback de traders.

### QuantConnect (desde el Mes 3–4)
- **Boot Camp / Learning Center gratis:** lecciones interactivas donde codificas estrategias sobre **LEAN**, el motor open-source que usan cientos de hedge funds. Aprendes diseño de algoritmos de nivel institucional con datos limpios de décadas.
- **Quant League:** competencia de estrategias en vivo — una estrategia tuya corriendo en su ranking es una línea de currículum verificable.
- Hazlo después del Mes 3 para llegar con bases de backtesting y aprovecharlo de verdad.

### WorldQuant BRAIN (desde el Mes 4–5) ⭐ la joya para ti
- Plataforma gratuita de **WorldQuant** (hedge fund real) donde construyes **alphas**: modelos matemáticos que predicen movimientos de precios, evaluados por Sharpe, turnover y fitness.
- Si tus alphas son buenas, **te pueden ofrecer un puesto de research consultant remunerado, remoto y flexible** — compatible con tu tesis y accesible desde México.
- También está el **International Quant Championship** (IQC) anual por universidades: podrías representar a CINVESTAV.
- Es la forma más directa de hacer *investigación quant real* sin estar contratado en un fondo.

### Numerai (opcional, Mes 5–6)
Torneo de data science sobre datos financieros ofuscados: subes predicciones de tu modelo ML y compites por criptomoneda. Encaja perfecto con tus proyectos del Mes 5.

### Tu tesis como activo quant
No la veas como algo separado: análisis fractal (DFA/Hurst) de series fisiológicas bajo estrés **es metodológicamente idéntico** al análisis de regímenes en series financieras. En entrevistas, ese puente es tu historia diferenciadora — igual que la de Zhou (biociencias MIT → Point72).

---

# 6. 📁 Tu portafolio final (13 proyectos)

| # | Proyecto | Mes | Demuestra |
|---|---|---|---|
| 1 | Análisis de factores (CAPM/FF) | 1 | Econometría |
| 2 | EDA cuantitativo + Hurst (DFA) | 2 | Tu firma única |
| 3 | Optimizador de portafolio (Streamlit) | 2 | Optimización + producto |
| 4 | Monte Carlo de riesgo y sizing | 2 | Gestión de riesgo |
| 5 | Motor de backtesting | 3 | Ingeniería de estrategias |
| 6 | Python ↔ Pine Script | 3 | Rigor y detalle |
| 7 | Walk-forward + robustez | 3 | Honestidad estadística |
| 8 | Pairs trading (cointegración) | 4 | Stat arb |
| 9 | Valuador de opciones (BS/MC/binomial) | 4 | Derivados |
| 10 | Estrategia ML (triple-barrier, purged CV) | 5 | ML financiero serio |
| 11 | Black-Scholes en C++ (benchmark) | 5 | Quant dev (opcional) |
| 12 | Bot de paper trading | 6 | Producción |
| 13 | Capstone end-to-end (estilo paper) | 6 | Investigación completa |

**Criterio de calidad de cada repo:** README con problema → datos → método → resultados → **limitaciones** (admitir limitaciones es señal de seniority, no de debilidad).

---

# 7. 📚 Recursos consolidados

### Gratuitos de nivel universitario
- ▶️ **MIT OCW 18.S096/18.642** — *Topics in Mathematics with Applications in Finance*: el curso completo con videos, dado en parte por practicantes de la industria. Tu referencia troncal gratuita.
- 🔗 **MITx — Mathematical Methods for Quantitative Finance** (edX, auditable gratis): si quieres una versión estructurada con problemas del Mes 1.
- ▶️ **Harvard Stat 110** — probabilidad (el estándar de oro).
- ▶️ 3Blue1Brown, StatQuest, QuantPy, NeuroTrader, Part Time Larry, The Art of Trading.

### Cursos de pago (Udemy, espera ofertas de ~$15 USD)
- *Quantitative Finance & Algorithmic Trading in Python* → Mes 2.
- *Machine Learning for Quant Finance and Algorithmic Trading* → Mes 5.
- *QuantConnect Boot Camp in Python* → alternativa guiada para la capa QuantConnect.

### Libros (en orden de uso)
1. 📗 **Green Book** (Zhou) — todo el roadmap.
2. Ernest Chan — *Quantitative Trading* y *Algorithmic Trading* → Meses 3–4.
3. Hull — *Options, Futures and Other Derivatives* → Mes 4.
4. López de Prado — *Advances in Financial Machine Learning* → Meses 3 y 5.
5. Hilpisch — *Python for Finance* → referencia transversal.
6. Crack — *Heard on the Street* → Mes 6.
7. (Opcional, profundidad) Shreve — *Stochastic Calculus for Finance I*.

### Comunidad y referencia
- 🔗 **awesome-quant** (GitHub) — el índice de todo el ecosistema.
- 🔗 r/quant (Reddit) — hilos de carrera y entrevistas.
- 🔗 Foros de QuantConnect y de la comunidad BRAIN.

---

# 8. ⚠️ Principios innegociables

1. Un backtest bonito casi nunca sobrevive en vivo. Sé tu propio escéptico.
2. In-sample y out-of-sample SIEMPRE separados.
3. Costos y slippage desde el día uno.
4. Cuidado con el repainting en Pine Script.
5. Estrategias simples y robustas > modelos sobre-parametrizados.
6. El rigor matemático separa al quant del "trader con scripts".
7. Documenta todo: el rigor vale tanto como los resultados.
8. **No pongas dinero real durante estos 6 meses.** Paper trading hasta dominar el proceso.

---

# 9. 🚀 Camino crítico mínimo (si una semana vas corto de tiempo)

Brain teasers diarios → 3Blue1Brown/Stat 110 (mate) → curso Udemy de Quant Finance (finanzas) → backtesting.py + Pine Script (práctica) → QuantConnect/BRAIN (aplicación) → Green Book 2ª pasada (entrevistas). Todo lo demás es profundidad que añades según tu rol objetivo.

### Tus primeros 3 pasos HOY
1. Green Book Cap. 1 (30 min).
2. Primer video de *Essence of Linear Algebra* (3Blue1Brown).
3. Crear: repo GitHub + cuenta TradingView + cuenta QuantConnect.
