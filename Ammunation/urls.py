from django.urls import include, path
from .views import index, adminGuns, administrador, modificararma, deleteGuns, deleteUser, descriptionGuns, \
editarPerfil, forgetPassword, gatoRandom, msgVerificarEmail, register, editarusuario, userProfile, vistaCompras, vistaVender, \
vistaVentas, cerrar_sesion, add_to_cart, update_cart_item, remove_from_cart, carrito, process_payment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('adminGuns/', adminGuns, name='adminGuns'),
    path('administrador/', administrador, name='administrador'),
    path('carrito/', carrito, name='carrito'),
    path('add/<int:arma_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('process_payment/', process_payment, name='process_payment'),
    path('modificararma/<id>', modificararma, name='modificararma'),
    path('deleteGuns/<id>', deleteGuns, name='deleteGuns'),
    path('deleteUser/<id>', deleteUser, name='deleteUser'),
    path('descriptionGuns/<id>', descriptionGuns, name='descriptionGuns'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('forgetPassword/', forgetPassword, name='forgetPassword'),
    path('gatoRandom/', gatoRandom, name='gatoRandom'),
    path('msgVerificarEmail/', msgVerificarEmail, name='msgVerificarEmail'),
    path('register/', register, name='register'),
    path('editarusuario/<id>', editarusuario, name='editarusuario'),
    path('userProfile/', userProfile, name='userProfile'),
    path('vistaCompras/', vistaCompras, name='vistaCompras'),
    path('vistaVender/', vistaVender, name='vistaVender'),
    path('vistaVentas/', vistaVentas, name='vistaVentas'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)