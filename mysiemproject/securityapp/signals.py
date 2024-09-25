from django.contrib.auth.signals import user_login_failed
import logging

logger = logging.getLogger('security')

def log_failed_login(sender, credentials, **kwargs):
    logger.warning(f"Failed login attempt with username: {credentials.get('username')}")

user_login_failed.connect(log_failed_login)
