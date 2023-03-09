from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post ,Comment,FreePost,FreeComment
from .models import musinsa_model
from .models import mixxo_model
from .models import spao_model

from .models import musinsa_rank
from .models import mixxo_rank
from .models import spao_rank

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)

admin.site.register(musinsa_model)
admin.site.register(mixxo_model)
admin.site.register(spao_model)

admin.site.register(musinsa_rank)
admin.site.register(mixxo_rank)
admin.site.register(spao_rank)