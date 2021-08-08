from . import __version__


def add_version(f):
    doc = f.__doc__
    f.__doc__ = "Version: " + __version__ + "\n\n" + doc

    return f
