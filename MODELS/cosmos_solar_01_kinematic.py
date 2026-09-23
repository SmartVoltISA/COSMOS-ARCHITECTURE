"""COSMOS-SOLAR-01: frame-dependence test for the Solar System trajectory.

This is a deliberately minimal kinematic model, not an N-body integrator.
It tests whether a visually spiral/helix-like trajectory survives a change
from an inertial Galactic frame to a Sun-centered frame.

Units:
- distance: AU
- time: Julian years
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np


AU_KM = 149_597_870.7
YEAR_DAYS = 365.25
GALACTIC_SPEED_KM_S = 720_000.0 / 3600.0  # NASA value: ~720,000 km/h
GALACTIC_PERIOD_YR = 230_000_000.0

PLANETS = {
    "Mercury": (0.387, 88.0),
    "Venus": (0.723, 224.7),
    "Earth": (1.000, 365.2),
    "Mars": (1.520, 687.0),
    "Jupiter": (5.20, 4331.0),
    "Saturn": (9.57, 10747.0),
    "Uranus": (19.17, 30589.0),
    "Neptune": (30.18, 59800.0),
}


def path_length(points: np.ndarray) -> float:
    return float(np.linalg.norm(np.diff(points, axis=0), axis=1).sum())


def simulate(years: int = 50, samples_per_day: int = 1) -> list[dict]:
    days = int(years * YEAR_DAYS)
    t = np.linspace(0.0, years, days * samples_per_day + 1)

    # Circular approximation of the Sun's Galactic motion.
    v_au_yr = GALACTIC_SPEED_KM_S * YEAR_DAYS * 86400.0 / AU_KM
    r_gal_au = v_au_yr * GALACTIC_PERIOD_YR / (2.0 * math.pi)
    omega_gal = 2.0 * math.pi / GALACTIC_PERIOD_YR

    sun = np.column_stack(
        (
            r_gal_au * np.cos(omega_gal * t),
            r_gal_au * np.sin(omega_gal * t),
            np.zeros_like(t),
        )
    )

    # Approximate 60-degree inclination between ecliptic and Galactic plane.
    tilt = math.radians(60.0)
    results = []

    for name, (radius_au, period_days) in PLANETS.items():
        omega = 2.0 * math.pi / (period_days / YEAR_DAYS)
        relative = np.column_stack(
            (
                radius_au * np.cos(omega * t),
                radius_au * np.sin(omega * t) * math.cos(tilt),
                radius_au * np.sin(omega * t) * math.sin(tilt),
            )
        )
        global_xyz = sun + relative

        heli_r = np.linalg.norm(relative, axis=1)
        results.append(
            {
                "planet": name,
                "radius_au": radius_au,
                "period_days": period_days,
                "heliocentric_path_au": path_length(relative),
                "galactic_frame_path_au": path_length(global_xyz),
                "galactic_frame_net_displacement_au": float(
                    np.linalg.norm(global_xyz[-1] - global_xyz[0])
                ),
                "heliocentric_r_min_au": float(heli_r.min()),
                "heliocentric_r_max_au": float(heli_r.max()),
                "heliocentric_r_std_au": float(heli_r.std()),
            }
        )

    return results


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    out = root / "DATA" / "COSMOS-SOLAR-01"
    out.mkdir(parents=True, exist_ok=True)

    rows = simulate()
    csv_path = out / "kinematic_50yr_metrics.csv"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {csv_path}")
    for row in rows:
        ratio = row["galactic_frame_path_au"] / row["heliocentric_path_au"]
        print(
            f'{row["planet"]:8s} '
            f'global/heliocentric path ratio={ratio:.3f} '
            f'r_std={row["heliocentric_r_std_au"]:.3e} AU'
        )


if __name__ == "__main__":
    main()
