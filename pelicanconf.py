#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gustavo Furtado de Oliveira Alves'
SITENAME = u'Minicurso de Lógica de Programação'
SITEURL = 'http://localhost:9000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly'
    }
}

# Theme
THEME = 'theme'
COURSE_DESCRIPTION = """Minicurso 100% GRÁTIS de Lógica de Programação.
São 10 aulas super explicadas com a melhor didática para ensinar programação do ZERO para qualquer pessoa!
Agora aprender programação está acessível a qualquer um!"""
COURSE_AUTHOR = "Gustavo"
LP_LINK = SITEURL
OG_IMAGE = "/images/gustavo-furtado.jpg"
LP_IMAGE = "/images/Logo.png"
LP_TITLE = "Quer aprender lógica de programação GRÁTIS?"
LP_DESCRIPTION = "Coloque seu e-mail abaixo e receba GRATUITAMENTE o minicurso de lógica de programação."
LP_ACTION = "http://mail.gustavofurtado.com.br/subscribe"
LP_HIDDEN_FIELDS = '<input type="hidden" name="list" value="oiJK0j8gmAdoxtJtv2pSxA" />'
TITLEBAR_TEXT = "Receba este minicurso de lógica de programação GRÁTIS!"
TOTAL_LESSONS = 10
SHARE_ON_TWITTER = "http://ctt.ec/4Rq9f"
SHARE_ON_FACEBOOK = "http://www.facebook.com/sharer.php?u=http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/"
SHARE_ON_GPLUS = "https://plus.google.com/share?url=http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/"
SHARE_ON_LINKEDIN = "https://www.linkedin.com/cws/share?url=http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/"
FOOTER_PSS = """
<p>Aqui você encontrará conteúdo simples, práticos e que vai te ensinar os conceitos básicos por trás da programação,
ao final será capaz de criar pequenos programas e estará pronto para aprender qualquer linguagem de programação sem dificuldades.</p>
"""
