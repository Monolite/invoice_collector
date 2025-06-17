from setuptools import setup, find_packages

setup(
    name="invoice_collector",
    version="1.0.0",
    description="Script to collect emails using gmail api",
    author="Augusto Gonzalez",
    url="https://github.com/Monolite/invoice_collector",
    python_requires=">=3.10.0",
    packages=find_packages(where="src"),  # Corrected the 'where' argument
    package_dir={"": "src"},  # Added package_dir to specify the root directory
    install_requires=[
        "setuptools",
        "ipykernel",
        "ruff",
        "google-api-python-client",
        "google-auth-oauthlib",
        "google-auth-httplib2",
    ],
)
