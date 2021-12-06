from rest_framework.decorators import action
from rest_framework.response import Response


class DetailedViewSetMixin:
    manager_method_prefix = "action_"
    serializer_action_classes = {}

    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(DetailedViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            queryset = getattr(
                queryset, f"{self.manager_method_prefix}{self.action}"
            )().all()
        except (AttributeError,):
            pass
        return queryset

    @action(detail=False)
    def detailed_list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        kwargs.update({"many": True, "context": {"request": self.request}})
        if page is not None:
            serializer = self.get_serializer_class()(page, **kwargs)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer_class()(queryset, **kwargs)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def detailed(self, *args, **kwargs):
        instance = self.get_object()
        kwargs.pop("pk")
        kwargs.update({"context": {"request": self.request}})
        serializer = self.get_serializer_class()(instance, **kwargs)
        return Response(serializer.data)
