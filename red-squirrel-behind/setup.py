from setuptools import find_packages, setup

requires = ['flask', 'python-dotenv', 'pymysql', "flask_sqlalchemy"]

setup(
    name="red-squirrel",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.8.2',
    install_requires=[
        "flask",
    ],
)