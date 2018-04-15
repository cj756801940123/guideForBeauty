"""guideForBeauty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from beauty import views
from beauty.lcj.handler import mapping_handler
from beauty.hmy.handler import get_similar_products
from beauty.hmy.handler import login
from beauty.hmy.handler import register
from beauty.zmh.handler import get_cut_price_products


urlpatterns = [
    # url(r'show_student$', views.show_student, ),
    # url(r'add_student$', views.show_student, ),
    # url(r'show_baseMakeup$', views.show_baseMakeup, ),  # 这个估计可以删掉
    # url(r'show_list$', views.show_list, ),
    # url(r'show_search_list$', views.show_search_list, ),

    #  cj 接口路由
    url(r'productsList/getProductsPage', mapping_handler.handle_search),

    #hmy接口路由
    #相似商品
    url(r'productsList/getAllSimilarProducts',get_similar_products.handle_search),
    #注册
    url(r'user/register',register.handle_register),
    #登录
    url(r'user/login',login.handle_login),

    # zmh接口路由
    url(r'cut_price/get_products',get_cut_price_products.handle_search),



]
