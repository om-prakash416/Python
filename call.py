from twilio.rest import Client
import time

# Your Twilio account credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_phone_number'

# List of phone numbers to call
phone_numbers = ['+1234567890', '+9876543210', ...]  # Add your phone numbers here

# Audio URL to play during the call
audio_url = 'https://example.com/your-audio-file.mp3'


def make_call(phone_number):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to=phone_number,
        from_=twilio_number,
        url=audio_url,
        method='GET'
    )
    return call.sid


def main():
    for number in phone_numbers:
        call_sid = make_call(number)
        print(f"Calling {number} (Call SID: {call_sid})")
        time.sleep(10)  # Wait for 10 seconds before making the next call


if __name__ == '__main__':
    main()
