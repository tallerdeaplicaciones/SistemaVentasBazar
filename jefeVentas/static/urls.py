#Urls app tickets
from django.urls import path
from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('list/', TicketListView.as_view(), name='ticket_list'),
    path('detail/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('create/', TicketCreateView.as_view(), name='ticket_create'),
    path('update/<int:pk>/', TicketUpdateView.as_view(), name='ticket_update'),
    path('update/delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket_delete'),
]
