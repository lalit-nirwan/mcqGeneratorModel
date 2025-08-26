from setuptools import find_packages, setup
setup(
    name='mcqGenAI',
    version='0.0.1',
    author='lalit',
    author_email='lalitnirwan0@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pypdf2"],
    packages=find_packages(),
)