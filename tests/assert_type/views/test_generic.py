from django.db import models
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from typing_extensions import assert_type


class MyModel(models.Model): ...


class MyDetailView(SingleObjectMixin[MyModel]): ...


detail_view = MyDetailView()
assert_type(detail_view.model, type[MyModel])
assert_type(detail_view.queryset, models.QuerySet[MyModel, MyModel] | None)
assert_type(detail_view.get_context_object_name(MyModel()), str)
assert_type(detail_view.get_context_object_name(1), str | None)


class MyListView(ListView[MyModel]): ...


list_view = MyListView()
assert_type(list_view.model, type[MyModel] | None)
assert_type(list_view.queryset, models.QuerySet[MyModel, MyModel] | None)
assert_type(list_view.get_context_object_name(models.QuerySet[MyModel]()), str)
assert_type(list_view.get_context_object_name(MyModel()), str | None)
assert_type(list_view.get_context_object_name(1), str | None)
