from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-reverse",
    version="0.1.0",
    description="Reverse the order of drawing",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Mike Stringer",
    url="https://github.com/stringertheory/vpype-reverse",
    packages=["vpype_reverse"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Graphics",
        "Environment :: Plugins",
    ],
    setup_requires=["wheel"],
    install_requires=[
        'click',
        'vpype[all]>=1.10,<2.0',
    ],
    entry_points='''
            [vpype.plugins]
            vpype_reverse=vpype_reverse.vpype_reverse:vpype_reverse
        ''',
)
