#!/usr/bin/env python
"""
pymazon - A Python based downloader for the Amazon.com MP3 store
Copyright (c) 2009 Steven C. Colbert

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

import os, sys, logging
from optparse import OptionParser


# setup logging
current_dir = os.getcwd()
if not os.access(current_dir, os.W_OK):
    msg = 'Pymazon must be started from a directory with write access.'    
    raise RuntimeError(msg)
LOG_FILENAME = os.path.join(current_dir, 'pymazon_error_log.txt')
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=LOG_FILENAME, format=fmt)


def validate_sysargs(args):
    if len(args)!=1:
        raise ValueError('A single positional argument must be supplied.')
        sys.exit()            
    amz_file = args[0]
    if not os.path.isfile(amz_file):
        raise ValueError('Amz file not found.')
        sys.exit()
    if not amz_file.endswith('.amz'):
        raise ValueError('Positional argument must be a path to a .amz file.')
        sys.exit()        
    return amz_file    
    
    
def main():
    parser = OptionParser()    
    parser.add_option('-d', '--dir', dest='save_dir', 
                      help='Directory in which to save the downloads', 
                      default=os.getcwd())
    parser.add_option('-g', '--gui', dest='gui', 
                      help='Launch the program in GUI mode',
                      action='store_true', default=False)
                      
    (options, args) = parser.parse_args()
    
    if options.gui:
        try:
            from pymazongui import MainWindow
            from PyQt4.QtGui import QApplication
        except ImportError:
            msg = 'Unable to import PyQt4, which is required to run Pymazon in '
            msg += 'GUI mode. It can still be used from the command line. '
            msg += 'Simply start Pymazon without the -g switch.'
            raise ImportError(msg)
        if args:
            amz_file = validate_sysargs(args)
        else:
            amz_file = None
        app = QApplication([])
        win = MainWindow(amz_file)
        win.show()
        app.exec_()
        
    else:
        from pymazonbackend import parse_tracks, Downloader
        amz_file = validate_sysargs(args)
        save_dir = options.save_dir   
        if not os.access(save_dir, os.W_OK):
            msg = 'Unable to write to target directory. '
            msg += 'Ensure the directory exits and write permission is granted.'
            raise RuntimeError(msg)
            sys.exit()
            
        def dl_printer(track, status):
            if status == 1:
                print('Downloading track %s by %s on album %s. ' 
                      % (track['title'], track['artist'], track['album']))
            elif status == 2:
                print 'Complete!\n'
            elif status == 3:
                print 'Error - Check Log!'
            elif status == 4:
                print 'Downloads Complete!'
            else:
                pass
            
        parsed_tracks = parse_tracks(amz_file)        
        dl = Downloader(save_dir, parsed_tracks, dl_printer)
        dl.start()
        dl.join()        
    
    
if __name__=='__main__':  
    main()
    
        