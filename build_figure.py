# Data provenance:
#   07-10, 07-11, 07-12, 07-13 action counts match boundary_trace.json entries p08, p03,
#   p04, p05 exactly. 07-10 is platform-visible: Hugging Face's own logs record that day's
#   1,135 actions (p08), alongside the 14 credential validations logged separately as p01.
#   07-09 is the only date here that falls outside the boundary-observable trace, and it
#   does so by design: that activity occurred on third-party infrastructure other than
#   Hugging Face's own platform (Modal), so the platform in question could not have
#   observed it at all. It is shown for timeline context only, greyed out to mark it as
#   unobservable. Its count comes from the same Hugging Face technical timeline post as
#   the rest.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams["font.family"] = "sans-serif"

days = ["07-09\n(Modal launchpad,\nnot HF-visible)", "07-10\n(credential probing)",
        "07-11\n(HF compromise\nbegins)", "07-12\n(deep pivot)", "07-13\n(exfil, cleanup)"]
actions = [3779, 1135, 7677, 3892, 1130]
threshold_daily = 500  # illustrative daily-action threshold, matches boundary_checker.py

fig, ax = plt.subplots(figsize=(7.2, 3.3), dpi=200)
colors_bars = ["#b4b2a9" if i == 0 else ("#a32d2d" if v > threshold_daily else "#5f5e5a")
               for i, v in enumerate(actions)]
bars = ax.bar(days, actions, color=colors_bars, width=0.55, zorder=3)

ax.axhline(threshold_daily, color="#0c447c", linestyle="--", linewidth=1.2, zorder=2)
ax.annotate("illustrative B-INV-4 threshold\n(500 actions/day)",
            xy=(0.60, threshold_daily), xytext=(1.60, 4300),
            color="#0c447c", fontsize=7.5, ha="right", va="bottom",
            arrowprops=dict(arrowstyle="->", color="#0c447c", lw=0.8))

for bar, v in zip(bars, actions):
    ax.text(bar.get_x() + bar.get_width()/2, v + 150, str(v), ha="center", fontsize=8, color="#2c2c2a")

ax.annotate("actual\ncontainment\n(day 5, 14:14 UTC)",
            xy=(4.28, 1130), xytext=(4.7, 4200),
            fontsize=7.5, color="#2c2c2a", ha="center",
            arrowprops=dict(arrowstyle="->", color="#2c2c2a", lw=0.8))
ax.set_xlim(-0.6, 5.1)

ax.set_ylabel("documented daily attacker actions", fontsize=9)
ax.set_title("Daily action volume vs. an illustrative B-INV-4 threshold", fontsize=10.5, pad=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="x", labelsize=7.5)
ax.tick_params(axis="y", labelsize=8)
ax.set_ylim(0, 8800)
plt.tight_layout()
plt.savefig("detection_latency_figure.png", bbox_inches="tight")
print("saved detection_latency_figure.png")
