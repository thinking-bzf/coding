from django.db import models

# Create your models here.


class FirstZY(models.Model):
    File = models.FileField(upload_to='File/FirstZY/original/')
    Dealed_File = models.FilePathField(path='File/FirstZY/result')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.File.name.split('/')[-1]

# class FirstZY_result(models.Model):
#     File=models.


class original_file(models.Model):
    File = models.FileField(upload_to='File/original/TDD')
    t_tddxx = models.FileField(upload_to='File/original/t_tddxx')
    Rename_FilePath = models.CharField(max_length=50)
    syd_name = models.CharField(max_length=50)
    pc_name = models.CharField(max_length=50)
    kl_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    clean_message = models.CharField(max_length=50, default='数据未清洗')

    def __str__(self):
        return self.syd_name+' '+self.pc_name+' '+self.kl_name


class Today_CleanedFile(models.Model):
    name = models.CharField(max_length=100, default='数据清洗汇总')
    Path = models.CharField(max_length=100, default='')
    Date = models.CharField(max_length=20)
    message = models.CharField(max_length=50, default='请先完成所有分省清洗')

    def __str__(self):
        return self.name


class Today_MergedFile(models.Model):
    name = models.CharField(max_length=100, default='当日数据拼接')
    Path = models.CharField(max_length=100, default='')
    Date = models.CharField(max_length=20)
    message = models.CharField(max_length=50, default='请正确上传源文件')

    def __str__(self):
        return self.name

