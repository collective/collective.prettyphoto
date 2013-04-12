.. image:: https://travis-ci.org/collective/collective.prettyphoto.png
   :target: https://travis-ci.org/collective/collective.prettyphoto

.. contents::

Introduction
============

prettyPhoto_ is a jQuery based lightbox clone. It supports images,
it also add support for videos, flash, YouTube, iFrames and ajax.

It's a full blown media lightbox. The setup is easy and quick, plus the
script is compatible in every major browser.

This plugin has been tested and is known to work in the following
browsers:

* Firefox 3.0+
* Google Chrome 10.0+
* Internet Explorer 6.0+
* Safari 3.1.1+
* Opera 9+


`collective.prettyphoto` integrates prettyPhoto 3.1.5 into Plone.

Installing
==========

Development focus is now set to Plone 4.x. Currently all 4.x versions
are tested on `Travis CI`_. Plone 3.x is no longer officially supported.


Installing without buildout
---------------------------

Install this package in either your system path packages or in the
``lib/python`` directory of your Zope instance. You can do this using
either easy_install or via the ``setup.py`` script.

Installing with buildout
------------------------

If you are using buildout_ to manage your instance installing
collective.prettyphoto is even simpler. You can install
collective.prettyphoto by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.prettyphoto

After updating the configuration you need to run the ``bin/buildout``,
which will take care of updating your system.


Usage
=====

collective.prettyphoto adds a new view for Collections and Folders:
Thumbnail view (prettyPhoto).

To use prettyPhoto for inline elements just add ``prettyPhoto`` from the
styles menu in TinyMCE to the link.


Configuration
=============

collective.prettyphoto can be customized via property sheet (go to ZMI,
portal_properties, prettyphoto_properties).

* theme:

  * pp_default (default)

  * dark_rounded

  * dark_square

  * facebook

  * light_rounded

  * light_square

* speed:

  * fast

  * normal (default)

  * slow

* opacity: value from ``0.0`` to ``1.0``
  (default: ``0.80``)

* show_title: show the title for images?
  (default: ``True``)

* counter_sep: the separator for the gallery counter 1 "of" 2
  (default: "/")

* autoplay: automatically start videos?
  (default: ``True``)

* iframe_width: the width of the iframe
  (must be percantage, default: ``75%``)

* iframe_height: the height of the iframe
  (must be percantage, default: ``75%``)

* overlay_gallery: If set to true, a gallery will overlay the fullscreen image
  on mouse over (default: ``False``, the bug (http://bit.ly/eKYdrF) is fixed
  since 0.4.1 (pP 3.0.3) but your image url has to contain
  (jpg|jpeg|png|gif) somewhere)

* slideshow: interval time in ms, ``0`` to disable slideshow
  (default: ``0``)

* autoplay_slideshow: automatically start slideshow?
  (default: ``False``, only woks when slideshow > ``0``)

* deeplinking: rewrite the browser location to enable directlinks to
  overlay images (default: ``False``)

* social_tools: html markup for social links within image overlays
  (twitter, FB, ...) (default: empty) see http://bit.ly/pDQ19A for detailed
  information


Copyright and Credits
=====================

prettyPhoto_ is developed by Stephane Caron
(http://www.no-margin-for-errors.com) and is licensed under Creative
Commons Attribution 2.5.

Author of collective.prettyphoto: Thomas Massmann (thomas.massmann@inqbus.de).

Contributors (alphabetically)

* fRiSi
* hpeteragitator
* jensens
* petschki
* saily

.. _prettyPhoto: http://www.no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/
.. _buildout: http://pypi.python.org/pypi/zc._buildout
.. _`Travis CI`: http://travis-ci.org/collective/collective.prettyphoto
