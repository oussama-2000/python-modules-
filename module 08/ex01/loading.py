def check_dependency(package_name: str) -> str:

    package_message = {
        "pandas": " Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": " Visualization ready"
    }
    try:
        module = __import__(package_name)

        return (f"[OK] {package_name} ({module.__version__})"
                f" - {package_message[package_name]}")
    except ImportError:
        return f"[KO] {package_name} not found"


def analyze_data() -> None:

    print("Analyzing Matrix data...")
    try:
        print("Processing 1000 data points...")
        pandas = __import__("pandas")
        numpy = __import__("numpy")
        data = {
            "time": numpy.arange(1000),
            "signal": numpy.random.randn(1000)
        }
        d = pandas.DataFrame(data)

        return d
    except Exception as e:
        print(e)


def create_visualization(data: object) -> None:

    try:
        import matplotlib.pyplot as plt

        print("Generating visualization...\n")

        plt.plot(data["time"], data["signal"])
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"Error during visualization: {e}")


if __name__ == "__main__":

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dependencies = ["pandas", "requests", "matplotlib"]
    for dependency in dependencies:
        print(check_dependency(dependency))

    print()
    analyzed_data = analyze_data()

    create_visualization(analyzed_data)
