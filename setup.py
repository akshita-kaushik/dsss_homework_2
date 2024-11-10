from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Specify dependencies here or leave it to load from requirements.txt
    ],
    # Metadata
    author="Akshita Kaushik",
    author_email="kaushikakshita0@gmail.com",
    description="A math quiz package for educational purposes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/akshita-kaushik/dsss_homework_2",  # Replace with your actual GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # Run the 'main' function from math_quiz.py
        ],
    },
)
