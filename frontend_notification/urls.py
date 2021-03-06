from django.conf.urls import patterns, include


urlpatterns = patterns('frontend_notification.views',
    # User notification for Customer UI
    (r'^user_notification/', 'notification_list'),
    (r'^user_notification/', include('notifications.urls')),
    (r'^notification_del_read/(.+)/$', 'notification_del_read'),
    # Notification Status (read/unread) for customer UI
    (r'^update_notification/(\d*)/$', 'update_notification'),
)
