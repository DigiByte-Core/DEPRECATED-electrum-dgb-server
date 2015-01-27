from setuptools import setup

setup(
    name="electrum-dgb-server",
    version="0.9",
    scripts=['run_electrum_dgb_server','electrum-dgb-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumdgbserver':'src'
        },
    py_modules=[
        'electrumdgbserver.__init__',
        'electrumdgbserver.utils',
        'electrumdgbserver.storage',
        'electrumdgbserver.deserialize',
        'electrumdgbserver.networks',
        'electrumdgbserver.blockchain_processor',
        'electrumdgbserver.server_processor',
        'electrumdgbserver.processor',
        'electrumdgbserver.version',
        'electrumdgbserver.ircthread',
        'electrumdgbserver.stratum_tcp',
        'electrumdgbserver.stratum_http'
    ],
    description="Digibyte Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/pooler/electrum-dgb-server/",
    long_description="""Server for the Electrum Lightweight Digibyte Wallet"""
)


