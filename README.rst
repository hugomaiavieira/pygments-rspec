Pygments RSpec
==============

This is an extension of Ruby lexer that just add some keywords used on RSpec_,
including some keywords used with Capybara_ too.

.. _RSpec: http://rspec.info
.. _Capybara: https://github.com/jnicklas/capybara


Install
+++++++

Using PyPI and pip
------------------

::

    $ (sudo) pip install pygments-rspec


Manual
------

::

    $ git clone git://github.com/hugomaiavieira/pygments-rspec.git
    $ cd pygments-rspec
    $ (sudo) python setup.py install


Using
+++++

Just use the **rspec** "language".


Using in LaTeX documents
++++++++++++++++++++++++

See the minted package at http://minted.googlecode.com.


Extra information
+++++++++++++++++

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/