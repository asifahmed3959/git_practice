class ChildrenModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ChildSerializer
    lookup_field = 'child_id'

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        self._parent = Parent.objects.filter(id=self.kwargs.get('parent_id', None)).first()

        if self._parent is None:
            raise Http404

    def get_object(self):
        obj = self.get_queryset().filter(id=self.kwargs.get('child_id')).first()

        if obj is None:
            raise Http404

        return obj

    def get_queryset(self):
        return Child.objects.filter(parent_id=self.kwargs.get('parent_id'))

    def perform_create(self, serializer):
        serializer.save(parent=self._parent)