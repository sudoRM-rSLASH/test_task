from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from accounts.models import User
from accounts.utils import Parser, DataValidator


@require_http_methods(["POST"])
@csrf_exempt
@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_new_users(request):
    with open("./accounts/downloads/csv_file.csv", "wb") as csv:
        csv.write(request.FILES.get("csv_file").read())
    parser = Parser(
        xml_file=request.FILES.get("xml_file"),
        csv_file=open("./accounts/downloads/csv_file.csv"),
    )
    users_list = DataValidator(
        parser.parse_csv(), parser.parse_xml()
    ).validate_user_info()
    User.objects.bulk_create(
        User.create_users_objects_from_list(users_list), ignore_conflicts=True
    )
    return redirect("get_main_page")


@require_http_methods(["POST", "GET"])
def signin(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return redirect("signin")
    return redirect("get_main_page")


@require_http_methods(["GET"])
def signout(request):
    logout(request)
    return redirect("signin")


@require_http_methods(["POST", "GET"])
@login_required
def get_main_page(request):
    return render(
        request,
        "main.html",
        context={
            "user_full_name": request.user.get_full_name(),
            "users": User.objects.exclude(is_superuser=True).all(),
        },
    )
