import sys
from importlib import import_module
# poetry env remove --all


def main() -> None:
    """Attempts to load programs, verify versions, and analyze data."""
    missing = []
    for pkg in ['pandas', 'numpy', 'matplotlib', 'requests']:
        try:
            import_module(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"\nError: Missing dependencies detected: {', '.join(missing)}")
        print("To load these programs into your construct,"
              " use one of the following:")
        print("Using pip: pip install -r requirements.txt")
        print("Using Poetry: poetry install")
        sys.exit(1)

    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plot  # type: ignore
    import requests  # type: ignore

    print("LOADING STATUS: Loading programs...\n")
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f"[OK] requests ({requests.__version__}) - Network access ready")
    print(f"[OK] matplotlib ({plot.matplotlib.__version__}) - Visualization"
          f" ready")
    print(f"[OK] numpy ({np.__version__}) - Numerical computations ready")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data: np.ndarray = np.random.randn(1000)  # random data array
    # creates dataframe object that can be visualized
    df: pd.DataFrame = pd.DataFrame({'signal': data})

    # uses pandas for data manipulation
    print("Manipulating data using pandas...")
    df['rolling_mean'] = df['signal'].rolling(window=50).mean()

    print("Generating visualization...")
    plot.figure(figsize=(10, 6))
    plot.plot(df['signal'], alpha=0.5, label='Raw Signal')
    plot.plot(df['rolling_mean'], color='red', linewidth=2,
              label='Rolling Mean (50)')
    plot.title('Matrix Data Analysis')
    plot.legend()
    plot.savefig('matrix_analysis.png')
    print("Analysis complete!\nResults saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
