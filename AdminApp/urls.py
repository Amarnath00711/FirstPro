from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addgrocery',views.addgrocery,name='addgrocery'),
    path('firststep',views.firststep,name='firststep'),
    path('add_cat',views.add_cat,name='add_cat'),
    path('second_step',views.second_step,name='second_step'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('thirdstep',views.thirdstep,name='thirdstep'),
    path('add_mov',views.add_mov,name='add_mov'),
    path('fourth_step',views.fourth_step,name='fourth_step'),
    path('edition/<int:id>',views.edition,name='edition'),
    path('updation/<int:id>',views.updation,name='updation'),
    path('deletion/<int:id>',views.deletion,name='deletion'),
    path('regview',views.regview,name='regview'),
    path('contact_table',views.contact_table,name='contact_table'),
    path('contactview',views.contactview,name='contactview'),
    path('checkouttable',views.checkouttable,name='checkouttable')
]