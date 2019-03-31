from pathlib import Path
from setuptools import setup

current_dir = Path(__file__).parent.resolve()

with open(current_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name="RustyReturn",
    version="0.1",
    py_modules = ['rustyreturn'],
    url="https://github.com/abstractequalsmagic/RustyReturn",
    description = "Return last statement of functions.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
)
