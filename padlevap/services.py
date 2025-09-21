
from twilio.rest import Client
from django.conf import settings
from django.utils import timezone
from .models import PhoneOTP
import logging

logger = logging.getLogger(__name__)

class PhoneOTPService:
    @staticmethod
    def send_otp(phone_number):
        """Send OTP to phone number - SIMPLIFIED VERSION"""
        try:
            print(f"Service: Starting send_otp for {phone_number}")
            
            # Step 1: Invalidate previous OTPs
            try:
                invalidated = PhoneOTP.objects.filter(
                    phone_number=phone_number,
                    is_verified=False
                ).update(is_verified=True)
                print(f"Service: Invalidated {invalidated} previous OTPs")
            except Exception as e:
                print(f"Service: Error invalidating OTPs: {e}")
                raise
            
            # Step 2: Create new OTP
            try:
                otp_instance = PhoneOTP.objects.create(phone_number=phone_number)
                print(f"Service: Created new OTP: {otp_instance.otp_code}")
            except Exception as e:
                print(f"Service: Error creating OTP: {e}")
                raise
            
            # Step 3: Try to send SMS (simplified)
            try:
                sms_success = PhoneOTPService._send_sms_simple(phone_number, otp_instance.otp_code)
                print(f"Service: SMS send result: {sms_success}")
            except Exception as e:
                print(f"Service: Error sending SMS: {e}")
                sms_success = False
            
            if sms_success:
                print(f"Service: Success - OTP sent to {phone_number}")
                return {
                    'success': True,
                    'message': 'OTP sent successfully',
                    'expires_in': getattr(settings, 'PHONE_OTP_EXPIRE_TIME', 300)
                }
            else:
                print(f"Service: SMS failed, deleting OTP")
                otp_instance.delete()
                return {
                    'success': False,
                    'message': 'Failed to send SMS'
                }
                
        except Exception as e:
            print(f"Service: Critical error: {e}")
            import traceback
            print(f"Service: Traceback: {traceback.format_exc()}")
            return {
                'success': False,
                'message': f'Service error: {str(e)}'
            }
    
    @staticmethod
    def _send_sms_simple(phone_number, otp_code):
        """Simplified SMS sending"""
        try:
            print(f"SMS: Attempting to send to {phone_number}")
            
            # Check if Twilio credentials exist
            twilio_sid = getattr(settings, 'TWILIO_ACCOUNT_SID', '')
            twilio_token = getattr(settings, 'TWILIO_AUTH_TOKEN', '')
            
            if twilio_sid and twilio_token:
                print("SMS: Twilio credentials found, attempting real SMS")
                try:
                    from twilio.rest import Client
                    client = Client(twilio_sid, twilio_token)
                    
                    expire_minutes = getattr(settings, 'PHONE_OTP_EXPIRE_TIME', 300) // 60
                    message_body = f"Your verification code is: {otp_code}. Valid for {expire_minutes} minutes."
                    
                    message = client.messages.create(
                        body=message_body,
                        from_=getattr(settings, 'TWILIO_PHONE_NUMBER', ''),
                        to=phone_number
                    )
                    
                    print(f"SMS: Sent via Twilio, SID: {message.sid}")
                    return True
                    
                except Exception as e:
                    print(f"SMS: Twilio error: {e}")
                    return False
            else:
                # Development mode - just log
                print(f"SMS: [DEVELOPMENT MODE] OTP {otp_code} for {phone_number}")
                print(f"📱 SMS OTP: {otp_code} sent to {phone_number}")
                return True
                
        except Exception as e:
            print(f"SMS: Error in _send_sms_simple: {e}")
            return False
    
    @staticmethod
    def verify_otp(phone_number, otp_code):
        """Verify OTP code - SIMPLIFIED"""
        try:
            print(f"Service: Verifying OTP {otp_code} for {phone_number}")
            
            otp_instance = PhoneOTP.objects.filter(
                phone_number=phone_number,
                otp_code=otp_code,
                is_verified=False
            ).first()
            
            if not otp_instance:
                return {'success': False, 'message': 'Invalid OTP code'}
            
            otp_instance.attempts += 1
            otp_instance.save()
            
            if otp_instance.is_expired():
                return {'success': False, 'message': 'OTP has expired'}
            
            if otp_instance.is_max_attempts_reached():
                return {'success': False, 'message': 'Maximum attempts reached'}
            
            otp_instance.is_verified = True
            otp_instance.save()
            
            return {'success': True, 'message': 'Phone number verified successfully'}
            
        except Exception as e:
            print(f"Service: Verify error: {e}")
            return {'success': False, 'message': f'Verification error: {str(e)}'}