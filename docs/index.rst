================================
Welcome to the Grenz-er-fahrung!
================================

As part of the WirvsVirus_ hackathon we join the fight against COVID-19.

.. _WirvsVirus: https://wirvsvirushackathon.org/

Introduction
============

The last couple of weeks were defined by the spread of the virus around the world. Europe, in particular, rapidly became the epicentre of the current epidemic. As a consequence borders throughout Europe were closed in a rush leading to haevy traffic jams. Europe's economy, famous for its free and borderless markets, risks being halted due to merchants, commuters, and truckers being stuck attempting to cross a border.

For this weekend we chose to **hack** together a prototype app which allows officials to provide questionnairies digitally, enabling border crossers to answer questions in advance and reduce the work of border policemen.

Introduction
============

Consider the following user story:

.. topic:: A truck driver delivering goods throughout Europe

   On his journey the truck driver travels from country A to B but does not speak the language spoken in country B fluently.

   How can the time of the border crossing be minimized?

   A policeman of country B at the border will want to know the truck drivers identity, his destination and reasons of travel. Most of the time will be lost communicating and answering questions while overcoming the language barrier.

   .. note:: What if the truck driver could answer the questions in advance, **in his own language**?
      
      The time it would take for the policeman to verify the answers would be only a fraction of the time it currently takes and seriously reduce traffic jams all over Europe's closed borders.


Application
===========

We took this scenario as a guide-line for our application and decided to write the following tools:

* A questionnaire generator which allows officials upload and distribute questionnairies to people who want to cross their border.
* A client webapp which allows anyone to answer the questions in their own language and generate a QR-Code containing the answers as a URL.
* A website containing the answers in the policeman's language.

Therefore allowing policemen to get answers to all questions they are supposed to ask just by scanning a QR-Code!

In the following the details of our implementation are documentated.

Questionnaire Generator
-----------------------

Border Crosser Webapp
---------------------

Border Police Website
---------------------

Backend: Connecting the Pieces
------------------------------

Contents
========
.. toctree::
   :glob:
   :maxdepth: 2

   source/source_files/project

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
