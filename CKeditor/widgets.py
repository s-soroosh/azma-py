__author__ = 'mahdi'
from django.forms.widgets import Textarea


class CKeditorWidgetBase(Textarea):
    class Media:
        def __init__(self):
            pass

        css = {
            'all': ('ckeditor/contents.css',)
        }
        js = (
            'ckeditor/highlight.min.js',
            'ckeditor/ckeditor.js',  # Ckeditor core script .
            'ckeditor/styles.js',  # Ckeditor styling script .
            'ckeditor/run.js',

        )


class ArticleWidget(CKeditorWidgetBase):
    class Media:
        def __init__(self):
            pass

        js = (
            'ckeditor/ArticleConfig/build-config.js',  # Article Editor Preconfigurations
            'ckeditor/ArticleConfig/config.js',  # Article Editor Main Configurations
        )


class CommentWidget(CKeditorWidgetBase):
    class Media:
        def __init__(self):
            pass

        js = (
            'ckeditor/CommentConfig/build-config.js',  # Article Editor Preconfigurations
            'ckeditor/CommentConfig/config.js',  # Article Editor Main Configurations
        )