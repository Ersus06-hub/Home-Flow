#  HomeFlow

Planificador de liquidez y ahorro familiar construido con Streamlit.

## ¿Qué hace?

- Registra ingresos y gastos mensuales desde el panel lateral
- Proyecta el saldo familiar a 6, 12, 24 o 36 meses
- Simula miles de escenarios con Monte Carlo para estimar el riesgo financiero
- Muestra gráficos interactivos de evolución del saldo y distribución de gastos
- Permite descargar la proyección en CSV

## Tecnologías

- [Streamlit](https://streamlit.io/) — interfaz web
- [NumPy](https://numpy.org/) — simulación Monte Carlo
- [Pandas](https://pandas.pydata.org/) — tablas de datos
- [Plotly](https://plotly.com/python/) — gráficos interactivos

## Requisitos

- Python 3.12 o superior

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/HomeFlow.git
cd HomeFlow

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows)
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
streamlit run home.py
```

La app se abre automáticamente en `http://localhost:8501`.

## Estructura del proyecto

```
HomeFlow/
├── home.py            # App principal
├── casa.png           # Logo del encabezado (sin fondo)
├── Omix.png           # Icono original
├── Omix_nobg.png      # Icono sin fondo (favicon)
├── requirements.txt   # Dependencias
└── .gitignore
```

## Nota

Los valores de ingresos y gastos arrancan en cero — el usuario los ingresa al abrir la app.
