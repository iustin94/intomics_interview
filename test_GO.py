#!/usr/bin/env python3

import pytest
import GO

def test__pop_single_value_1():
    attributes = { '42': ['answer'], 'foo': ['bar'] }
    answer = GO._pop_single_value('42', attributes)
    assert answer == 'answer'
    assert attributes == { 'foo': ['bar'] }

def test__pop_single_value_2():
    with pytest.raises(KeyError):
        GO._pop_single_value('42', {})

def test__pop_single_value_3():
    with pytest.raises(ValueError):
        GO._pop_single_value('42', { '42': [ '1', '2' ]})

def test__pop_single_value_4():
    with pytest.raises(ValueError):
        GO._pop_single_value('42', { '42': [ ]})

def test__pop_single_value_5():
    with pytest.raises(TypeError):
        GO._pop_single_value('42', None)

def test_GO_category_1():
    category = GO.GO_category({'id': [ '42' ], 'name': [ 'fortytwo' ], 'def': [ 'answer' ]})
    assert category.id == '42'
    assert category.name == 'fortytwo'
    assert category.definition == 'answer'
    assert category.others == {}
    assert str(category) == '42 (fortytwo)'
    
def test_GO_relation_1():
    relation = GO.GO_relation({'id': ['rel'], 'name': ['relation']})
    assert relation.id == 'rel'
    assert relation.name == 'relation'
    assert relation.is_transitive == False
    assert relation.others == {}
    assert str(relation) == '<rel>'

def test_GO_relation_2():
    relation = GO.GO_relation({'id': ['rel'], 'name': ['relation'],
                                   'is_transitive': [ 'TRUE' ]})
    assert relation.id == 'rel'
    assert relation.name == 'relation'
    assert relation.is_transitive == True
    assert relation.others == {}
    assert str(relation) == '<rel>'

def test_GO_relation_3():
    relation = GO.GO_relation({'id': ['rel'], 'name': ['relation'],
                                   'is_transitive': [ 'false' ]})
    assert relation.id == 'rel'
    assert relation.name == 'relation'
    assert relation.is_transitive == False
    assert relation.others == {}
    assert str(relation) == '<rel>'

def test_GO_relation_4():
    bp = GO.GO_category({'id': ['GO:0008150'], 'name': ['biological_process'], 'def': ['']})
    mp = GO.GO_category({'id': ['GO:0008152'], 'name': ['metabolic process'], 'def': ['']})
    cp = GO.GO_category({'id': ['GO:0009987'], 'name': ['cellular process'], 'def': ['']})
    m = GO.GO_category({'id': ['GO:0032259'], 'name': ['methylation'], 'def': ['']})
    is_a = GO.GO_relation({'id': ['is_a'], 'name': ['is_a'], 'is_transitive': [True]})
    is_a.add_pair(mp, bp)
    is_a.add_pair(cp, bp)
    is_a.add_pair(m, mp)
    is_a.add_pair(m, bp)  # Because the relation is transitive.
    assert (cp, bp) in is_a
    assert (m, bp) in is_a
    assert (m, mp) in is_a
    assert (mp, bp) in is_a
    assert not (bp, cp) in is_a
    assert not (bp, m) in is_a
    assert not (bp, mp) in is_a
    assert not (cp, m) in is_a
    assert not (cp, mp) in is_a
    assert not (m, cp) in is_a
    assert not (mp, cp) in is_a
    assert not (mp, m) in is_a
    assert is_a[bp] == set()
    assert is_a[cp] == { bp }
    assert is_a[m] == { bp, mp }
    assert is_a[mp] == { bp }
    assert sorted(is_a) == [ (mp, bp ), (cp, bp ), (m, bp), (m, mp ) ]

def test_GO_relation_5():
    bp = GO.GO_category({'id': ['GO:0008150'], 'name': ['biological_process'], 'def': ['']})
    mp = GO.GO_category({'id': ['GO:0008152'], 'name': ['metabolic process'], 'def': ['']})
    cp = GO.GO_category({'id': ['GO:0009987'], 'name': ['cellular process'], 'def': ['']})
    m = GO.GO_category({'id': ['GO:0032259'], 'name': ['methylation'], 'def': ['']})
    is_a = GO.GO_relation({'id': ['is_a'], 'name': ['is_a'], 'is_transitive': [True]})
    is_a.add_pair(mp, bp)
    is_a.add_pair(cp, bp)
    is_a.add_pair(m, mp)
    is_a.add_pair(bp, m)  # Introduce a cycle for testing.
    is_a_copy = is_a.copy()
    assert is_a == is_a_copy
    
def test_GO_1():
    go = GO.GO('go.obo')
    assert 'is_a' in go.relations
    assert 'ends_during' in go.relations
    assert 'happens_during' in go.relations
    assert 'has_part' in go.relations
    assert 'negatively_regulates' in go.relations
    assert 'never_in_taxon' in go.relations
    assert 'occurs_in' in go.relations
    assert 'part_of' in go.relations
    assert 'positively_regulates' in go.relations
    assert 'regulates' in go.relations
    assert 'starts_during' in go.relations
    
def test_GO_2():
    go = GO.GO('go.obo')
    assert len(go.relations['is_a'][go.categories['GO:0000022']]) == 2
