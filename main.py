import matplotlib

matplotlib.use("Agg")  # Xuất file ảnh trực tiếp không qua GUI
import matplotlib.pyplot as plt
import numpy as np

# Cài đặt font chữ Times New Roman và chất lượng hình ảnh
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.size"] = 12

materials = ["SmS", "SmSe", "SmTe"]
x = np.arange(len(materials))


# ==========================================
# FIG 1: Bar chart Bulk Modulus B0
# ==========================================
def draw_fig1():
    calc_B0 = [449.3, 425.3, 390.5]
    exp_B0 = [466.3, 400.0, 400.0]

    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    width = 0.35

    rects1 = ax.bar(
        x - width / 2,
        calc_B0,
        width,
        label=r"Calculated ($B_0 = 2103.93 \cdot V_0^{-0.4454}$)",
        color="#2b6cb0",
    )
    rects2 = ax.bar(
        x + width / 2,
        exp_B0,
        width,
        label="Experimental (literature)",
        color="#c85a21",
    )

    ax.set_ylabel(r"Bulk modulus $B_0$ (kbar)", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(materials, fontsize=13)
    ax.set_ylim(0, 550)

    # Hiển thị giá trị chính xác trên đỉnh cột
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(
            f"{height:.1f}",
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 2),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10.5,
        )
    for rect in rects2:
        height = rect.get_height()
        ax.annotate(
            f"{height:.1f}",
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 2),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10.5,
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False, loc="upper right", fontsize=10)

    plt.tight_layout()
    plt.savefig("fig1.png", dpi=600)
    plt.close()


# ==========================================
# FIG 2: Absolute relative deviation \delta_B
# ==========================================
def draw_fig2():
    delta_B = [3.7, 6.3, 2.4]
    labels_text = [
        r"3.7% ($\varepsilon_B$=-3.7%)",
        r"6.3% ($\varepsilon_B$=+6.3%)",
        r"2.4% ($\varepsilon_B$=-2.4%)",
    ]

    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    width = 0.55

    rects = ax.bar(x, delta_B, width, color="#805ad5")

    ax.set_ylabel(r"Absolute relative deviation $\delta_B$ (%)", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(materials, fontsize=13)
    ax.set_ylim(0, 10)

    for i, rect in enumerate(rects):
        ax.annotate(
            labels_text[i],
            xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10.5,
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig("fig2.png", dpi=600)
    plt.close()


# ==========================================
# FIG 3: Characteristic transition pressure P_t
# ==========================================
def draw_fig3():
    p_t = [6.5, 55.0, 58.0]
    ranges = [(6.0, 6.5), (26.0, 90.0), (20.0, 80.0)]
    annotations = [
        "6.5 kbar\n(range 6-6.5)",
        "55.0 kbar\n(range 26-90)",
        "58.0 kbar\n(range 20-80)",
    ]

    fig, ax = plt.subplots(figsize=(6.5, 4.0))

    for i in range(len(materials)):
        ax.plot(
            [i, i], ranges[i], color="#a0aec0", linewidth=6, solid_capstyle="round"
        )
        ax.plot(i, p_t[i], marker="o", color="#c53030", markersize=9)
        ax.annotate(
            annotations[i],
            xy=(i, ranges[i][1] if i > 0 else p_t[i]),
            xytext=(0, 5 if i > 0 else 10),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9.5,
        )

    ax.set_ylabel(
        r"Characteristic transition pressure $P_t$ (kbar)", fontsize=13
    )
    ax.set_xticks(x)
    ax.set_xticklabels(materials, fontsize=13)
    ax.set_ylim(0, 100)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig("fig3.png", dpi=600)
    plt.close()


# ==========================================
# FIG 4: V0 and B0(calc) - Dual Y-Axis Chart
# ==========================================
def draw_fig4():
    v0 = [32.03, 36.23, 43.88]
    b0_calc = [449.3, 425.3, 390.5]

    fig, ax1 = plt.subplots(figsize=(6.5, 4.0))

    color1 = "#2f855a"
    ax1.set_ylabel(
        r"Specific volume $V_0$ ($\mathrm{cm^3/mol}$)",
        color=color1,
        fontsize=13,
    )
    (line1,) = ax1.plot(
        x,
        v0,
        color=color1,
        marker="o",
        linewidth=2.5,
        markersize=9,
        label=r"$V_0$ (specific volume)",
    )
    ax1.tick_params(axis="y", labelcolor=color1, labelsize=11)
    ax1.set_ylim(30.0, 46.0)

    ax2 = ax1.twinx()
    color2 = "#2b6cb0"
    ax2.set_ylabel(
        r"Bulk modulus $B_0(\mathrm{calc})$ (kbar)", color=color2, fontsize=13
    )
    (line2,) = ax2.plot(
        x,
        b0_calc,
        color=color2,
        marker="s",
        linestyle="--",
        linewidth=2.5,
        markersize=8,
        label=r"$B_0(\mathrm{calc})$",
    )
    ax2.tick_params(axis="y", labelcolor=color2, labelsize=11)
    ax2.set_ylim(380, 460)

    ax1.set_xticks(x)
    ax1.set_xticklabels(materials, fontsize=13)

    lines = [line1, line2]
    labels = [l.get_label() for l in lines]
    ax1.legend(
        lines,
        labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.12),
        ncol=2,
        frameon=False,
        fontsize=11,
    )

    ax1.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)

    plt.tight_layout()
    plt.savefig("fig4.png", dpi=600)
    plt.close()


# ==========================================
# FIG 5: Normalized volume V/V0 vs Pressure P
# ==========================================
def draw_fig5():
    fig, ax = plt.subplots(figsize=(6.5, 4.2))

    def bm_eos(P, B0):
        return (1 + 4 * (P / B0)) ** (-1 / 4)

    # 1. SmS (B0 = 449.3)
    P1_before = np.linspace(0, 6.5, 50)
    V1_before = bm_eos(P1_before, B0=449.3)
    P1_after = np.linspace(6.5, 10, 20)
    V1_after = bm_eos(P1_after, B0=449.3) - 0.115

    ax.plot(P1_before, V1_before, color="#c53030", linewidth=2.2, label="SmS")
    ax.plot(
        [6.5, 6.5], [V1_before[-1], V1_after[0]], color="#c53030", linewidth=2.2
    )
    ax.plot(P1_after, V1_after, color="#c53030", linewidth=2.2)
    ax.axvline(x=6.5, color="#c53030", linestyle=":", linewidth=1, alpha=0.6)

    # 2. SmSe (B0 = 425.3)
    P2_before = np.linspace(0, 55, 100)
    V2_before = bm_eos(P2_before, B0=425.3)
    P2_dash = np.linspace(55, 100, 50)
    V2_dash = bm_eos(P2_dash, B0=425.3)
    P2_after = np.linspace(55, 100, 50)
    V2_after = bm_eos(P2_after, B0=425.3) - 0.08

    ax.plot(P2_before, V2_before, color="#2b6cb0", linewidth=2.2, label="SmSe")
    ax.plot(
        P2_dash,
        V2_dash,
        color="#2b6cb0",
        linestyle="--",
        linewidth=1.5,
        alpha=0.6,
    )
    ax.plot(
        [55, 55], [V2_before[-1], V2_after[0]], color="#2b6cb0", linewidth=2.2
    )
    ax.plot(P2_after, V2_after, color="#2b6cb0", linewidth=2.2)
    ax.axvline(x=55, color="#2b6cb0", linestyle=":", linewidth=1, alpha=0.6)

    # 3. SmTe (B0 = 390.5)
    P3_before = np.linspace(0, 58, 100)
    V3_before = bm_eos(P3_before, B0=390.5) - 0.005
    P3_dash = np.linspace(58, 90, 50)
    V3_dash = bm_eos(P3_dash, B0=390.5) - 0.005
    P3_after = np.linspace(58, 90, 50)
    V3_after = bm_eos(P3_after, B0=390.5) - 0.075

    ax.plot(P3_before, V3_before, color="#2f855a", linewidth=2.2, label="SmTe")
    ax.plot(
        P3_dash,
        V3_dash,
        color="#2f855a",
        linestyle="--",
        linewidth=1.5,
        alpha=0.6,
    )
    ax.plot(
        [58, 58], [V3_before[-1], V3_after[0]], color="#2f855a", linewidth=2.2
    )
    ax.plot(P3_after, V3_after, color="#2f855a", linewidth=2.2)
    ax.axvline(x=58, color="#2f855a", linestyle=":", linewidth=1, alpha=0.6)

    ax.set_title(
        r"Solid: Birch–Murnaghan compression + valence-collapse step at $P_t$"
        "\n"
        r"Dashed: purely elastic Birch–Murnaghan prediction",
        fontsize=10,
        pad=10,
    )

    ax.set_xlabel(r"Pressure $P$ (kbar)", fontsize=13)
    ax.set_ylabel(r"Normalized volume $V/V_0$", fontsize=13)
    ax.set_xlim(-5, 105)
    ax.set_ylim(0.75, 1.02)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False, loc="lower left", fontsize=11)

    plt.tight_layout()
    plt.savefig("fig5.png", dpi=600)
    plt.close()


if __name__ == "__main__":
    draw_fig1()
    draw_fig2()
    draw_fig3()
    draw_fig4()
    draw_fig5()
    print(
        "Tất cả các hình đã được tạo thành công với số liệu Python mới chính xác!"
    )