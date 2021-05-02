from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'TikTok API Video Wrapper'
LONG_DESCRIPTION = 'Python Package that uses TikTok\'s API wrapper for videos.'

setup(
        name="pytokapi", 
        version=VERSION,
        author="CryptosByte",
        author_email="notcryptos@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests"],
        
        keywords=[
          'python',
          'tiktok',
          'api',
          'wrapper'
        ],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)