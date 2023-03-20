.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

================================
collective.restapi.facetedsearch
================================

This addon provides Plone-REST-Api endpoints for a faceted search. The GET endpoint is highly inspired by the REST-Api search and the POST endpoint is highly inspired by the REST-Api querystringsearch. Configuration of facets must be done by overloading GroupByCriteria of collective.collectionfilter

Features
--------

- Can be bullet points


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install collective.restapi.facetedsearch by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.restapi.facetedsearch


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://https://git.saw-leipzig.de/muellers/collective.restapi.facetedsearch/-/issues
- Source Code: https://git.saw-leipzig.de/muellers/collective.restapi.facetedsearch.git
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
