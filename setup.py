from setuptools import setup, find_packages

setup(
    name="summary-maker",  # Replace with your project's name
    version="0.1.0",
    author="NEERAJ SINGH",
    author_email="demo@gmail.com",
    description="A text and video summarization application",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/neeraj46665/Smart-Summarizer-Suite",  # Update with your repo link
    packages=find_packages(where='app'),  # Finds packages in the app directory
    package_dir={"": "app"},
    include_package_data=True,
    install_requires=[
        "streamlit",
        "PyPDF2",
        "langchain",
        "langchain-community",
        "langchain-groq",
        "langchain-cohere",
        "pytube",
        "youtube-transcript-api",
        "python-dotenv",
        "requests",
        "beautifulsoup4",
        "transformers",
        "cohere"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Minimum Python version required
)
