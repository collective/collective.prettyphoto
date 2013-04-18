Changelog
=========

0.5 (2013-04-18)
----------------

- Documentation updates
  [saily]

- Upgrade to prettyPhoto 3.1.5
  [saily]

- Add ui-tests using robotframework to validate views.
  [saily]

- Add travis integration for Plone 4.3.x, Plone 4.2.x, Plone 4.1.x and
  Plone 4.0.x. Plone 3.3.x cannot be tested with new layered testing structure
  of ``plone.app.testing`` and will never be testable on travis because they
  don't and will never support Python 2.4.

  So we changed primary focus of development to Plone >= 4.0.
  [saily]

- Switchted to ``plone.app.testing`` and added some basic installation tests.
  [saily]

- Add egg-containing buildout and bootstrap.py
  [saily]

- Use ``zcml:condition="installed plone.app.collection"`` to switch to a new
  GS profile which appends prettyphoto views to Collection instead Topic type.
  [saily]

- Refactor GS profiles and depend each profile on a 'extended' profile which
  hold generic stuff as registering css and js. Generic setup takes the first
  profile which is found in folder, so this has to be alpha-sorted behind
  'default'.
  [saily]


0.4.5.2 (2012-09-12)
--------------------
- more manifest packaging madness

0.4.5.1 (2012-09-12)
--------------------

- fix bug with sdist packaging
  [jensens]

0.4.5 (2012-09-11)
------------------

- corrected the global js-function
  [bennyboy]

- Made it possible to later (i.e. after ajax calls) bind prettyphoto
  to images. thus we have a global js-function plonePrettyPhotoEnable now.
  Also did some housekeeping, added integrated buildout, gitignore, ...
  [jensens]

0.4.4 (2011-12-02)
------------------

- Added possiblity to provide custom markup by subclassing the
  view that creates the prettyphoto configuration.
  (see ``browser.view.Javascript.markup``)
  [fRiSi]

0.4.3 (2011-07-22)
------------------

- Fixed parameter names used to configure prettyPhoto
  and added autoplay_slideshow.

  Previously titles have been shown although ``show_title`` has been set to
  ``False`` in ``prettyphoto_properties``.
  [fRiSi]

- Finish update to 3.1.2 by updating css and images and adding the new `pp_default`
  theme (which is the new default btw ;-)
  [fRiSi]

0.4.2 (2011-07-13)
------------------

- Upgraded to prettyPhoto 3.1.2 and implemented two new properties:
  deeplinking , social_tools
  [petschki]

0.4.1 (2011-03-22)
------------------

- Upgraded to prettyPhoto 3.0.3 .
  This fixes thumbnails in overlay_gallery partly because the regular expression
  now looks for a (jpg|jpeg|png|gif) within the whole url. if your originaly
  linked images are completely without this, they still wont show up.
  [petschki]

- fixed overlay_gallery property defaults to "False"
  [petschki]

0.4.0 (2011-02-23)
------------------

- Upgraded to prettyPhoto library including it's css and image sprite to 3.0.1
  to fix issues with jQuery 1.4.4 (see http://bit.ly/hxYUrt) which is shipped
  with latest Plone 4 by default. This fixes #2.
  [saily]

- Added default thumbnails for 'overlay_galleries' feature.
  [saily]

- Added 'overlay_gallery' and 'slideshow' as additional configuration options
  but disabled by default cause of a bug in jquery.prettyPhoto.js which avoids
  displaying thumbnails not ending on (jpg|jpeg|png|gif).
  See http://bit.ly/eKYdrF
  [saily]

0.3.3 (2010-12-20)
------------------

- Fixed iframe configuration (width was used for height too)
  [fRiSi]

0.3.2 (2010-07-10)
------------------

- Fixed install issue with Plone 4 (Large Plone Folder was removed).
  [hpeteragitator]

- Set version in metadata.xml to 1, since this has nothing to do with the package version.
  [tmassman]

0.3.1 (2010-05-19)
------------------

- Fixed version numbers and missing upgrade steps.
  [tmassman]

- Added custom browserlayer.
  [tmassman]

- Upgrade to prettyPhoto 2.5.6
  [tmassman]

0.3 (2010-05-17)
----------------

- Don't fail when installing on sites w/o kupu (plone4 compatibility).
  [fRiSi]

0.2 (2010-01-03)
----------------

- Fixed wrong kupu styles.
  [tmassman]

- Added iFrame support (use 'prettyPhoto Iframe Link' for external sites)
  [tmassman]


0.1 (2009-12-29)
----------------

- Initial release
  [tmassman]

