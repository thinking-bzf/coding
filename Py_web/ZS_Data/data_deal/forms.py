from django import forms
from .models import FirstZY, original_file


class FirstZYform(forms.ModelForm):
    class Meta:
        model = FirstZY
        fields = ['File']
        labels = {'File': '上传文件'}


class OriginalForm(forms.ModelForm):
    pc_name = forms.ChoiceField(choices=[(
        '本科第一批', '本科第一批'), ('普通提前批', '普通提前批'), ('国家专项', '国家专项'), ('地方专项', '地方专项')], label='批次')
    kl_name = forms.ChoiceField(
        choices=[('理工类', '理工类'), ('文史类', '文史类'), ('艺术类', '艺术类'), ('综合改革', '综合改革')], label='科类')
    class Meta:
        model = original_file
        fields = ['File', 'syd_name','pc_name','kl_name','t_tddxx']
        labels = {'File': '上传文件', 'syd_name': '生源地','t_tddxx':'上传t_tddxx'}
