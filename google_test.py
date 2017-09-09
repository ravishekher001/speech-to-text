import google.auth
from google.cloud import speech


credentials, project = google.auth.default()
# import ipdb; ipdb.set_trace()
# credentials = credentials.create_scoped(['https://www.googleapis.com/auth/cloud-platform'])

client = speech.SpeechClient()
# client = speech.SpeechClient()
with open('rooney-short.flac', 'rb') as fp:
    content = fp.read()

audio = speech.types.RecognitionAudio(content=content)

config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,
        # sample_rate_hertz=16000,
        language_code='en-GB')
response = client.recognize(config, audio)
import ipdb; ipdb.set_trace()
alternatives = response.results[0].alternatives
for alternative in alternatives:
    print(alternative.transcript)


#
# client = speech.Client()
# # client = Client.from_service_account_json('speech-test-1-21f6ae68d225.json')
# client = speech.SpeechClient()
#
# import ipdb; ipdb.set_trace()
# pass
