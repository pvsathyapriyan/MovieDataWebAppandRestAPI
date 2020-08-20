from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Movies, Category


#Receives the idlist and newrating and updates the Movies table
def EditRows(id_list,newrating_list):
	n = 0
	for i in id_list:
		Movies.objects.filter(id=int(i)).update(rating=newrating_list[n])
		n = n+1

#This function will provide us with the ID of the category that the user chose in the home screen
def matchForeignKey(query):
		if query == 'None':
			return 'None'
		value = Category.objects.get(category=query)
		categoryid = value.id
		return categoryid

#View for Home page with Category Model as it is needed for the list of categories for filter dropdown
class HomePageView(ListView):
	model = Category
	template_name = 'home.html'
	def get_queryset(self):
		object_list = Category.objects.all()
		return object_list

#View for page that appears after searching/filtering
class FilterPageView(ListView):
	model = Movies
	template_name = 'filter.html'

	def get_queryset(self):
		#receives 3 values from home.html template which is then used to provide the correct search results
		query1 = self.request.GET.get("filtercategory")
		query2 = self.request.GET.get("filterrating")
		query = self.request.GET.get("searchterm")
		categoryid = matchForeignKey(query1)

		#logic for choosing the search results
		if query1 != 'None' and query2 != 'None' and query != 'None':
			object_list = Movies.objects.filter(category=categoryid, rating=query2, moviename__icontains=query)
		if query1 == 'None' and query2 != 'None' and query != 'None':
			object_list = Movies.objects.filter(rating=query2, moviename__icontains=query)
		if query1 != 'None' and query2 == 'None' and query != 'None':
			object_list = Movies.objects.filter(category=categoryid, moviename__icontains=query)
		if query1 != 'None' and query2 != 'None' and query == 'None':
			object_list = Movies.objects.filter(category=categoryid, rating=query2)
		if query1 == 'None' and query2 != 'None' and query == 'None':
			object_list = Movies.objects.filter(rating=query2)
		if query1 != 'None' and query2 == 'None' and query == 'None':
			object_list = Movies.objects.filter(category=categoryid)
		if query1 == 'None' and query2 == 'None' and query == 'None':
			object_list = Movies.objects.all()
		if query1 == 'None' and query2 == 'None' and query != 'None':
			object_list = Movies.objects.filter(moviename__icontains=query)
		return object_list


#view for the page that will allow users to edit the search results
#receives the list of ids of the rows that user clicks. 
def EditPageView(request):
	if request.method == 'POST':
		id_list = request.POST.getlist('editvalue')
		rows = []
		if not id_list:
			return render(request, 'None.html')
		else:
		#rows are extracted wrt the id_list received and converted to a list of dicts.
			for i in id_list:
				temp_query_set = (Movies.objects.filter(id=i))
				rows.append(temp_query_set.values()[0])
			context = {'rows' : rows}
			return render(request, 'editpage.html', context)


#IDs of the selected rows and New Rating Value is passed to a EditRows function for updating Movies Table
def DisplayPageView(request):
	if request.method == 'POST':
		id_list = request.POST.getlist('movieid')
		newrating_list = request.POST.getlist('newrating')
		EditRows(id_list,newrating_list)
		#logic to return only the rows that are updated
		rows = []
		for i in id_list:
			temp_query_set = (Movies.objects.filter(id=i))
			rows.append(temp_query_set.values()[0])
		context = {'rows' : rows}
		return render(request, 'displayrows.html', context)


#view for exporting the searched/filtered results to excel
def ExportxlView(request):

	import xlwt

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="Movies.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	#Two sheets are created one for Movies Table, another for Category Table
	ws = wb.add_sheet('Movies')
	ws2 = wb.add_sheet('Category')

	#Movies Table
    #Adding header to the sheet's first row 
	row_num = 0
	columns = ['Id', 'Movie Name', 'Rating', 'CategoryId' ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num])

    
	#Adding data from the table. Values are added according to the id_list received from template
	if request.method == 'POST':
		id_list = request.POST.getlist('editvalue')
		rows = []
		for i in id_list:
			temp_query_set = (Movies.objects.filter(id=i))
			rows.append(temp_query_set.values()[0])
		for row in rows:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, list(row.values())[col_num])
	
	#Category Table
	#Adding header to the sheet's first row 
	row_num = 0
	columns = ['Id', 'CategoryName' ]

	for col_num in range(len(columns)):
		ws2.write(row_num, col_num, columns[col_num])


	#Logic to add the Category Table value to Sheet 2
	rows = Category.objects.all().values_list('id','category')

	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws2.write(row_num, col_num, row[col_num])


	wb.save(response)
	return response