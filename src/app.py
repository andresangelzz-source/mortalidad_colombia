import pandas as pd
import os
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

BASE_DIR = os.path.dirname(__file__)
# =========================
# CARGAR ARCHIVOS EXCEL
# =========================

df_mortalidad = pd.read_csv(
    os.path.join(BASE_DIR, "data", "Nuevo_anexo.csv"),
    sep=";"
)

df_codigos = pd.read_csv(
    os.path.join(BASE_DIR, "data", "Nuevo_anexo1.csv"),
    sep=";"
)

df_divipola = pd.read_csv(
    os.path.join(BASE_DIR, "data", "Divipola_CE_(1).csv"),
    sep=";"
)


# =========================
# MOSTRAR INFORMACIÓN
# =========================


#print(df_mortalidad.columns)
#print(df_mortalidad.head())


print(df_codigos.columns)
#print(df_codigos.head())


print(df_divipola.columns)
#print(df_divipola.head())

df_final = df_mortalidad.merge(df_divipola, on="COD_DEPARTAMENTO", how="left")
df_final["SEXO"] = df_final["SEXO"].replace({
    1: "Hombre",
    2: "Mujer",
    3: "Sin información"
})

# GRAFICOS

fig_dep = px.bar(
    df_final.groupby("DEPARTAMENTO").size().reset_index(name="TOTAL"),
    x="DEPARTAMENTO",
    y="TOTAL",
    title="Mortalidad por Departamento",
    text="TOTAL"
)

fig_dep.update_layout(
    title_font_size=24,
    title_x=0.5,
    xaxis_title="Departamebto",
    yaxis_title="Numero de Muertes"
)

fig_sexo = px.pie(
    df_final,
    names="SEXO",
    title="Mortalidad por Sexo",
    hole=0.4
)

fig_sexo.update_layout(
    title_font_size=24,
    title_x=0.5,
)
fig_edad = px.histogram(
    df_final,
    x="GRUPO_EDAD1",
    title="Distribución por Edad",
    text_auto=True
)
fig_edad.update_layout(
    title_font_size=24,
    title_x=0.5,
    xaxis_title="Grupo de Edad",
    yaxis_title="Numero de Muertes",
    bargap=0.2
)

# =========================
# APP DASH
# =========================

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1(
        "Dashboard Mortalidad en Colombia 2019", 
        style={
            "textAlign": "center",
            "color": "#1f3b73"
        }
    ),

    dcc.Dropdown(
        options=[
            {"label": dep, "value": dep}
            for dep in sorted(df_final["DEPARTAMENTO"].dropna().unique())
        ],
        value=sorted(df_final["DEPARTAMENTO"].dropna().unique())[0],
        id="filtro_departamento",
        style={"marginBottom": "20px"}
    ),

    html.Div([

        html.Div([
            html.H3("Total Muertes"),
            html.H2(f"{len(df_final):,}")
        ], style={
             "backgroundColor": "white",
             "padding": "20px",
             "borderRadius": "10px",
             "boxShadow": "2px 2px 10px lightgray",
             "textAlign": "center",
             "width": "30%"
        }),
    
        html.Div([
            html.H3("Departamentos"),
            html.H2(df_final["DEPARTAMENTO"].nunique())
        ], style={
             "backgroundColor": "white",
             "padding": "20px",
             "borderRadius": "10px",
             "boxShadow": "2px 2px 10px lightgray",
             "textAlign": "center",
             "width": "30%"
        }),
        html.Div([
            html.H3("Municipios"),
            html.H2(df_final["MUNICIPIO"].nunique())
        ], style={
             "backgroundColor": "white",
             "padding": "20px",
             "borderRadius": "10px",
             "boxShadow": "2px 2px 10px lightgray",
             "textAlign": "center",
             "width": "30%"
        })

    ], style={
    "display": "flex",
    "justifyContent": "space-around",
    "marginBottom": "30px"
    }),
     
    dcc.Graph(figure=fig_sexo), 
    dcc.Graph(figure=fig_dep), 
    dcc.Graph(figure=fig_edad)
],     style={
        "background": "#F5F5F5",
        "padding": "20px"

})

if __name__ == '__main__':
    app.run(debug=True)