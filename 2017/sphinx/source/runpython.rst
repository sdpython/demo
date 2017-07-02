

Inclure un script Python
========================

Pour inclure un script, il suffit d'utiliser ``::`` :

::

    ::
    
        import sys
        print(sys.version_info)
        
Admettons maintenant qu'on souhaite inclure le
résultat du programe dans la documentation. Pour faire cela,
il faut inclure l'extension 
`pyquickhelper.sphinxext.sphinx_runpython_extension <https://github.com/sdpython/pyquickhelper/blob/master/src/pyquickhelper/sphinxext/sphinx_runpython_extension.py>`_.
Le fichier `conf.y` est modifié :

::

    extensions = ['sphinx.ext.intersphinx',
        ...
        'pyquickhelper.sphinxext.sphinx_runpython_extension']

On utilise la directive ``.. runpython::`` :

::

    .. runpython::
    
        import sys
        print(sys.version_info)
        
Ce qui donne :
        
.. runpython::
    
    import sys
    print(sys.version_info)
    
On peut également inclure le code avec l'option
``:showcode:``

::

    .. runpython::
        :showcode:
        
        import sys
        print(sys.version_info)

Ce qui donne :

.. runpython::
    :showcode:
    
    import sys
    print(sys.version_info)
    
Ou avoir une sortie au format de la documentation.
Le code suivant récurpère la liste de fichiers et l'affiche.

::

    .. runpython::
        :showcode:
        :rst:
        
        import os
        for name in os.listdir('.'):
            print("* `{0}`".format(name))

Ce qui donne :

.. runpython::
    :rst:
    
    import os
    for name in os.listdir('.'):
        print("* `{0}`".format(name))
