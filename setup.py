from setuptools import setup, find_packages

setup(
    name="repl-python-wakatime",
    description="Python REPL plugin for automatic time tracking and metrics generated from your programming activity",
    author="Wu Zhenyu",
    author_email="wuzhenyu@ustc.edu",
    version="0.0.12",
    url="https://repl-python-wakatime.readthedocs.io",
    project_urls={
        "Homepage": "https://repl-python-wakatime.readthedocs.io",
        "Download": "https://github.com/wakatime/repl-python-wakatime/releases",
        "Bug Report": "https://github.com/wakatime/repl-python-wakatime/issues",
        "Source": "https://github.com/wakatime/repl-python-wakatime"
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    keywords=["wakatime", "plugin", "python", "ipython", "ptpython"],
    license="GPL v3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(where="."),
    package_data={
        "repl_python_wakatime": ["py.typed", "assets/*"]
    },
    install_requires=[
        # List your core dependencies here, e.g.
        # "some_package >= 1.0",
    ],
    extras_require={
        "dev": [line.strip() for line in open("requirements/dev.txt").readlines()],
        "ipython": [line.strip() for line in open("requirements/ipython.txt").readlines()],
        "keyring": [line.strip() for line in open("requirements/keyring.txt").readlines()],
        "ptipython": [line.strip() for line in open("requirements/ptipython.txt").readlines()],
        "ptpython": [line.strip() for line in open("requirements/ptpython.txt").readlines()],
    },
    include_package_data=True,
    zip_safe=False
)
