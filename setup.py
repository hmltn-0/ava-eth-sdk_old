from setuptools import setup, find_packages

setup(
    name='ava_protocol_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        'grpcio-tools',
    ],
    description='Python SDK for smart contract deployment automation with Ava Protocol',
    author='Julius Hamilton',
    author_email='juliushamilton100@example.com',
    url='https://github.com/hmltn-0/ava-eth-sdk',
)

