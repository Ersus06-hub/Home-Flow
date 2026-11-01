import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import base64
from PIL import Image as _PIL_Image

st.set_page_config(
    page_title="HomeFlow | Finanzas familiares",
    page_icon=_PIL_Image.open("Omix.png"),
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        --hf-bg: #0E1117;
        --hf-panel: #171B27;
        --hf-border: #30384A;
        --hf-text: #F3F4F6;
        --hf-muted: #AAB4C5;
        --hf-purple: #A78BFA;
        --hf-blue: #60A5FA;
        --hf-green: #34D399;
    }
    .stApp { background: var(--hf-bg); color: var(--hf-text); }
    [data-testid="stHeader"] { background: rgba(14,17,23,.92); }
    [data-testid="stSidebar"] {
        background: #191B26;
        border-right: 1px solid var(--hf-border);
    }
    .main-title {
        font-size: clamp(2.1rem, 4vw, 3rem);
        color: var(--hf-purple);
        font-weight: 850;
        letter-spacing: -1.2px;
        margin-bottom: .1rem;
    }
    .sub-title { color: var(--hf-muted); font-size: 1.05rem; margin-bottom: 1.5rem; }
    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #1B2030, #151925);
        border: 1px solid var(--hf-border);
        padding: 18px 20px;
        border-radius: 16px;
        min-height: 125px;
        box-shadow: 0 6px 20px rgba(0,0,0,.12);
    }
    [data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p {
        color: #C4B5FD !important;
        font-weight: 600 !important;
    }
    [data-testid="stMetricValue"], [data-testid="stMetricValue"] div {
        color: #F9FAFB !important;
        font-weight: 750 !important;
    }
    [data-testid="stMetricDelta"] { color: var(--hf-green) !important; }
    .stTabs [data-baseweb="tab-list"] { gap: .45rem; border-bottom: 1px solid var(--hf-border); }
    .stTabs [data-baseweb="tab"] { padding: .7rem 1rem; font-weight: 650; }
    .stTabs [aria-selected="true"] { color: var(--hf-purple) !important; }
    div[data-testid="stExpander"] { border: 1px solid var(--hf-border); border-radius: 12px; overflow: hidden; }
    .stAlert { border-radius: 12px; }
    div[data-testid="stDataFrame"] { border: 1px solid var(--hf-border); border-radius: 12px; overflow: hidden; }
    hr { border-color: var(--hf-border); }
    h1, h2, h3 { letter-spacing: -.4px; }
    @media (max-width: 768px) {
        .main-title { font-size: 2rem; }
        [data-testid="stMetric"] { padding: 12px; min-height: 100px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def soles(valor):
    return f"S/ {valor:,.2f}"


@st.cache_data(show_spinner=False)
def img_base64(ruta):
    """Convierte una imagen local a base64 para incrustarla en HTML."""
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ENCABEZADO
_logo = img_base64("casa.png")

# INGRESOS
st.sidebar.header("Configuración financiera")

st.markdown(
    f'<div style="margin-top:-8.0rem;margin-bottom:0;text-align:left;margin-left:-7.5rem">'
    f'<img src="data:image/png;base64,{_logo}" '
    f'style="height:16rem;width:auto;mix-blend-mode:screen">'
    f"</div>",
    unsafe_allow_html=True,
)
with st.sidebar.expander("Ingresos", expanded=True):
    ingreso_principal = st.number_input(
        "Sueldo principal mensual (S/)", min_value=0.0, value=0.0,
        step=100.0, key="ingreso_principal"
    )
    ingreso_secundario = st.number_input(
        "Segundo sueldo mensual (S/)", min_value=0.0, value=0.0,
        step=100.0, key="ingreso_secundario"
    )
    ingreso_extra = st.number_input(
        "Otros ingresos mensuales (S/)", min_value=0.0, value=0.0,
        step=100.0, key="ingreso_extra"
    )
    bono_julio = st.number_input(
        "Bono de julio (S/)", min_value=0.0, value=0.0,
        step=100.0, key="bono_julio"
    )
    bono_diciembre = st.number_input(
        "Bono de diciembre (S/)", min_value=0.0, value=0.0,
        step=100.0, key="bono_diciembre"
    )

ingreso_total = ingreso_principal + ingreso_secundario + ingreso_extra


# GASTOS
with st.sidebar.expander("Gastos", expanded=True):
    vivienda = st.number_input(
        "Vivienda mensual (S/)", min_value=0.0, value=0.0,
        step=50.0, key="vivienda"
    )
    alimentacion = st.number_input(
        "Alimentación mensual (S/)", min_value=0.0, value=0.0,
        step=50.0, key="alimentacion"
    )
    servicios = st.number_input(
        "Servicios mensuales (S/)", min_value=0.0, value=0.0,
        step=50.0, key="servicios"
    )
    educacion = st.number_input(
        "Educación mensual (S/)", min_value=0.0, value=0.0,
        step=50.0, key="educacion"
    )
    transporte = st.number_input(
        "Transporte mensual (S/)", min_value=0.0, value=0.0,
        step=50.0, key="transporte"
    )
    deudas = st.number_input(
        "Deudas mensuales (S/)", min_value=0.0, value=0.0,
        step=50.0, key="deudas"
    )
    varios = st.number_input(
        "Otros gastos mensuales (S/)", min_value=0.0, value=0.0,
        step=50.0, key="varios"
    )
    gasto_marzo = st.number_input(
        "Matrícula y útiles en marzo (S/)", min_value=0.0, value=0.0,
        step=100.0, key="gasto_marzo"
    )

gasto_total = vivienda + alimentacion + servicios + educacion + transporte + deudas + varios


# PARÁMETROS DE PROYECCIÓN
with st.sidebar.expander("Saldo, rendimiento y riesgo", expanded=True):
    saldo_inicial = st.number_input(
        "Saldo inicial (S/)", min_value=0.0, value=0.0,
        step=500.0, key="saldo_inicial"
    )
    tasa_anual = st.slider(
        "Rendimiento anual (%)", min_value=0.0, max_value=15.0,
        value=0.0, step=0.1, key="tasa_anual"
    )
    volatilidad = st.slider(
        "Imprevistos mensuales (S/)", min_value=0.0, max_value=1000.0,
        value=0.0, step=50.0, key="volatilidad"
    )
    horizonte = st.selectbox(
        "Horizonte de proyección (meses)", [6, 12, 24, 36],
        index=1, key="horizonte"
    )
    cantidad_simulaciones = st.selectbox(
        "Escenarios simulados", [1000, 2000, 5000],
        index=1, key="cantidad_simulaciones"
    )


# MOTOR FINANCIERO: proyección desde enero.
@st.cache_data(show_spinner=False)
def calcular_proyeccion(
    saldo_inicial, ingreso, gasto, bono_julio, bono_diciembre,
    gasto_marzo, tasa_anual, volatilidad, horizonte, cantidad_simulaciones
):
    tasa_mensual = (1 + tasa_anual / 100) ** (1 / 12) - 1
    meses = np.arange(horizonte + 1)
    flujo_base = ingreso - gasto
    saldo_base = np.zeros(horizonte + 1, dtype=float)
    saldo_base[0] = saldo_inicial

    rng = np.random.default_rng(42)
    escenarios = np.zeros((cantidad_simulaciones, horizonte + 1), dtype=float)
    escenarios[:, 0] = saldo_inicial

    for mes in range(1, horizonte + 1):
        flujo = flujo_base
        mes_del_anio = ((mes - 1) % 12) + 1
        if mes_del_anio == 3:
            flujo -= gasto_marzo
        if mes_del_anio == 7:
            flujo += bono_julio
        if mes_del_anio == 12:
            flujo += bono_diciembre

        saldo_base[mes] = saldo_base[mes - 1] * (1 + tasa_mensual) + flujo
        shocks = rng.normal(0, volatilidad, size=cantidad_simulaciones)
        escenarios[:, mes] = (
            escenarios[:, mes - 1] * (1 + tasa_mensual) + flujo + shocks
        )

    p10 = np.percentile(escenarios, 10, axis=0)
    p50 = np.percentile(escenarios, 50, axis=0)
    p90 = np.percentile(escenarios, 90, axis=0)
    prob_final_negativo = float(np.mean(escenarios[:, -1] < 0) * 100)
    prob_alguna_vez_negativo = float(
        np.mean(np.any(escenarios[:, 1:] < 0, axis=1)) * 100
    )

    saldo_sin_intereses = float(saldo_inicial)
    for mes in range(1, horizonte + 1):
        flujo = flujo_base
        mes_del_anio = ((mes - 1) % 12) + 1
        if mes_del_anio == 3:
            flujo -= gasto_marzo
        if mes_del_anio == 7:
            flujo += bono_julio
        if mes_del_anio == 12:
            flujo += bono_diciembre
        saldo_sin_intereses += flujo

    return (
        meses, saldo_base, p10, p50, p90, tasa_mensual,
        saldo_sin_intereses, prob_final_negativo, prob_alguna_vez_negativo
    )


(
    meses, saldo_base, p10, p50, p90, tasa_mensual, saldo_sin_intereses,
    prob_final_negativo, prob_alguna_vez_negativo
) = calcular_proyeccion(
    saldo_inicial, ingreso_total, gasto_total, bono_julio, bono_diciembre,
    gasto_marzo, tasa_anual, volatilidad, horizonte, cantidad_simulaciones
)

flujo_neto = ingreso_total - gasto_total
saldo_final = float(saldo_base[-1])
intereses_estimados = saldo_final - saldo_sin_intereses
saldo_minimo = float(np.min(saldo_base))
mes_minimo = int(np.argmin(saldo_base))
fondo_emergencia = gasto_total * 3
tasa_ahorro = (flujo_neto / ingreso_total * 100) if ingreso_total > 0 else 0.0


# RESUMEN FINANCIERO
st.subheader("Resumen financiero")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Ingresos mensuales", soles(ingreso_total))
c2.metric("Gastos mensuales", soles(gasto_total))
c3.metric(f"Saldo proyectado ({horizonte} meses)", soles(saldo_final))
c4.metric("Ahorro mensual potencial", soles(flujo_neto))

if flujo_neto < 0:
    st.error(
        f"Déficit mensual: {soles(abs(flujo_neto))}. "
        "Los gastos recurrentes superan los ingresos."
    )
elif flujo_neto == 0:
    st.warning("Tus ingresos y gastos mensuales están equilibrados.")
else:
    st.success(
        f"Tu ahorro potencial mensual es {soles(flujo_neto)}, "
        f"equivalente al {tasa_ahorro:.1f}% de tus ingresos, antes de gastos extraordinarios."
    )

with st.expander("Ver otros indicadores"):
    extra1, extra2, extra3 = st.columns(3)
    extra1.metric("Intereses estimados", soles(intereses_estimados))
    extra2.metric("Fondo de emergencia (3 meses)", soles(fondo_emergencia))
    extra3.metric("Rendimiento anual", f"{tasa_anual:.1f}%")


# PESTAÑAS
tab1, tab2, tab3 = st.tabs(["Proyección", "Presupuesto", "Riesgo financiero"])

with tab1:
    st.subheader("Evolución del saldo familiar")
    figura = go.Figure()
    figura.add_trace(go.Scatter(
        x=np.concatenate([meses, meses[::-1]]),
        y=np.concatenate([p90, p10[::-1]]),
        fill="toself",
        fillcolor="rgba(124, 58, 237, 0.18)",
        line=dict(color="rgba(0,0,0,0)"),
        name="Rango P10-P90",
        hoverinfo="skip",
    ))
    figura.add_trace(go.Scatter(
        x=meses, y=p50, mode="lines", name="Mediana de escenarios",
        line=dict(color="#A78BFA", dash="dot", width=3),
    ))
    figura.add_trace(go.Scatter(
        x=meses, y=saldo_base, mode="lines+markers", name="Proyección base",
        line=dict(color="#60A5FA", width=3), marker=dict(size=6),
    ))
    figura.add_hline(y=0, line_dash="dash", line_color="#F87171")
    figura.update_layout(
        title="Proyección del saldo familiar",
        xaxis_title="Mes de proyección (desde enero)",
        yaxis_title="Saldo disponible (S/)",
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        height=500,
        margin=dict(l=20, r=20, t=70, b=35),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(gridcolor="#30384A", zerolinecolor="#F87171"),
        font=dict(color="#E5E7EB", family="Arial"),
    )
    st.plotly_chart(figura, use_container_width=True)

    tabla = pd.DataFrame({
        "Mes": meses,
        "Saldo base (S/)": np.round(saldo_base, 2),
        "Escenario bajo P10 (S/)": np.round(p10, 2),
        "Mediana P50 (S/)": np.round(p50, 2),
        "Escenario alto P90 (S/)": np.round(p90, 2),
    })
    st.subheader("Tabla mensual")
    st.dataframe(tabla, use_container_width=True, hide_index=True)
    st.download_button(
        "Descargar proyección CSV",
        data=tabla.to_csv(index=False).encode("utf-8-sig"),
        file_name="homeflow_proyeccion.csv",
        mime="text/csv",
    )


with tab2:
    col1, col2 = st.columns(2)
    categorias = pd.DataFrame({
        "Categoría": ["Vivienda", "Alimentación", "Servicios", "Educación",
                      "Transporte", "Deudas", "Varios"],
        "Monto": [vivienda, alimentacion, servicios, educacion,
                  transporte, deudas, varios],
    })
    categorias_positivas = categorias[categorias["Monto"] > 0].copy()

    with col1:
        st.subheader("Distribución de gastos")
        if not categorias_positivas.empty:
            grafico_gastos = px.pie(
                categorias_positivas, names="Categoría", values="Monto", hole=0.48,
                color_discrete_sequence=[
                    "#8B5CF6", "#60A5FA", "#34D399", "#FBBF24",
                    "#F472B6", "#FB7185", "#94A3B8",
                ],
            )
            grafico_gastos.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#E5E7EB"),
                legend=dict(orientation="h", yanchor="bottom", y=-0.2),
                margin=dict(l=10, r=10, t=20, b=20),
                height=420,
            )
            st.plotly_chart(grafico_gastos, use_container_width=True)
        else:
            st.info("Introduce gastos mayores que cero para ver el gráfico.")

    with col2:
        st.subheader("Balance mensual")
        st.metric("Ingresos totales", soles(ingreso_total))
        st.metric("Gastos recurrentes", soles(gasto_total))
        st.metric("Flujo neto mensual", soles(flujo_neto))
        st.metric("Gasto extraordinario de marzo", soles(gasto_marzo))
        st.metric("Bono de julio", soles(bono_julio))
        st.metric("Bono de diciembre", soles(bono_diciembre))

    st.subheader("Detalle de gastos")
    detalle_gastos = categorias.copy()
    detalle_gastos.loc[len(detalle_gastos)] = ["TOTAL MENSUAL", gasto_total]
    st.dataframe(detalle_gastos, use_container_width=True, hide_index=True)


with tab3:
    st.subheader("Diagnóstico de liquidez")
    r1, r2, r3 = st.columns(3)
    r1.metric("Saldo mínimo proyectado", soles(saldo_minimo))
    r2.metric("Riesgo de terminar en negativo", f"{prob_final_negativo:.1f}%")
    r3.metric("Riesgo de saldo negativo algún mes", f"{prob_alguna_vez_negativo:.1f}%")

    if mes_minimo == 0:
        st.caption("El saldo mínimo corresponde al saldo inicial.")
    else:
        st.caption(f"El saldo mínimo de la proyección base ocurre en el mes {mes_minimo}.")

    if saldo_minimo < 0:
        st.error(
            f"La proyección base llega a {soles(saldo_minimo)}. "
            "Revisa los gastos, los ingresos o el saldo inicial."
        )
    elif saldo_minimo < 1000:
        st.warning(
            f"Tu saldo mínimo es {soles(saldo_minimo)}. Conviene evaluar una reserva adicional."
        )
    else:
        st.success(
            f"La proyección base permanece por encima de cero. Saldo mínimo: {soles(saldo_minimo)}."
        )

    st.subheader("Fondo de emergencia")
    st.write(f"Meta de referencia (3 meses de gastos): **{soles(fondo_emergencia)}**.")
    if saldo_final >= fondo_emergencia:
        st.success("El saldo final proyectado alcanza la meta de referencia.")
    else:
        st.info("El saldo final proyectado aún no alcanza la meta de tres meses de gastos.")

    st.subheader("Modelo matemático")
    st.latex(r"S_m = S_{m-1}(1+r_m)+I_m-G_m+E_m")
    st.write(
        "S representa el saldo, r la tasa mensual, I los ingresos recurrentes, "
        "G los gastos recurrentes y E los eventos extraordinarios del mes."
    )
    st.latex(
        r"S_m^{(j)}=S_{m-1}^{(j)}(1+r_m)+I_m-G_m+E_m+\varepsilon_m^{(j)}"
    )
    st.write(
        f"Tasa mensual equivalente: {tasa_mensual * 100:.4f}%. "
        f"Escenarios simulados: {cantidad_simulaciones:,}. "
        f"Desviación estándar mensual de imprevistos: {soles(volatilidad)}."
    )
    st.warning(
        "La simulación es orientativa. Supone imprevistos mensuales aleatorios e independientes; "
        "no predice el futuro con certeza."
    )

st.divider()
st.caption("HomeFlow · Planificador orientativo de liquidez familiar · Los resultados son estimaciones.")
