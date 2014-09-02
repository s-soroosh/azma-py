__author__ = 'mahdi'
from django.forms.widgets import Textarea
from azma.settings import DEBUG


# changing directory for debug mode and product mode
if DEBUG:
    d = 'ckeditor_d'
else:
    d = 'ckeditor_p'


class CKeditorWidgetBase(Textarea):
    class Media:
        def __init__(self):
            pass

        css = {
            'all': (d + '/contents.css',)
        }
        js = (
            d + '/highlight.min.js',
            d + '/ckeditor.js',  # Ckeditor core script .
            d + '/styles.js',  # Ckeditor styling script .
            d + '/run.js',

        )


class ArticleWidget(CKeditorWidgetBase):
    class Media:
        def __init__(self):
            pass

        js = (
            d + '/ArticleConfig/build-config.js',  # Article Editor Preconfigurations
            d + '/ArticleConfig/config.js',  # Article Editor Main Configurations
        )


class CommentWidget(CKeditorWidgetBase):
    class Media:
        def __init__(self):
            pass

        js = (
            d + '/CommentConfig/build-config.js',  # Article Editor Preconfigurations
            d + '/CommentConfig/config.js',  # Article Editor Main Configurations
        )