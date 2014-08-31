__author__ = 'mahdi'
from django.forms.models import ModelForm
from tutorial.models import Tutorial
from django.utils.text import ugettext_lazy as _
from CKeditor.widgets import ArticleWidget


class TutorialForm(ModelForm):



    class Meta:
        model = Tutorial
        fields = ("category", "keyword", "abstract", "name", "local_name", "author", "content", "registered_date")
        labels = {
            "Category": _("Tutorial Category"),
            "keyword": _("Tutorial Keywords"),
            "abstract": _("Tutorial Abstract"),
            "name": _("Tutorial Name"),
            "local_name": _("Tutorial Local Name"),
            "content": _("Tutorial Content"),
            "author": _("Tutorial Author"),
            "registered_date": _("Tutorial Submit Date"),
        }
        help_texts = {
            "Category": _("Which Category this tutorial belongs to ?"),
            "keyword": _("Describe this tutorial contents with keywords , no more than 75 characters"),
            "abstract": _("a Breif of this tutorial"),
            "name": _("a name which will be used for accessing this tutorial via url"),
            "local_name": _("a friendly name for identifing the tutorial"),
            "content": _("tutorial content "),
            "author": _("the author who writes this tutorial , perhaps you"),
            "registered_date": _("tutorial publish date"),
        }

        widgets = {
            # "Category": ,
            #"keyword": ,
            "abstract": ArticleWidget(),
            #"name": ,
            #"local_name":,
            "content": ArticleWidget(),
            #"author": ,
            #"registered_date": ,
        }

        # error_messages = {
        # "Category": {
        #
        #     },
        #     "keyword": {
        #
        #     },
        #     "abstract": {
        #
        #     },
        #     "name": {
        #
        #     },
        #     "local_name": {
        #
        #     },
        #     "content": {
        #
        #     },
        #     "author": {
        #
        #     },
        #     "registered_date": {
        #
        #     },
        # }
        #