from wagtail.embeds import format
from wagtail.embeds.exceptions import EmbedException


class MediaEmbedHandler(object):
    """
    MediaEmbedHandler will be invoked whenever we encounter an element in HTML content
    with an attribute of data-embedtype="media". The resulting element in the database
    representation will be:
    <embed embedtype="media" url="http://vimeo.com/XXXXX">
    """
    @staticmethod
    def get_db_attributes(tag):
        """
        Given a tag that we've identified as a media embed (because it has a
        data-embedtype="media" attribute), return a dict of the attributes we should
        have on the resulting <embed> element.
        """
        return {
            'url': tag['data-url'],
        }

    @staticmethod
    def expand_db_attributes(attrs, for_editor):
        """
        Given a dict of attributes from the <embed> tag, return the real HTML
        representation.
        """
        if for_editor:
            try:
                return format.embed_to_editor_html(attrs['url'])
            except EmbedException:
                # Could be replaced with a nice error message
                return ''
        else:
            return format.embed_to_frontend_html(attrs['url'])
