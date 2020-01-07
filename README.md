# Python coding test

## Introduction

Understanding our genes e.g., what they do, which processes they are
part of, and where the proteins they code for are found, is of utmost
importance for many kinds of research, including bioinformatics. To
facilitate this, the scientific community has developed *Gene
Ontology*, or just *GO*, which is an extensive database of
  * various properties a gene can have, and
  * information on how these properties relate to each other.
  
In this test we will work with some Python code that reads in the Gene
Ontology database in a suitable data structure and processes the data
in certain ways. This code could be one of the first steps in creating
a web based browser for Gene Ontology and related data resources.

For this test you do not need to understand the many different
properties the Gene Ontology describes, however you will need to have
a good understanding of Python, be able to think logically, and know a
few things about the Gene Ontology database which are described in the
following.

The properties that a gene can have are called *GO categories*. In the
data we will be working with, there are 47,385 different GO
categories. Each GO category has an `id`, e.g. `GO:0008150`, a more
descriptive `name`, e.g. `biological_process`, and a few other
attributes.

How the GO categories relate to each other is captured in *relations*
that are composed of *relationships*. There are a number of different
relations, and the most important of these is the `is_a` relation. For
example, the GO category with `id` equal to `GO:0000003` and `name`
equal to `reproduction` forms a relationship in the `is_a` relation to
`GO:0008150` (`biological_process`), i.e. `reproduction` `is_a `
`biological_process`. There are a number of other types of
relations. Another example is `part_of`, where one of the
relationships is `GO:0098687` (`chromosomal region`) is `part_of`
`GO:0005694` (`chromosome`).

Mathematically speaking, a relationship is a pair of categories, and a
relation is a set of relationships.

You can *invert* a relation, e.g. create the relation `has_part` from
`part_of` by saying that category *a* `has_part` category *b* if
category *b* is `part_of` category *a* (note that *a* and *b* swapped
place).

Relations can also be combined, e.g. you can construct a new relation
`my_rel` from `is_a`and `part_of` by saying that two categories are
related with `my_rel` if they are related with at least one of the
`is_a` or `part_of` relations.

Some relations are *transitive*, meaning that if *a* is related to
*b*, and *b* is related to *c*, then *a* is also related to *c*. The
`is_a` relation is transitive, e.g. we have the relationship
`GO:0019953` (`sexual reproduction`) `is_a` `GO:0000003`
(`reproduction`), and as we also have the relationship `GO:0000003`
(`reproduction`) `is_a` `GO:0008150` (`biological_process`), we know
that we have the relationship `GO:0019953` (`sexual reproduction`)
`is_a` `GO:0008150` (`biological_process`). However these indirect
relationships are not explicitly stated in the Gene Ontology database.

There are other aspects of the Gene Ontology database that we don't
need to know about for now. If you are interested, you can look at
http://geneontology.org for more information.

## Materials

In addition to this document, three other files have been provided:
  * The `go.obo` file contains the Gene Ontology database in a fairly
    simple text-based format. This file was downloaded from
    http://purl.obolibrary.org/obo/go.obo and is licensed under the
    [Creative Commons Attribution 4.0 International Public License][1].
    Please see http://geneontology.org for more information.
  * The `GO.py` file contains code for parsing the `go.obo` file and
    storing the information using three classes defined in the `GO.py`
    file.
  * The file `test_GO.py` defines a number of functions that help
    testing the code in `GO.py`.

[1]: https://creativecommons.org/licenses/by/4.0/legalcode

## Tasks

### 1. Understand the provided code

Take a look at the provided code in `GO.py`. There are three classes
defined. The `GO` class can be used to make an object representing the
information in the `go.obo` file. To do this, it uses two other
classes, `GO_category` and `GO_relation`.

Try to understand what the code does. It may help to add some comments
or doc strings as you go.

### 2. Fix a bug

The file `test_GO.py` defines a number of functions that can be used
to test the code in `GO.py`. You can run the tests using the Python
module `pytest`.

One of the tests fails. If you look at the lines 206-217 in `go.obo`
that define the GO category `GO:0000022` (`mitotic spindle
elongation`) you will see that `GO:0000022` should be related to two
other GO categories, but for some reason no relationships are are
stored in our data structure. Fix this bug before proceeding to the
next tasks.

### 3. Implement inverting relations

Add code that finds the inverse of a relation as described in the
[Introduction](#introduction) section.

### 4. Implement combining relations

Add code that creates a new relation by combining two others as
described in the [Introduction](#introduction) section.

### 5. Implement making a relation transitive

As was described in the [Introduction](#introduction) section, the
`is_a` relation is transitive, but all the indirect relationships are
not explicitly mentioned in the `go.obo` file. Implement code that
adds these indirect relationships.

## Notes

All this code should run with Python 3 on an ordinary PC or
server. CPU and memory requirements should be modest.

We are aware that some of the tasks are difficult and time
consuming. We will not be surprised if you need to put several hours
of work into solving them.

You are welcome to search the Internet for help, but we will expect
you to be able to explain the code that you come up with.

Also, we will kindly ask you not to actively make other people aware
of this test, as we would like to use it for future interviews.

Please provide us your code to solve the tasks the day before the
interview so that we can familiarize ourselves with your solutions.
