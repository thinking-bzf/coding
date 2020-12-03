import os

import pandas as pd
import xlrd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import (FileResponse, Http404, HttpResponse,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import time
from .forms import FirstZYform, OriginalForm
from .models import original_file, FirstZY, Today_CleanedFile, Today_MergedFile
from openpyxl import load_workbook
from . import deal
# from django.utils.timezone import now
from dateutil.parser import parse

# Create your views here.

# 获取文件目录中所有文件名

# 寻找当前目录的所有文件


def file_files(file_path):
    List = []
    for root, dirs, files in os.walk(file_path):
        if len(files) != 0:
            List += files
    return List

# 网站主页


def index(request):
    return render(request, 'index.html')

# @login_required

# 志愿指数处理


def FirstZY_deal(request):
    if request.method != 'POST':
        form = FirstZYform()
    else:
        form = FirstZYform(request.POST, request.FILES)
        if form.is_valid():
            # 获取文件对象
            file = request.FILES.get('File')
            # 配合上传文件的名字
            file_name = str(file).split(
                '.')[0] + time.strftime("%Y%m%d%H%M%S") + '.xlsx'
            # 将文件表单上传到数据库
            new_file = form.save(commit=False)
            new_file.save()
            # 志愿指数的计算
            df = pd.read_excel(request.FILES.get('File'), 't_tddxx')
            result = deal.deal_FirstZY(df)
            # 得到的结果输出到指定目录
            result.to_excel(os.path.join(
                'File/FirstZY/result/', 'result_' + file_name))
            # 处理成功后返回弹窗信息
            messages = '数据处理成功'
            # 上传完一个表单后 返回一个空表单
            form = FirstZYform()
            # 得到所有
            Files = FirstZY.objects.order_by('date_added')
            context = {'messages': messages,
                       'form': form, 'file_name': file_name, 'Files': Files}
            return render(request, 'FirstZY/FirstZY.html', context)
    Files = FirstZY.objects.order_by('date_added')
    context = {'form': form, 'Files': Files}
    return render(request, 'FirstZY/FirstZY.html', context)

# 志愿指数下载


def FirstZY_dl(request, file_name):
    file = open(os.path.join(
        'File/FirstZY/result', 'result_'+str(file_name)).split('.')[0]+'.xlsx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    file_name = 'attachment;filename ="result_' + \
        str(file_name).split('.')[0]+'.xlsx'
    response['Content-Disposition'] = file_name.encode('utf-8', 'ISO-8859-1')
    return response


# 上传源文件
def original(request):
    if request.method != 'POST':
        form = OriginalForm()
    else:
        # 得到表单上传文件
        form = OriginalForm(request.POST, request.FILES)
        if form.is_valid():

            # 将上传文件存入数据库
            new_file = form.save(commit=False)
            new_file.save()
            # 获取对文件的命名
            syd = request.POST.get('syd_name')+' '
            pc = request.POST.get('pc_name')+' '
            kl = request.POST.get('kl_name')
            # 获取文件
            file = request.FILES.get('File')
            # 将文件重命名 并存放在指定文件夹
            dic_name = syd + pc + kl
            file_name = syd + pc + kl + '.xlsx'
            upload_path = os.path.join('File/original/renamed/',
                                       time.strftime("%Y"), time.strftime("%m%d"))
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            with open(os.path.join("File/original/renamed/", time.strftime("%Y"), time.strftime("%m%d"), "%s" % file_name), 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            # 将tddxx和TDD变成一张表
            writer = pd.ExcelWriter(os.path.join(
                upload_path, file_name), engine="xlsxwriter")
            # 读取表格对象
            rb = xlrd.open_workbook(os.path.join(
                upload_path, file_name), formatting_info=True)
            # 将TDD中的工作表加到writer对象中
            for x in rb.sheet_names():
                sheet = pd.read_excel(rb, sheet_name=x, dtype=object)
                sheet.to_excel(writer, sheet_name=x, startcol=0, index=False)
            # 将tddxx添加到writer中
            t_tddxx = request.FILES.get('t_tddxx')
            tddxx = pd.read_excel(request.FILES.get(
                't_tddxx'), 't_tddxx', dtype=object)
            tddxx.to_excel(writer, sheet_name='t_tddxx',
                           startcol=0, index=False)
            # 保存writer对象
            writer.save()

            messages = '数据上传成功'
            form = OriginalForm()
            context = {'messages': messages, 'form': form}
            return render(request, 'Total/original_upload.html', context)
    context = {'form': form}
    return render(request, 'Total/original_upload.html', context)

# 显示源文件的主页


def original_index(request):
    Files = original_file.objects.order_by('date_added')
    date_list = []
    files = {}
    for x in Files:
        date_list.append(x.date_added.strftime("%Y-%m-%d"))
    for x in date_list:
        # 判断分省清洗情况
        flag = 1
        filter_files = original_file.objects.filter(
            date_added__year=x[:4], date_added__month=x[5:7], date_added__day=x[8:])
        for i in filter_files:
            if i.clean_message != '数据已清洗':
                flag = 0
                break
        TotalFlag = 1
        # 判断今日是否全部完成
        TodayCleanFile = Today_CleanedFile.objects.filter(Date=x)
        TotalMessage = ''
        if not any(TodayCleanFile):
            if flag:
                TotalMessage = '分省已完成,可汇总'
            else:
                TotalMessage = '请先完成所有分省清洗'
        else:
            for File in TodayCleanFile:
                TotalMessage = File.message
        files[x] = [filter_files, flag, TodayCleanFile, TotalMessage]
    s = '录取汇总'
    context = {'files': files, 's': s}
    return render(request, 'Total/original_index.html', context)

# 源文件下载


def original_dl(request, year, date_time, file_name):
    file = open(os.path.join(
        'File/original/renamed', year, date_time, file_name+'.xlsx'), 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    file_name = 'attachment;filename ="'+file_name+'.xlsx"'
    response['Content-Disposition'] = file_name.encode('utf-8', 'ISO-8859-1')
    return response

# 分省数据清洗下载


def Data_CleanDL(request, year, date_time, file_name, s):
    file = open(os.path.join(
        'File/data_clean', year, 'part', date_time, file_name + s + '.xlsx'), 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    file_name = 'attachment;filename ="' + file_name + s + '.xlsx"'
    response['Content-Disposition'] = file_name.encode('utf-8', 'ISO-8859-1')
    return response

# 分省数据清洗


def data_clean(request, year, date_time, file_name, file_id):
    result_path = os.path.join(r'File\data_clean', year, 'part', date_time)
    original_path = os.path.join(
        'File/original/renamed', year, date_time)
    File = original_file.objects.get(id=file_id)
    try:
        deal.data_clean(result_path, file_name, original_path)
        File.cleaned_FilePath = os.path.join(
            r'File\data_clean', year, 'part', date_time)
        File.save()
    except FileNotFoundError:
        File.clean_message = '清洗错误,请正确上传源文件'
        File.save()
    else:
        File.clean_message = '数据已清洗'
        File.save()
    # return render(request, 'Total/original_index.html', context)
    return redirect(reverse('data_deal:original_index'))

# 当日上传数据清洗


def Today_clean(request, date):
    dateList = date.split('-')
    year = dateList[0]
    month = dateList[1]
    day = dateList[2]
    path = os.path.join(
        r'File\data_clean', year, 'Total')
    try:
        result = deal.clean_concat(os.path.join(
            r'File\data_clean', year, 'part', month + day))
        if not os.path.exists(path):
            os.makedirs(path)
        result.to_excel(os.path.join(
            r'File\data_clean', year, 'Total', month + day + '分省汇总.xlsx'))
    except FileNotFoundError:
        TodayCleanFile = Today_CleanedFile(message='清洗错误.请重新分省清洗')
        TodayCleanFile.save()
    else:
        TodayCleanFile = Today_CleanedFile(
            name=month + day + '清洗汇总.xlsx', Path=path, Date=date, message='当日清洗完成')
        TodayCleanFile.save()
    return redirect(reverse('data_deal:original_index'))

# 当日清洗下载


def Today_cleanDL(request, date):
    dateList = date.split('-')
    year = dateList[0]
    month = dateList[1]
    day = dateList[2]
    file = open(os.path.join(
        'File/data_clean/', year, 'Total', month + day + '分省汇总.xlsx'), 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    file_name = 'attachment;filename ="' + month + day + '分省汇总.xlsx"'
    response['Content-Disposition'] = file_name.encode('utf-8', 'ISO-8859-1')
    return response

# 当日拼接主页


def OriginalMerge_index(request):
    Files = original_file.objects.order_by('date_added')
    date_list = []
    files = {}
    for x in Files:
        date_list.append(x.date_added.strftime("%Y-%m-%d"))
    for x in date_list:
        # 判断分省清洗情况
        flag = 1
        filter_files = original_file.objects.filter(
            date_added__year=x[:4], date_added__month=x[5:7], date_added__day=x[8:])
        for i in filter_files:
            if i.clean_message != '数据已清洗':
                flag = 0
                break
        TotalFlag = 1
        # 判断今日是否全部完成
        TodayMergedFile = Today_MergedFile.objects.filter(Date=x)
        TotalMessage = ''
        if not any(TodayMergedFile):
            if flag:
                TotalMessage = '分省已完成,可汇总'
            else:
                TotalMessage = '请先完成所有分省清洗'
        else:
            for File in TodayMergedFile:
                TotalMessage = File.message
        files[x] = [filter_files, flag, TodayMergedFile, TotalMessage]
    s = '录取汇总'
    context = {'files': files, 's': s}
    return render(request, 'Total/original_merge.html', context)

# 对当日上传的源文件拼接处理


def Today_Merge(request, date):
    datelist = date.split('-')
    year = datelist[0]
    month = datelist[1]
    day = datelist[2]
    Original_Path = os.path.join(r'File\original\renamed', year, month + day)
    Result_Path = os.path.join(
        'File\OriginalMerge', year, month + day)
    if not os.path.exists(Result_Path):
        os.makedirs(Result_Path)
    try:
        result = deal.original_merge(Original_Path)
        result.to_excel(os.path.join(Result_Path,  month +
                                     day + 'MerageResult.xlsx'), index=False)
    except FileNotFoundError:
        OriginalMergeFile = Today_MergedFile(message='拼接错误,请正确上传源文件')
        OriginalMergeFile.save()
    else:
        OriginalMergeFile = Today_MergedFile(
            name=month + day + 'MerageResult.xlsx', Path=Result_Path, Date=date, message='当日总表拼接完成')
        OriginalMergeFile.save()
    return redirect(reverse('data_deal:OriginalMerge_index'))
