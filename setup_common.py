from configparser import ConfigParser


def get_metadata_and_options():
    config = ConfigParser()
    config.read(["metadata.cfg", "site.cfg"])

    metadata = dict(config.items("metadata"))
    options = dict(config.items("options"))

    metadata["py_modules"] = list(filter(None, metadata["py_modules"].split("\n")))
    metadata["classifiers"] = list(filter(None, metadata["classifiers"].split("\n")))

    return metadata, options


def enabled(options, option):
    value = options[option]
    s = value.lower()
    if s in ("yes", "true", "1", "y"):
        return True
    elif s in ("no", "false", "0", "n"):
        return False
    else:
        raise ValueError(f"Unknown value {value} for option {option}")


def create_release_file(metadata):
    with open("MySQLdb/release.py", "w", encoding="utf-8") as rel:
        rel.write(
            """
__author__ = "%(author)s <%(author_email)s>"
version_info = %(version_info)s
__version__ = "%(version)s"
"""
            % metadata
        )
