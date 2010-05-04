Introduction
============

prettyPhoto is a jQuery based lightbox clone. Not only does it support images, it also add support for videos, flash, YouTube, iFrames. It's a full blown media lightbox. The setup is easy and quick, plus the script is compatible in every major browser.

The original implementation can be found here: http://www.no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/

This plugin has been tested and is known to work in the following browsers

* Firefox 2.0+

* Safari 3.1.1+

* Opera 9+

* Internet Explorer 6.0+

`collective.prettyphoto` integrates prettyPhoto 2.5.5 into Plone.

Installing
==========

This package requires Plone 3.x or later (tested on 3.3.3).

Installing without buildout
---------------------------

Install this package in either your system path packages or in the lib/python
directory of your Zope instance. You can do this using either easy_install or
via the setup.py script.

Installing with buildout
------------------------

If you are using `buildout`_ to manage your instance installing
collective.prettyphoto is even simpler. You can install
collective.prettyphoto by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.prettyphoto

After updating the configuration you need to run the ''bin/buildout'', which
will take care of updating your system.

.. _buildout: http://pypi.python.org/pypi/zc.buildout


Usage
=====

collective.prettyphoto adds a new view for Topics, Folders and Large Plone Folders: Thumbnail view (prettyPhoto).

To use prettyPhoto for inline elements just add 'prettyPhoto' from the styles menu (Kupu and TinyMCE) to the link.


Configuration
=============

collective.prettyphoto can be customized via property sheet (go to ZMI, portal_properties, prettyphoto_properties).

* theme:

  * dark_rounded

  * dark_square

  * facebook

  * light_rounded (default)

  * light_square

* speed:

  * fast

  * normal (default)

  * slow

* opacity: value from 0.0 to 1.0 (default: 0.80)

* show_title: show the title for images? (default: True)

* counter_sep: the separator for the gallery counter 1 "of" 2 (default: "/")

* autoplay: automatically start videos? (default: True)

* iframe_width: the width of the iframe (must be percantage, default: 75%)

* iframe_height: the height of the iframe (must be percantage, default: 75%)

Copyright and Credits
=====================

prettyPhoto is developed by Stephane Caron (http://www.no-margin-for-errors.com) and is licensed under Creative Commons Attribution 2.5.

Author of collective.prettyphoto: Thomas Massmann (thomas.massmann@inqbus.de).