# Scraping-Alba
Script to scrap data from Legislative Assembly of Bahia website

This program was tested in Debian Jessie and Wheezy

Before using this script, set locale to pt-br utf-8

To do this run the command "sudo dpkg-reconfigure locales" and choose pt_BR.UTF-8 UTF-8

USAGE: script.py INDICE_OF_THE_DEPUTIE RANGE_OF_DEPUTIES

Example: script.py 1 33 // It will scrap data from all the deputies from the 1st to the 33th

List of deputies available at http://www.al.ba.gov.br/deputados/Prestacao-de-Contas.php.
