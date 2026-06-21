import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize

st.set_page_config(page_title="Portfolio Optimizer", layout="wide")
st.title("📈 Portfolio Optimizer — Markowitz Frontier")

# --- Sidebar: inputs del usuario ---
st.sidebar.header("Configuración")
tickers_input = st.sidebar.text_input(
    "Tickers (separados por coma)", "AAPL,TSLA,AMZN,GLD"
)
tickers = [t.strip().upper() for t in tickers_input.split(",")]

start_date = st.sidebar.date_input("Fecha inicio", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("Fecha fin", pd.to_datetime("2024-12-31"))
rf = st.sidebar.slider("Tasa libre de riesgo (%)", 0.0, 10.0, 4.0) / 100

# --- Descarga de datos ---
@st.cache_data
def cargar_datos(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)["Close"]
    if isinstance(data, pd.Series):
        data = data.to_frame()
    return data

data = cargar_datos(tickers, start_date, end_date)
returns = np.log(data / data.shift(1)).dropna()

# Usar el orden REAL de columnas (lección de la clase pasada — bug del orden)
tickers_reales = returns.columns.tolist()
mu = returns.mean().values * 252
Sigma = returns.cov().values * 252
n = len(tickers_reales)

# --- Funciones de optimización ---
def portfolio_stats(w, mu, Sigma):
    ret = w @ mu
    vol = np.sqrt(w @ Sigma @ w)
    return ret, vol

def neg_sharpe(w, mu, Sigma, rf):
    ret, vol = portfolio_stats(w, mu, Sigma)
    return -(ret - rf) / vol

def vol_objetivo(w, Sigma):
    return w @ Sigma @ w

bounds = tuple((0, 1) for _ in range(n))
w0 = np.array([1/n] * n)
restr_suma1 = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

# GMV
res_gmv = minimize(vol_objetivo, w0, args=(Sigma,), method='SLSQP',
                    bounds=bounds, constraints=restr_suma1)
w_gmv = res_gmv.x
ret_gmv, vol_gmv = portfolio_stats(w_gmv, mu, Sigma)

# Máximo Sharpe
res_sharpe = minimize(neg_sharpe, w0, args=(mu, Sigma, rf), method='SLSQP',
                       bounds=bounds, constraints=restr_suma1)
w_sharpe = res_sharpe.x
ret_sharpe, vol_sharpe = portfolio_stats(w_sharpe, mu, Sigma)
sharpe_ratio = (ret_sharpe - rf) / vol_sharpe

# --- Frontera eficiente ---
retornos_obj = np.linspace(mu.min(), mu.max(), 50)
riesgos_frontera = []
for r_obj in retornos_obj:
    restricciones = [
        restr_suma1,
        {'type': 'eq', 'fun': lambda w, r_obj=r_obj: w @ mu - r_obj}
    ]
    res = minimize(vol_objetivo, w0, args=(Sigma,), method='SLSQP',
                    bounds=bounds, constraints=restricciones)
    riesgos_frontera.append(np.sqrt(res.fun))

# --- Layout: 2 columnas ---
col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(riesgos_frontera, retornos_obj, 'b-', linewidth=2, label='Frontera Eficiente')
    for i, t in enumerate(tickers_reales):
        ax.scatter(np.sqrt(Sigma[i,i]), mu[i], s=80)
        ax.annotate(t, (np.sqrt(Sigma[i,i]), mu[i]))
    ax.scatter(vol_gmv, ret_gmv, color='green', s=150, marker='*', label='Mín. Varianza')
    ax.scatter(vol_sharpe, ret_sharpe, color='red', s=150, marker='*', label='Máx. Sharpe')
    ax.set_xlabel("Riesgo (volatilidad anualizada)")
    ax.set_ylabel("Retorno esperado anualizado")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Portafolio Máximo Sharpe")
    for t, w in zip(tickers_reales, w_sharpe):
        st.write(f"**{t}**: {w*100:.1f}%")
    st.metric("Retorno esperado", f"{ret_sharpe*100:.2f}%")
    st.metric("Riesgo", f"{vol_sharpe*100:.2f}%")
    st.metric("Sharpe Ratio", f"{sharpe_ratio:.2f}")

    st.subheader("Portafolio Mínima Varianza")
    for t, w in zip(tickers_reales, w_gmv):
        st.write(f"**{t}**: {w*100:.1f}%")
    st.metric("Retorno esperado", f"{ret_gmv*100:.2f}%")
    st.metric("Riesgo", f"{vol_gmv*100:.2f}%")