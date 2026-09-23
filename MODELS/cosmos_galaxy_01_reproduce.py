"""COSMOS-GALAXY-01 reproduction launcher.

This file deliberately does not pretend to contain the authors' numerical
results. It prepares a local reproducibility run against the public
TillSawala/MW-M31 notebook.

Run on a machine with internet access and the pinned dependencies.

The authoritative numerical model is the authors' published code:
https://github.com/TillSawala/MW-M31
"""

from pathlib import Path
import subprocess
import sys

REPO_URL = "https://github.com/TillSawala/MW-M31"
LOCAL_REPO = Path("DATA/COSMOS-GALAXY-01/MW-M31")


def main():
    LOCAL_REPO.parent.mkdir(parents=True, exist_ok=True)

    if not LOCAL_REPO.exists():
        subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL, str(LOCAL_REPO)],
            check=True,
        )

    print("Public control repository available at:", LOCAL_REPO)
    print("Next step: install the exact published dependencies and execute galaxies.ipynb.")
    print("COSMOS must compare the resulting figures/metrics against the published paper.")


if __name__ == "__main__":
    main()
