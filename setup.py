"""
독립유공자 공훈록 MCP 서버 - 설치 스크립트
"""

from setuptools import setup, find_packages

setup(
    name="gonghun_mcp_server",
    version="0.1.0",
    description="독립유공자 공훈록 MCP 서버",
    author="shinkeonkim",
    author_email="dev.shinkeonkim@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        "httpx>=0.23.0",
        "python-dotenv>=1.0.0",
        "mcp-server>=0.4.1,<0.5.0",
        "pydantic>=1.10.8,<2.0.0",  # pydantic v2와 호환성 문제가 있음
    ],
    entry_points={
        "console_scripts": [
            "gonghun-server=gonghun_mcp.main:run",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)