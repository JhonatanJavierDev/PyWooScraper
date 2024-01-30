from setuptools import setup, find_packages

setup(
    name='pywooscraper',
    version='0.1.0',
    description=' Library for scraping stores with WooCommerce, extracts the total number of products it has.',
    author='Jhon Corella',
    author_email= 'corella.jhonatan@gmail.com',
    url='https://https://github.com/jhonatanjavierdev',
    download_url='https://github.com/JhonatanJavierDev/PyWooScraper',
    keywords=['scraping', "woocomerce", "wordpress", "scrap"],
    license='MIT'M
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
