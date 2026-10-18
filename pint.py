import pandas as pd
import matplotlib.pyplot as plt

Style = {
    "two_ukas": "blue",
    "bin_serch_two_arr": "orange",
    "exp_serch_two_arr": "green",
    "double_bin_search_two_arr": "red",
}
Label = {
    "two_ukas": "Два указателя",
    "bin_serch_two_arr": "Бинарный",
    "exp_serch_two_arr": "Экспоненциальный",
    "double_bin_search_two_arr": "Двойной бинарный",
}
Markers = {
    "two_ukas": "o",
    "bin_serch_two_arr": "s",
    "exp_serch_two_arr": "^",
    "double_bin_search_two_arr": "D",
}


def plot_series(df, x_col, x_label, title, filename):
    """Строит график time_sec vs x_col для всех алгоритмов."""
    if df.empty:
        print(f"⚠️  Нет данных для {title}")
        return

    plt.figure(figsize=(10, 6))
    for algo in df["algorithm"].unique():
        data = df[df["algorithm"] == algo].sort_values(x_col)
        plt.plot(
            data[x_col], data["time_sec"],
            marker=Markers.get(algo, "o"),
            color=Style.get(algo, None),
            label=Label.get(algo, algo),
            linewidth=2, markersize=9,
        )
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel("Время (с)", fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"✅ {filename}")


def build_4_plots(csv_file="results.csv"):
    df = pd.read_csv(csv_file)
    df = df[df["type"] == "normal"].copy()

    # --------------------------------------------------------
    # ГРАФИК 1: N = 10^8, M растёт (M << N)
    # --------------------------------------------------------
    sub = df[df["N"] == 10**8].copy()
    plot_series(
        sub, x_col="M",
        x_label="M (размер массива a)",
        title="График 1: N = 10⁸ (M << N), M растёт",
        filename="plot_1_N1e8_M_grows.png",
    )

    # --------------------------------------------------------
    # ГРАФИК 2: M = 10^8, N растёт (M >> N)
    # --------------------------------------------------------
    sub = df[df["M"] == 10**8].copy()
    plot_series(
        sub, x_col="N",
        x_label="N (размер массива b)",
        title="График 2: M = 10⁸ (M >> N), N растёт",
        filename="plot_2_M1e8_N_grows.png",
    )

    # --------------------------------------------------------
    # ГРАФИК 3: M = N, оба растут
    # --------------------------------------------------------
    sub = df[df["M"] == df["N"]].copy()
    sub["size"] = sub["M"]
    plot_series(
        sub, x_col="size",
        x_label="M = N (размер обоих массивов)",
        title="График 3: M = N, оба растут",
        filename="plot_3_MeqN.png",
    )

    # --------------------------------------------------------
    # ГРАФИК 4: M = 10^7 фиксировано, N = 10^7, 10^8
    # --------------------------------------------------------
    sub = df[df["M"] == 10**7].copy()
    plot_series(
        sub, x_col="N",
        x_label="N (размер массива b)",
        title="График 4: M = 10⁷, N растёт",
        filename="plot_4_M1e7_N_grows.png",
    )


if __name__ == "__main__":
    build_4_plots("results.csv")