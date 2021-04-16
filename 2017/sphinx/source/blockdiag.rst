
Dessiner un graphe avec Sphinx
==============================

Cet exemple s'appuie sur l'extension
`sphinxcontrib-blockdiag <http://blockdiag.com/en/blockdiag/sphinxcontrib.html>`_.

.. blockdiag::
   :desctable:

   blockdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }
