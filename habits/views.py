from habits.paginators import PagePagination
from habits.permissions import IsOwner
from habits.serializers import GoodHabitSerializer, NiceHabitSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from habits.serializers import HabitSerializer
from habits.models import GoodHabit, NiceHabit


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        habit_data = self.request.data
        if 'is_nice' in habit_data and habit_data['is_nice']:
            return NiceHabitSerializer
        else:
            return GoodHabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
    pagination_class = PagePagination

    def get_queryset(self):
        return GoodHabit.objects.filter(owner=self.request.user) | NiceHabit.objects.filter(owner=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PagePagination

    def get_queryset(self):
        return GoodHabit.objects.filter(is_public=True) | NiceHabit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return GoodHabit.objects.filter(owner=self.request.user) | NiceHabit.objects.filter(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return GoodHabit.objects.filter(owner=self.request.user) | NiceHabit.objects.filter(owner=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner]

    def get_queryset(self):
        return GoodHabit.objects.filter(owner=self.request.user) | NiceHabit.objects.filter(owner=self.request.user)
