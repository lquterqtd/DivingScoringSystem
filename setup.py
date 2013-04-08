__author__ = 'Administrator'
from distutils.core import setup
import py2exe
setup(
    windows=[
        {
            "script" : "main.py",
            "icon_resources" : [
                (
                    1, "diving.ico",
                )
            ]
        }
    ],
    options={
        "py2exe" : {
            "packages": ["sqlalchemy.dialects.sqlite"],
            "dll_excludes": ["MSVCP90.dll"],
            "compressed": 1,
            "optimize": 2,
            "bundle_files": 1,
        }
    },
)