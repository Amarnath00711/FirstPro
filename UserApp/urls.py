from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexuser,name='indexuser'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('viewgrocery',views.viewgrocery,name='viewgrocery'),
    path('singlecategory',views.singlecategory,name='singlecategory'),
    path('singlegrocery',views.singlegrocery,name='singlegrocery'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('loginusing',views.loginusing,name='loginusing'),
    path('userdata',views.userdata,name='userdata'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('category',views.category,name='category'),
    path('categories',views.categories,name='categories'),
    path('singleecategory/<int:id>',views.singleecategory,name='singleecategory'),
    path('contact',views.contact,name='contact'),
    path('contactfrom',views.contactfrom,name='contactfrom'),
    path('contactview',views.contactview,name='contactview'),
    path('editing/<int:id>',views.editing,name='editing'),
    path('updating',views.updating,name='updating'),
    path('deleting/<int:id>',views.deleting,name='deleting'),
    path('shooting/<int:id>',views.shooting,name='shooting'),
    path('cinema/<str:category>',views.cinema,name='cinema'),
    path('singlemovie/<int:id>',views.singlemovie,name='singlemovie'),
    path('about',views.about,name='about'),
    path('shopingcart',views.shopingcart,name='shopingcart'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('cartdata/<int:id>',views.cartdata,name='cartdata'),
    path('grocerystep',views.grocerystep,name='grocerystep'),
    path('add_gro',views.add_gro,name='add_gro'),
    path('gro_step',views.gro_step,name='gro_step'),
    # path('editt/<int:id>',views.editt,name='editt'),
    # path('updaate/<int:id>',views.updaate,name='updaate'),
    path('deletee/<int:id>',views.deletee,name='deletee'),
    path('thankspage',views.thankspage,name='thankspage'),
    path('checkoutinfo',views.checkoutinfo,name='checkoutinfo')
]