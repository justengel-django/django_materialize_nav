from .utils import NavHeader, NavItem
from .search.nav_option_views import SearchOptions

from .navigation.views import TemplateMixin, TitleViewMetaclass, BaseNavOptions, TitleOptions, NavBarOptions, \
    SideBarOptions, BaseNavView

from .search.views import SearchNavView, SearchView


__all__ = ['TemplateMixin', 'NavHeader', 'NavItem', 'TitleViewMetaclass', 'BaseNavOptions', 'TitleOptions',
           'NavBarOptions', 'SideBarOptions', 'SearchOptions', 'BaseNavView',
           'SearchNavView', 'SearchView',
           'NavView']


class NavView(SearchNavView):
    pass
