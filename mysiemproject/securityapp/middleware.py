from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger('security')

class SecurityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if self.is_suspicious_request(request):
            logger.warning(f"Suspicious activity detected from IP: {request.META['REMOTE_ADDR']}")
            # Handle suspicious request, e.g., block it, throttle, etc.

    def is_suspicious_request(self, request):
        # Example logic to detect anomalies
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if 'sqlmap' in user_agent:  # Simplified anomaly detection example
            return True
        return False
