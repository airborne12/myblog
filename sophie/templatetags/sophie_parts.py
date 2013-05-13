from django import template
from django.core.urlresolvers import reverse

from sophie.utils import multiblog_enabled

register = template.Library()

@register.inclusion_tag('sophie/templatetags/lists_category_of.tag')
def sophie_lists_category_of(blog):
    return {'category_list': blog.get_categories()}

@register.inclusion_tag('sophie/templatetags/shows_feed_of.tag')
def sophie_shows_feed_of(blog):
    return { 'blog': blog }

@register.inclusion_tag('sophie/templatetags/shows_about.tag')
def sophie_shows_about(blog):
    return { 'blog': blog }


@register.inclusion_tag('sophie/templatetags/links_siblings_of.tag')
def sophie_links_siblings_of(page, blog, urlname, part_slug=None):
    # conditional operatior hack xx and yy or zz == xx ? yy : zz
    url_bits = multiblog_enabled and { 'blog_slug': blog.slug } or {}

    # urls are named following this convention:
    #   sophie_[part name]_[page type]_url
    # which is taken advantage of here:
    urlparts = urlname.split('_')
    # if the type is 'details', then its url contains a slug of the part
    if urlparts[2] == 'details':
        # django.core.urlresolvers.reverse() does not accept unicode keywords
        # which is why this part needs encoding
        url_bits[('%s_slug' % urlparts[1]).encode('utf8')] = part_slug

    # Note that previous_page_number() is dumb, it returns the number
    # regardless of whether that page exists, same with next_page_number.
    # So, this needs to be guarded in the template
    url_bits['page_num'] = page.previous_page_number()
    previous_link = reverse( urlname, kwargs=url_bits )

    url_bits['page_num'] = page.next_page_number()
    next_link = reverse( urlname, kwargs=url_bits )
    
    return {
        'previous_link': previous_link,
        'next_link': next_link,
        'page': page,
    }

@register.inclusion_tag('sophie/templatetags/lists_entries_in.tag')
def sophie_lists_entries_in(entries, blog, empty_msg = ''):
    return {
        'entries': entries,
        'blog': blog,
        'empty_msg': empty_msg,
    }

