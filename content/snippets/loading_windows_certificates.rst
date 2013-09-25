Loading certificates from the Windows Root Authorities Store
============================================================

:date: 2013-09-24 19:16
:category: Snippets
:tags: cpp, code, certificate, ssl

Here is how you load certificates from the root store on Windows in CPP, to include it in an OpenSSL context:

.. code-include:: cpp/cacerts-windows.cpp
    :lexer: cpp

