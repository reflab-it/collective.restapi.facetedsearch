# -*- coding: utf-8 -*-
from collective.collectionfilter.interfaces import IGroupByCriteria
from collective.collectionfilter.interfaces import IGroupByModifier
from zope.component import adapter
from zope.interface import implementer
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from collective.taxonomy.interfaces import ITaxonomy
from plone.api import portal


@implementer(IGroupByModifier)
@adapter(IGroupByCriteria)
def groupby_modifier(groupby):
    pass
    # groupby._groupby['tax_ou_type']['display_modifier'] = lambda x: getVocabTitle(x, 'tax_ou_type')
    # groupby._groupby['license_short_title']['display_modifier'] = lambda x: getVocabTitle(x, 'license_short_title')
    # groupby._groupby['tax_research_fields']['display_modifier'] = lambda x: getVocabTitle(x, 'tax_research_fields')
    # groupby._groupby['taxonomy_ddc']['display_modifier'] = lambda x: getVocabTitle(x, 'taxonomy_ddc')
    # groupby._groupby['taxonomy_stock_categories']['display_modifier'] = lambda x: getVocabTitle(x, 'taxonomy_stock_categories')


def getVocabTitle(token, metadata_name):
    mappings = portal.get_registry_record(name='saw.facetedsearch.metadata_vocab_mapping', default={})
    if metadata_name in mappings:
        vocabname = mappings[metadata_name]
        taxonomy = queryUtility(ITaxonomy, name=vocabname)
        if taxonomy:
            title = taxonomy.translate(token)
            return title
        else:
            vocab = queryUtility(IVocabularyFactory, name=vocabname)
            if vocab:
                term = vocab().getTermByToken(token)
                if term and term.title:
                    return term.title

    return token
