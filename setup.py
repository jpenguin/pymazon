#!/usr/bin/env python
"""
Pymazon - A Python based downloader for the Amazon.com MP3 store
Copyright (c) 2010 Steven C. Colbert

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.command.install_scripts import install_scripts
from distutils.core import setup


class InstallScripts(install_scripts):
    '''create the bat for windows so the launcher script
    works out of the box'''
    def run(self):
        import os
        if os.name == 'nt':
            import sys
            parts = os.path.split(sys.executable)
            py_path = os.path.join(*(parts[:-1]))
            script_path = os.path.join(py_path, 'Scripts')
            f = open(os.path.join(script_path, 'pymazon.bat'), 'w')
            pymazon = os.path.join(script_path, 'pymazon')
            bat = '@' + ('"%s" "%s"' % (sys.executable, pymazon)) + ' %*'
            f.write(bat)
            f.close()
        install_scripts.run(self)


setup(name='Pymazon',
      version='0.9.1',
      description='Python Based Downloader for the Amazon mp3 Store',
      author='S. Chris Colbert',
      author_email='sccolbert@gmail.com',
      url='http://code.google.com/p/pymazon/',
      package_dir = {'pymazon': './pymazon'},
      packages=['pymazon', 'pymazon.core', 'pymazon.qt', 'pymazon.gtk',
                'pymazon.qt', 'pymazon.resource', 'pymazon.util',
                'pymazon.cmd'],
      package_data={'pymazon.resource': ['icons/*.png'],
                    'pymazon.qt': ['*.ui'],
                    'pymazon.gtk': ['*.glade']},
      scripts=['./bin/pymazon'],
      license='GPLv3',
      long_description=\
'''Pymazon is a Python implemented alternative to the Amazon mp3 downloader.
It allows you to download legally purchased mp3's from the Amazon mp3 store
using the .amz file provided by Amazon after the purchase. Pymazon can be
used as both a command line client or a gui (if PyQt4 or PyGtk is installed). 
The only hard external dependency is PyCrypto, which is available in the
Ubuntu (and likely other distro's) repositories (python-crypto),
and the cheese shop.''',
      cmdclass={'install_scripts': InstallScripts},
     )
