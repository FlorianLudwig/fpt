import sys
import setuptools
import imp


def get_setup_data(path):
    """get the arguments of setup() call inside a setup.py by executing it

    The only way to get data out of a setup.py is by executing it.  The setuptools
    setup() function is mocked to extract the desired information

    :param path: path to the setup.py file
    :type path: str
    :rtype: dict
    """
    data = {}

    old_setup = setuptools.setup
    old_modules = sys.modules.keys()

    def s(**kwargs):
        data.update(kwargs)

    setuptools.setup = s
    imp.load_source('fake-load-setup-py', path)

    for module in sys.modules.keys():
        if module not in old_modules:
            del sys.modules[module]

    setuptools.setup = old_setup
    return data
