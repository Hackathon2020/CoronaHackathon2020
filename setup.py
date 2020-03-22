from setuptools import setup, find_packages

# allows to get version via python setup.py --version
__version__ = "dev"

install_requires = [ #what packages are required
    "PyQt5",
    #"pyyaml",
    #"tqdm",
    #"Pillow < 7.0.0",
    #"chainer",
    #"numpy",
    #"pandas",  # for csv dataset and eval pipeline
    "flask-bootstrap"
    "flask-wtf"
    "flask",
    "jsonschema"
]

install_full = [  # for extra functionality e.g. features in development
    #"streamlit > 0.49",  # for edexplore
    #"psutil",  # for edlist
    #"scipy>=1.4.1",  # pinned dependency of scikit-image; 1.4.1 fixes https://github.com/scipy/scipy/issues/11237
    #"scikit-image",  # for ssim in image_metrics.py
    #"matplotlib",  # for plot_datum
    #"flowiz",  # for visualizing flow with streamlit
    #"wandb",  # for `--wandb_logging True`
    #"tensorboard",  # for `--tensorboard_logging True`
]
install_docs = [  # for building the documentation
    "sphinx >= 1.4",
    "sphinx_rtd_theme",
    "better-apidoc",
]
install_dev = [  # for developoing
    "black",  # for formatting of code
    #"pytest",
    #"pytest-cov",
    #"coveralls",
    #"coverage < 5.0",
]
extras_require = {"docs": install_docs, "dev": install_dev, "full": install_docs+install_dev}

long_description = """This is a Hackathon project. [Documentation](https://coronahackathon2020.readthedocs.io/)"""


setup(
    name="hackathon_project",
    version=__version__,
    description="Hacking vs Covid-19",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hackathon2020/CoronaHackathon2020",
    author="#wir",
    author_email="t.b.a",
    license="MIT",
    packages=find_packages(),
    package_data={"": ["*.yaml"]},
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
    scripts=[
        "project/grenz-app", #script files that can be called as package
        "project/beamten-app", #script files that can be called as package
        "project/dict-gener-app", #script files that can be called as package
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
