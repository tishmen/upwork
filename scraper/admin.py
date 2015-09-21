from django.contrib import admin, messages

from scraper.models import Account, Scraper, Freelancer, Job, Inviter
from scraper.tasks import scrape_task, invite_task


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    pass


@admin.register(Scraper)
class ScraperAdmin(admin.ModelAdmin):

    list_display = ('name', 'last_run', 'success')
    actions = ('scrape', )

    def scrape(self, request, queryset):
        count = queryset.count()
        for scraper in queryset:
            scrape_task.delay(scraper)
        if count == 1:
            message_bit = '1 scraper'
        else:
            message_bit = '{} scrapers'.format(count)
        self.message_user(
            request, 'Delayed scrape_task for {}'.format(message_bit),
            level=messages.SUCCESS
        )

    scrape.short_description = 'Run selected scrapers'


class JobInline(admin.StackedInline):

    model = Job
    extra = 0


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'title', 'location', 'hourly_rate', 'rating', 'job_success',
        'hours_worked', 'job_count'
    )
    list_filter = ('scraper', )
    actions = ('invite', )
    search_fields = ('name', 'title', 'location')
    inlines = (JobInline, )

    def invite(self, request, queryset):
        inviter = Inviter.objects.get(active=True)
        count = queryset.count()
        invite_task.delay(queryset, inviter)
        if count == 1:
            message_bit = '1 freelancer'
        else:
            message_bit = '{} freelancers'.format(count)
        self.message_user(
            request, 'Delayed invite_task for {}'.format(message_bit),
            level=messages.SUCCESS
        )

    invite.short_description = 'Run selected inviters'


@admin.register(Inviter)
class InviterAdmin(admin.ModelAdmin):

    list_display = ('name', 'active', 'last_run', 'success')
