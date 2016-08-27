Easy_Network( Python3 scripts ) Under development.
==================================================

easy_network provide python3 network scripts. For example, to get a page form a web server.
easy_network supports mulit-threadin.g

Requirements
------------

* Python > 3.5.1

Set Up
------

Install virtualenv. (for protecting your Home environment.)

.. code-block:: bash
   
   python3 -m pip install -U pip setuptools
   python3 -m pip install virtualenv
   # or
   pip3 install virtualenv

activate virtualenv

.. code-block:: bash
   
   virtualenv -p python3 venv
   source venv/bin/activate
   # Removing virtual environment
   # (venv) deactivate
   
build & install
---------------

.. code-block:: bash
   
   pip install git+https://github.com/Moguf/easy_network.git
   # or 
   git clone https://github.com/Moguf/easy_network.git
   cd enet_network
   python setup.py build
   python setup.py install
   
How to use
----------

.. code-block:: python

   from enet import Downloader
   url = ['http://www.google.com','http://yahoo.co.jp','https://github.com']
   tmp = Downloader(url)
   tmp.gets()
