#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
 
# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import privaan


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        os.system("chmod +x /etc/init.d/privaanservice")
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        username = raw_input("Enter the username for sender: ")
        password = raw_input("Enter the password for sender: ")
        sender_email = raw_input("Enter the email for the sender: ")
        sender_receivers = raw_input("Enter the emails for receivers (coma separated): ")
        os.system("rm privaan/config.py && touch privaan/config.py")
        f = open('privaan/config.py', 'w')
        
        f.write('username = \''+username+'\'\n')
        f.write('password = \''+password+'\'\n')
        f.write('fromaddr = \''+sender_email+'\'\n')
        f.write('toaddrs = \''+sender_receivers+'\'\n')
        f.close()
        install.run(self)
        os.system("chmod +x /etc/init.d/privaanservice")

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(
 
    # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
    name='privaan',
 
    # la version du code
    version=privaan.__version__,
 
    # Liste les packages à insérer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),
 
    # votre pti nom
    author="Stephen KINGER",
 
    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ça implique.
    author_email="",
 
    # Une description courte
    description="Tool to monitor apache logs and notify on connexions",
 
    # Une description longue, sera affichée pour présenter la lib
    # Généralement on dump le README ici
    long_description=open('README.md').read(),
 
    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # Une url qui pointe vers la page officielle de votre lib
    url='http://github.com/StephenKinger/privaan',
 
    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: WIP",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
    ],
 
    install_requires=[
        'mock',
        'pygtail',
        'docopt==0.6.2',
    ],
    
    data_files=[('/etc/init.d', ['daemon/privaanservice'])],

 
    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme "django-admin".
    # Par exemple, si on veut créer la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # créé automatiquement. 
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'privaan = privaan:privaan_run',
        ],
    },
 
    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="MIT",
 
    # Il y a encore une chiée de paramètres possibles, mais avec ça vous
    # couvrez 90% des besoins
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
 
)
