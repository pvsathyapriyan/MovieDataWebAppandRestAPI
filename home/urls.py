from django.urls import path
from .views import HomePageView, FilterPageView, EditPageView, DisplayPageView, ExportxlView


urlpatterns = [
	#this page has search bar and filter options
    path('', HomePageView.as_view(), name='home'), 

    #this page displays the search results
    path('filterpage/', FilterPageView.as_view(), name='filterresults'), 

    #this page lets us edit rows that are selected in the above page
    path('editrowspage/', EditPageView, name='editrows'), 

    #this page displays the rows after they are edited
    path('displayrows/', DisplayPageView, name='displayrows'), 

    #url for downloading the excel
    path('exportxl/', ExportxlView, name='exportxl'), 
]