import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Genera un gráfico de líneas basado en el archivo news.csv
    y lo guarda en files/plots/news.png según las instrucciones del video.
    """
    # 1. Cargar el dataset (la primera columna es el índice de los años)
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # 2. Diccionarios de configuración visual para resaltar 'Internet'
    colors = {
        'Television': 'dimgrey',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,  # Pone la línea de Internet por encima de las demás
        'Radio': 1
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,  # Hace la línea de Internet más gruesa
        'Radio': 2
    }

    # 3. Crear figura vacía
    plt.figure()

    # 4. Graficar las líneas mediante un ciclo for
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    # 5. Agregar el título
    plt.title("How people get their news", fontsize=16)

    # 6. Remover los bordes superior, derecho, izquierdo y hacer invisible el eje Y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # 7. Agregar marcadores (scatter) y textos (text) en los extremos de cada línea
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        # --- Extremo izquierdo ---
        # Punto inicial
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col]
        )
        
        # Texto inicial (Nombre de la fuente y porcentaje)
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col]
        )

        # --- Extremo derecho ---
        # Punto final
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col]
        )
        
        # Texto final (Solo porcentaje)
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha='left',
            va='center',
            color=colors[col]
        )

    # 8. Personalizar el eje X para que muestre todos los años
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )

    # 9. Ajustar el diseño y guardar el gráfico
    plt.tight_layout()
    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")