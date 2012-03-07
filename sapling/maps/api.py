from tastypie import fields
from tastypie.resources import ALL

from models import MapData
import pages.api  # Scoped import to prevent ImportError.
from sapling.api import api, SlugifyMixin
from sapling.api.resources import GeoResource


class MapResource(SlugifyMixin, GeoResource):
    page = fields.ToOneField(pages.api.PageResource, 'page')

    class Meta:
        queryset = MapData.objects.all()
        resource_name = 'map'
        field_to_slugify = 'page'
        slug_lookup_field = 'page__slug'
        filtering = {
            'points': ALL,
            'lines': ALL,
            'polys': ALL,
            'geom': ALL,
            'length': ALL,
        }


api.register(MapResource())