**Notice: A new release is available (0.9.1) which addresses a recent change to the format of Amazon .amz files. Older versions of Pymazon will no longer work with new Amazon purchases. Please update to this new version.**

**If you are feeling generous, you could help support my ~~beer fund~~ work on Pymazon by donating a couple bucks:**

[https://www.paypal.com/en\_US/i/btn/btn\_donateCC\_LG.gif ](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=sccolbert%40gmail%2ecom&lc=US&item_name=Pymazon&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)

**If you maintain a distro package of Pymazon, or you are using a distro packaged version of Pymazon, please let me know (<my googlecode username>@gmail.com) so I can keep a list of where it is being used, and keep the maintainers informed of new releases. Thanks!**

# Pymazon #

**Pymazon runs on PyQt4!**

![http://pymazon.googlecode.com/files/pymazonqt_screen.png](http://pymazon.googlecode.com/files/pymazonqt_screen.png)

**Pymazon runs on PyGtk!**

![http://pymazon.googlecode.com/files/pymazongtk_screen.png](http://pymazon.googlecode.com/files/pymazongtk_screen.png)

**Pymazon runs on the command line!**

![http://pymazon.googlecode.com/files/pymazoncmd_screen.png](http://pymazon.googlecode.com/files/pymazoncmd_screen.png)

**That's three times as many options as the official Amazon downloader!**


---

## Summary ##
**Current Version = 0.9.1**

This project is a python implemented downloader for the amazon mp3 store.

The propietary Amazon downloader for Linux just, well, it's not good. Seriously guys, C++ and boost for a downloader!??! Not to mention there are no 64-bit Linux builds and they are like 2 release behind for Ubuntu. Ugh.

**Pymazon DOES NOT depend on Clamz!** There are a few wiki's and smaller distros
packaging Pymazon with a Clamz dependency. This is unnecessary. However
giving credit where it is due, Clamz cracked the Amazon encryption, so without that
project Pymazon probably wouldn't exist.

The only dependency outside of the Python standard library is [PyCrypto](http://www.pycrypto.org) (and PyQt4 >= 4.5 or PyGtk if you want to use the GUI).

Though it was made to solve an issue for Linux users, Pymazon runs just fine on Windows.

---

## Installation ##
Pymazon was made to provide an alternative to the Linux version of the Amazon
dowloader (and hopefully avoid most the issues that plague it). That said,
it should still run just fine under Windows.

First, make sure you have [PyCrypto](http://www.pycrypto.org) installed.
On Ubuntu:

```
$ sudo apt-get install python-crypto
```

or

```
$ pip install pycrypto
```

If you don't have pip installed, you can get it from the cheeseshop.
I recommend pip over setuptools.

```
$ easy_install pip
```

If you want to use the GUI, you will need to have PyQt4 or PyGtk installed.
On Ubuntu:

```
$ sudo apt-get install python-qt4
```
or
```
$ sudo apt-get install python-gtk2
```

Once you have PyCrypto (and optionally PyQt4 of PyGtk) installed,
you can install Pymazon.

To get Pymazon from the cheeseshop:

```
$ pip install pymazon
```
or
```
$ easy_install pymazon
```

If you're not using virtualenv, you may need to sudo.

Or, to build/install Pymazon yourself (there's really nothing to _build_):

```
$ wget http://pymazon.googlecode.com/files/Pymazon-0.9.1.tar.gz
$ tar -xzf Pymazon-0.9.1.tar.gz
$ cd Pymazon-0.9.1
$ sudo python setup.py install
```

or, if you want to install locally

```
$ python setup.py install --user
```

If you install locally, you may need to symlink ~/.local/bin/pymazon
to a folder on your PATH

You can also download the bleeding-edge source with Mercurial:

```
$ hg clone https://pymazon.googlecode.com/hg/ pymazon 
```

Then just build/install it via:

```
$ python setup.py install
```

---

## Use ##
First, read HowToAmzDownload.

Currently, pymazon can be used from the command line or the GUI
(which requires PyQt4 >= 4.5 or PyGtk).

### _GUI Interface_ ###
To Launch Pymazon in GUI mode:
```
$ pymazon 
```
The GUI is pretty self explanatory.

### _Command Line Interface_ ###
To download to current directory:
```
$ pymazon -c /path/to/amz/file/foo.amz
```
To download to alternate directory:
```
$ pymazon -c -d /path/to/save/dir/ /path/to/amz/file/foo.amz
```

If you get stuck:
```
$ pymazon --help
```

---

### _Name Templates_ ###
Pymazon supports name templates for the save name of the file.

A name template is a string of the form:
```
${argument}whatevertextyouwant
```
Valid arguments include:
> title
> artist
> tracknum
> album

For example, suppose the current name template is
```
${tracknum} - ${title}
```
The for a song spam.mp3 that is number 05 on the album, and a save directory of
/ham/eggs, then the song will be written to disk as:
```
/ham/eggs/05 - spam.mp3
```
The templates are flexible. Suppose you have a template of the form:
```
${artist}/${album}/${tracknum} - ${title}
```
and a save directory ~/Music, then every song in the .amz file will be written
to disk as:
```
~/Music/artist/album/tracknum - title
```
This is the format used by the author of Pymazon.

---

### _Configuration File_ ###
Pymazon supports a pymazonrc file located at ~/.pymazon/pymazonrc
For windows users this path is the output of
```
>>> import os
>>> os.path.join(os.path.expanduser('~'), '.pymazon', 'pymazonrc')
```

This file is created automatically when Pymazon first starts.

If you use the GUI interface, you don't need to worry about this file
as Pymazon handles everything via the settings dialog. However, if
you are a command line user, you can make your life easier by
tweaking the settings in the file to your liking. The config
file is pretty self explanatory.


---

## Stuff ##
If you get _**Error!**_ printed to the console or status box when downloading,
Pymazon will create a log file in the .pymazon/logs directory.
This log will have more information about what caused
the failure and the specifics of the track it was trying to download.
The usual cause for errors are due to no internet connection (in which case
you won't see album art in the GUI) or an expired .amz file
(i.e. the Amazon download links have expired). If you get an error, and the
link in the log file is valid (you can use it from a web browser), then please
file a bug report and include the log as an attachment.

Errors not related to downloading will show up as exceptions with (hopefully)
useful error messages.

I appreciate comments, suggestions, and bug reports.

That's about it.

SCC