import os
from pathlib import Path


def run():
    """
    Run Streamlit app

    Returns
    -------
    """

    dirname = Path(__file__).parent.parent.parent
    filename = "Home.py"

    os.chdir(dirname)
    print("Running streamlit from", os.getcwd())

    os.system(f"streamlit run {filename}")


if __name__ == "__main__":
    run()
