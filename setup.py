from setuptools import setup

requires = ['nfcpy']

setup(
    name='nfcpy_id_reader',
    version='0.1.0',
    description='Read the ID of an NFC Tag with nfcpy',
    url='https://github.com/ayabok/nfcpy_id_reader_py3',
    author='ayabok',
    author_email='ayabok@outlook.com',
    license='EUPL 1.1',
    keywords='nfc pasori',
    packages=['nfcpy_id_reader'],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

