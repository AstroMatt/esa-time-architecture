from django.contrib import admin
from time_architecture.light.models import LED


@admin.register(LED)
class LEDAdmin(admin.ModelAdmin):
    list_display = ['title', 'hour_00', 'hour_01', 'hour_02', 'hour_03', 'hour_04', 'hour_05', 'hour_06', 'hour_07', 'hour_08', 'hour_09', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15', 'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23']
    list_filter = ['box', 'name']
    #search_fields = ['^name']
    readonly_fields = ['box', 'name']
    ordering = ['box', 'name']
    change_list_filter_template = 'admin/filter_listing.html'



    def title(self, obj):
        return obj.__str__().replace(' ', '&nbsp;')

    title.allow_tags = True

    class Media:
        css = {'all': ['light/css/hide-actions.css']}
