from setuptools import setup, find_packages

setup(
    name="darkkaraoke",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
        "librosa",
        "soundfile",
        "pydub",
        "moviepy",
        "numpy",
        "Pillow",
        "pysrt",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "darkkaraoke=src.darkkaraoke:main"
        ]
    },
)
