from kitconcept.keywordmanager import _
from plone.autoform import directives
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IKeywordManagerSettings(Interface):
    """Keyword Manager settings stored in the backend"""

    ignore_indexes = schema.TextLine(
        title=_("Ignore indexes"),
        description=_(
            "Indexes of type 'KeywordIndex' that the Keyword Manager shouldn't be able "
            "to manage. These are disallowed intentionally, since managing them could "
            "cause problems. Provide the values as a comma-separated string, e.g. "
            '"block_types, object_provides".'
        ),
        required=True,
        default="block_types, object_provides",
    )

    directives.widget(
        "always_reindex",
        vocabulary="kitconcept.keywordmanager.vocabularies.indexes",
        frontendOptions={
            "widgetProps": {"isMulti": True},
        },
    )

    always_reindex = schema.TextLine(
        title=_("Always reindex"),
        description=_(
            "Indexes that should always be reindexed when merging or deleting "
            "keywords on objects. Most users won't need to configure this. "
            'Provide the values as a comma-separated string, e.g. "block_types, '
            'object_provides".',
        ),
        required=True,
        default="SearchableText",
    )


@adapter(Interface, Interface)
class KeywordManagerControlpanel(RegistryConfigletPanel):
    """Keyword Manager Settings Control panel"""

    title = _("Keyword Manager Settings")
    schema = IKeywordManagerSettings
    schema_prefix = "kitconcept.keywordmanager"
    configlet_id = "KeywordManagerSettings"
    configlet_category_id = "Products"
    group = "Products"
