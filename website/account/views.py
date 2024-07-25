from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, DistrictOfficeForm, BranchLocationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import headoffice_required, districtoffice_required, branchlocation_required, role_required
from .models import DistrictOfficeList, BranchLocation

# Create your views here.
def index (request):
    return render(request, 'account/index.html')

def createadmin(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Admin created successfully.'
            return redirect('login_view')  # Redirect to login page after successful registration
        else:
            msg = 'Form is not valid. Please correct the errors.'
    else:
        form = SignUpForm()
        
    return render(request, 'account/createadmin.html', {'form': form, 'msg': msg})


def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)
    if request.method == "POST":  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_headoffice:
                login(request, user)
                return redirect('dashboardHO')
            elif user is not None and user.is_districtoffice:
                login(request, user)
                return redirect('dashboardDO')
            elif user is not None and user.is_branchlocation:
                login(request, user)
                return redirect('branchlocation')
            else:
                msg = 'invalid credentials'
        else: 
            msg = 'error validating form'
    return render(request, 'account/login_view.html', {"form": form, "msg": msg})

@login_required
def dashboardDO(request):
        return render(request, 'account/dashboardDO.html')
    
@login_required
def dashboardHO(request):
        return render(request, 'account/dashboardHO.html')

@login_required
# @headoffice_required
@role_required('is_headoffice')
def headoffice(request):
    return render(request, 'account/headoffice.html')

@login_required
# @districtoffice_required
@role_required('is_headoffice', 'is_districtoffice')
def districtoffice(request):
    district_offices = DistrictOfficeList.objects.all()
    context = {'district_offices': district_offices}
    return render(request, 'account/districtoffice.html', context)

@login_required
# @branchlocation_required
@role_required('is_headoffice', 'is_districtoffice', 'is_branchlocation')
def branchlocation(request):
    # Fetch all DistrictOfficeList entries
    district_offices = DistrictOfficeList.objects.all()
    # Create a dictionary to hold branch locations by district office
    branch_locations_by_district = {}

    for district in district_offices:
        # Fetch branch locations for each district office
        branch_locations = BranchLocation.objects.filter(districtofficelist=district)
        branch_locations_by_district[district] = branch_locations

    context = {'branch_locations_by_district': branch_locations_by_district}
    return render(request, 'account/branchlocation.html', context)

def addlocation(request):
    return render(request, 'account/addlocation.html')

def createuser(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created successfully.'
            return redirect('login_view')  # Redirect to login page after successful registration
        else:
            msg = 'Form is not valid. Please correct the errors.'
    else:
        form = SignUpForm()
        
    return render(request, 'account/createuser.html', {'form': form, 'msg': msg})

def addlocation(request):
    if request.method == "POST":
        if 'add_district' in request.POST:
            district_form = DistrictOfficeForm(request.POST)
            if district_form.is_valid():
                district_form.save()
                return redirect('addlocation')
        elif 'add_branch' in request.POST:
            branch_form = BranchLocationForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                return redirect('addlocation')
    else:
        district_form = DistrictOfficeForm()
        branch_form = BranchLocationForm()
        
    return render(request, 'account/addlocation.html', {
        'district_form': district_form,
        'branch_form': branch_form,
        'District_offices': DistrictOfficeList.objects.all()
    })